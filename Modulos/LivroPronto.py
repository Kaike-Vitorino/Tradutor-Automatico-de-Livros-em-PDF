from ExtrairTexto import *

def add_pags_no_pdf(pdf_file, translated_pages):
    with open(pdf_file, 'rb') as f:
        pdf_ler = PdfReader(f)
        pdf_escrever = PdfFileWriter()

        for page_num in range(pdf_ler.getNumPages()):
            if page_num in translated_pages:
                pdf_escrever.addPage(translated_pages[page_num])
            else:
                pdf_escrever.addPage(pdf_ler.getPage(page_num))

        with open('translated.pdf', 'wb') as output_pdf:
            pdf_escrever.write(output_pdf)
