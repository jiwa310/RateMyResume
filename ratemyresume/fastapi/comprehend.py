import json
import boto3
import fitz
import PyPDF2

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

def edit_pdf(pdf_path, pii_words):
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        # Iterate through PII words
        for pii_word in pii_words:
            # Search for the PII word on the page
            instances = page.search_for(pii_word)

            # Redact each instance with a black rectangle
            for instance in instances:
                rect = fitz.Rect(instance)
                rc = page.add_redact_annot(rect, fill=(0,0,0))
                page.apply_redactions()

    # pdf_document.save(f"anonymous_{pdf_path}")
    pdf_document.save()
    pdf_document.close()


# if __name__ == "__main__":
#     text_reader = PyPDF2.PdfReader("example2.pdf")

#     pdf_text = text_reader.pages[0]
#     text = pdf_text.extract_text()
#     pii_words = get_pii_words(text)
#     # for word in pii_words:
#     #     print(word)
#     edit_pdf("example2.pdf", pii_words)