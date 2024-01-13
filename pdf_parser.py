import fitz  # PyMuPDF library

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

    pdf_document.save(f"anonymous_{pdf_path}")
    pdf_document.close()

if __name__ == "__main__":
    # We need a way to dynamically run the pdf file through Amazon Comprehend to retrieve the pii_list first using a dynamically retrieved pdf path based on what the user uploaded
    pdf_path = "example2.pdf"
    pii_words = ["John W. Smith", "2002 Front Range Way Fort Collins, CO 80525", "jwsmith@colostate.edu"]  # Example PII words

    edit_pdf(pdf_path, pii_words)
