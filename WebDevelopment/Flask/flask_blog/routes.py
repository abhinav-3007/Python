import os
import secrets
from PIL import Image
from flask import render_template, redirect, flash, url_for, request, abort
from flask_blog.forms import SignUpForm, LoginForm, PostForm, UpdateProfileForm, UpdatePostForm
from flask_blog import db, app, bcrypt
from flask_blog.models import Post, User
from flask_login import login_user, logout_user, current_user, login_required

with app.app_context():
    db.create_all()

    about_info ={
        "name" : "Abhi's Blog",
        "tagline" : "Share your thoughts on this site for others to see.",
        "about" : "This is a website made to give you a platform where you can share your thoughts and ideas amongst other "
                  "things with the world.",
        "picture" : "b_logo.png"
    }


    @app.route("/")
    @app.route("/home")
    def home():
        page = request.args.get("page", 1, type=int)
        data = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template("home.html", posts=data, title="Home", about_info=about_info)


    @app.route("/about")
    def about():
        return render_template("about.html", title="About", about_info=about_info)


    @app.route("/login", methods=["GET", "POST"])
    def login():
        login_form = LoginForm()
        if login_form.validate_on_submit():
            user = User.query.filter_by(email=login_form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, login_form.password.data):
                login_user(user, remember=login_form.remember_me.data)
                next_page = request.args.get("next")
                flash("You have logged in successfully!", "success")
                return redirect(next_page) if next_page else redirect(url_for("home"))
            else:
                flash("Login Failed. Please check your Email ID and Password ", "danger")
        return render_template("login.html", title="Login", form=login_form)


    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        signup_form = SignUpForm()
        if signup_form.validate_on_submit():
            hash_password = bcrypt.generate_password_hash(signup_form.password.data).decode("utf-8")
            user = User(first_name=signup_form.first_name.data, last_name=signup_form.last_name.data,
                        email=signup_form.email.data, password=hash_password)
            db.session.add(user)
            db.session.commit()
            flash(f"Your account has been created! You can login now.", "success")
            return redirect(url_for("login"))
        return render_template("signup.html", title="Sign Up", form=signup_form)

    @app.route("/logout")
    def logout():
        logout_user()
        flash(f"You have been successfully been logged out.", "success")
        return redirect(url_for("login"))


    def save_profile_picture(picture):
        random_hex = secrets.token_hex(8)
        _, fext = os.path.splitext(picture.filename)
        picture_fname = random_hex+fext
        picture_path = os.path.join(app.root_path, "static/profile_pictures", picture_fname)

        output_size = (150,150)
        p_pic = Image.open(picture)
        p_pic.thumbnail(output_size)
        p_pic.save(picture_path)

        return picture_fname


    @app.route("/profile", methods=["GET", "POST"])
    @login_required
    def profile():
        update_form = UpdateProfileForm()
        if update_form.validate_on_submit():
            current_user.first_name = update_form.first_name.data
            current_user.last_name = update_form.last_name.data
            current_user.email = update_form.email.data
            current_user.about_me = update_form.about_me.data
            if update_form.profile_pic.data:
                picture_file = save_profile_picture(update_form.profile_pic.data)
                if current_user.profile_pic != "default.png":
                    remove_path = os.path.join(app.root_path, "static/profile_pictures", current_user.profile_pic)
                    os.remove(remove_path)
                current_user.profile_pic = picture_file
            db.session.commit()
        elif request.method == "GET":
            update_form.first_name.data = current_user.first_name
            update_form.last_name.data = current_user.last_name
            update_form.email.data = current_user.email
            update_form.about_me.data = current_user.about_me
        image_file = url_for("static", filename="profile_pictures/"+current_user.profile_pic)
        return render_template("profile.html", title="Profile", image_file=image_file, form=update_form)


    def save_post_picture(picture):
        random_hex = secrets.token_hex(8)
        _, fext = os.path.splitext(picture.filename)
        picture_fname = random_hex+fext
        picture_path = os.path.join(app.root_path, "static/images", picture_fname)

        output_size = (800,600)
        p_pic = Image.open(picture)
        p_pic.thumbnail(output_size)
        p_pic.save(picture_path)

        return picture_fname


    @app.route("/post/add", methods=["GET","POST"])
    @login_required
    def add_post():
        post_form = PostForm()
        p_pic = None
        if post_form.validate_on_submit():
            if post_form.post_pic.data:
                p_pic = save_post_picture(post_form.post_pic.data)
            post = Post(title=post_form.title.data, content=post_form.content.data, user_id=current_user.id, post_pic=p_pic)
            db.session.add(post)
            db.session.commit()
            flash("Your post has been added", "success")
            return redirect(url_for("home"))

        return render_template("add_post.html", title="Add Post", form=post_form)


    @app.route("/post/<int:post_id>", methods=["GET", "POST"])
    def post(post_id):
        post = Post.query.get_or_404(post_id)
        update_post_form = UpdatePostForm()
        if update_post_form.validate_on_submit():
            post.title=update_post_form.title.data
            post.content = update_post_form.content.data
            if update_post_form.post_pic.data:
                picture_file = save_post_picture(update_post_form.post_pic.data)
                if post.post_pic:
                    remove_path = os.path.join(app.root_path, "static/images", post.post_pic)
                    os.remove(remove_path)
                post.post_pic = picture_file
            db.session.commit()
            flash("Your post has been updated", "success")
            return redirect(url_for("post", post_id=post.id))
        elif request.method == "GET":
            update_post_form.title.data = post.title
            update_post_form.content.data = post.content
        return render_template("post.html", title=post.title, post=post, form=update_post_form)


    @app.route("/post/<int:post_id>/delete", methods=["POST", "GET"])
    @login_required
    def delete_post(post_id):
        post = Post.query.get_or_404(post_id)
        if post.creator != current_user:
            abort(403)
        if post.post_pic:
            remove_path = os.path.join(app.root_path, "static/images", post.post_pic)
            os.remove(remove_path)
        db.session.delete(post)
        db.session.commit()
        flash("Your post has been deleted", "success")
        return redirect(url_for("home"))


    @app.route("/post/<int:post_id>/delete_post_picture", methods=["POST", "GET"])
    @login_required
    def delete_post_picture(post_id):
        post = Post.query.get_or_404(post_id)
        if post.creator != current_user:
            abort(403)
        if post.post_pic:
            remove_path = os.path.join(app.root_path, "static/images", post.post_pic)
            os.remove(remove_path)
            post.post_pic = None
            db.session.commit()
            flash("Your post picture has been deleted", "success")
        else:
            flash("Post picture does not exist", "warning")
        return redirect(url_for("post", post_id=post_id))


    @app.route("/profile/<int:user_id>")
    def profile_by_id(user_id):
        user = User.query.get_or_404(user_id)
        data = Post.query.filter_by(creator=user).order_by(Post.date_posted.desc()).all()
        return render_template("user.html", title=f"{user.first_name} {user.last_name}", profile=user, posts=data)


    @app.errorhandler(404)
    def error_404(error):
        return render_template("errors/404.html")


    @app.errorhandler(403)
    def error_404(error):
        return render_template("errors/403.html")


    @app.errorhandler(500)
    def error_500(error):
        return render_template("errors/500.html")
