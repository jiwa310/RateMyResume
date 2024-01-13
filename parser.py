import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for token in doc:
#     print(token.text)

nlp = spacy.load("en_core_web_lg")
doc = nlp(" Vincent Cheong 909-551-8312 | vcheong0202@gmail.com | website | linkedin |  github  EDUCATION University of California — Santa Barbara, Santa Barbara, CA	   Sep. 2022 — Present Major: Computer Engineering B.S. GPA: 3.83 - Dean’s List Engineering")

for ent in doc.ents:
    # if ent.label_ == "PERSON" or ent.label_ == "ORG":
        print(ent.text, ent.label_)