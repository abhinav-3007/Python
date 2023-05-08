from flask_blog import db
from datetime import datetime
from flask_login import UserMixin
from flask_blog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    about_text = "Hello there! I love blogging!"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    profile_pic = db.Column(db.String(60), nullable=False, default="default.png")
    about_me = db.Column(db.Text, nullable=False, default=about_text)
    posts = db.relationship("Post", backref="creator", lazy=True)

    def __repr__(self):
        return f"User('{self.id}', '{self.first_name}', '{self.last_name}', '{self.email}', {self.profile_pic}, " \
               f"'{self.about_me}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    post_pic = db.Column(db.String(60), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.content}',{self.post_pic} , '{self.date_posted}', '{self.user_id}')"
