import json
import boto3

comprehend = boto3.client(service_name = 'comprehend', region_name = 'us-west-2')

pii_words = """
            jasonwang@ucsb.edu, Jason Wang, 909-616-8947
            """

pii_output = comprehend.detect_pii_entities(Text=pii_words, LanguageCode='en')

#dumps turns JSON to Python string
#loads turns Python string to JSON
print(json.dumps(pii_output, indent = 2))

