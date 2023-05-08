import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia("en")

page = wiki_wiki.page("India")

for s in page.sections:
    print(s.title, ':', s.text, s.sections,"\n\n\n")