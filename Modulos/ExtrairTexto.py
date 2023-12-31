from PyPDF2 import PdfReader, PdfWriter, PageObject
from io import BytesIO
from reportlab.pdfgen import canvas

def extrair_pagina(pdf_file, numero_pagina):
    with open(pdf_file, 'rb') as f:
        pdf_leitor = PdfReader(f)
        pdf_escrever = PdfWriter()

        pdf_escrever.addPage(pdf_leitor.getPage(numero_pagina - 1))

        return pdf_escrever

def converter_pagina_em_texto(pagina):
    pdf_leitor = PdfReader('Mushoku Tensei Jobless Reincarnation Vol. 17.pdf')

    pagina_conteudo = {}

    for indx, pdf_pag in enumerate(pdf_leitor.pages):
        pagina_conteudo[indx + 1] = pdf_pag.extract_text()

    return pagina_conteudo

def converter_texto_em_pagina(texto):
    # Cria um novo objeto PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    # Adiciona o texto ao PDF
    c.drawString(100, 750, texto)

    # Finaliza o PDF
    c.save()

    # Cria um objeto PageObject a partir do PDF
    buffer.seek(0)
    nova_pagina = PageObject.createBlankPage(None, 595, 842)
    nova_pagina.mergePage(PdfReader(buffer).getPage(0))

    return nova_pagina