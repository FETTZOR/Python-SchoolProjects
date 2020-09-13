import spacy

nlp = spacy.load("en_core_web_md")


doc2 = nlp("Music is an art form, and cultural activity, whose medium is sound. General definitions of music include common Greek")
for ent in doc2.ents:
    print(ent.text, ent.label_)