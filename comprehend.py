import json
import boto3

comprehend = boto3.client(service_name = 'comprehend', region_name = 'us-west-2')

pdf_text = """
            John W. Smith
            2002 Front Range Way Fort Collins, CO 80525
            jwsmith@colostate.edu

            Career Summary 

            Four years experience in early childhood development with a di verse background in the care of 
            special needs children and adults.

            Adult Care Experience

            • Determined work placement for 150 special needs adult clients.
            • Maintained client databases and records.
            • Coordinated client contact with local health care professionals on a monthly basis.
            • Managed 25 volunteer workers.

            Childcare Experience

            • Coordinated service assignments for 20 part -time counselors and 100 client families. 
            • Oversaw daily activity and outing planning for 100 clients.
            • Assisted families of special needs clients with researching financial assistance and 
            healthcare. 
            • Assisted teachers with managing daily classroom activities.
            • Oversaw daily and special st udent activities.

            Employment History
            1999-2002  Counseling Supervisor, The Wesley Ce nter, Little Rock, Arkansas.
            1997-1999  Client Specialist, Rainbow Special Ca re Center, Little Rock, Arkansas
            1996-1997 Teacher’s Assistant, Cowell Elem entary, Conway, Arkansas

            Education 

            University of Arkansas at Little Rock, Little Rock, AR

            • BS in Early Childhood Development (1999) 
            • BA in Elementary Education (1998) 
            • GPA (4.0 Scale):  Early Childhood Developm ent – 3.8, Elementary Education – 3.5, 
            Overall 3.4.
            • Dean’s List, Chancellor’s List
            """

pii_output = comprehend.detect_pii_entities(Text=pdf_text, LanguageCode='en')

#dumps turns JSON to Python string
#loads turns Python string to JSON
#print(json.dumps(pii_output, indent = 2))

pii_words = []

for entry in pii_output["Entities"]:
    type = entry["Type"]
    if (type == "NAME" or type == "ADDRESS" or type == "EMAIL" or type == "PHONE" or type == "AGE"):
        start = entry["BeginOffset"]
        end =   entry["EndOffset"]
        word =  pdf_text[start:end]
        pii_words.append(word)

for word in pii_words:
    print(word)
