import json
import boto3

comprehend = boto3.client(service_name = 'comprehend', region_name = 'us-west-2')

def get_pii_words(pdfText):
    pdf_text = pdfText
    pii_output = comprehend.detect_pii_entities(Text=pdf_text, LanguageCode='en')

    #dumps turns JSON to Python string
    #loads turns Python string to JSON
    #print(json.dumps(pii_output, indent = 2))

    pii_words = []

    for entry in pii_output["Entities"]:
        type = entry["Type"]
        if (type == "NAME" or type == "ADDRESS" or type == "EMAIL" or type == "PHONE" or type == "AGE"):
            score = entry["Score"]
            start = entry["BeginOffset"]
            end =   entry["EndOffset"]
            word =  pdf_text[start:end]
            pii_words.append(word)
            #print(str(score) + ' ' + word + ' ' + type)

    return pii_words
    


# def main(): 
#     array = get_pii_words("""
#                         gnawnasoj@outlook.com
#                         123-456-7890
#                         California
#                         """)
    
#     for word in array:
#         print(word)

# if __name__=="__main__": 
#     main()
