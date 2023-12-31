from PyPDF2 import *
from deep_translator import GoogleTranslator
import spacy

def extrair_pagina(arquivo_pdf, numero_pagina):
    with open(arquivo_pdf, 'rb') as f:
        leitor_pdf = PdfReader(f)
        escritor_pdf = PdfWriter()

        escritor_pdf.add_page(leitor_pdf.pages[numero_pagina - 1])

        with open('pagina.pdf', 'wb') as pdf_saida:
            escritor_pdf.write(pdf_saida)


def converter_pagina_em_texto(pagina):
    pdf_leitor = PdfReader(pagina)

    pagina_conteudo = {}

    for indx, pdf_pag in enumerate(pdf_leitor.pages):
        pagina_conteudo[indx + 1] = pdf_pag.extract_text()

    return pagina_conteudo


def texto_traduzir(conteudo_pagina, idioma_requerido):
    # Traduzir o conteúdo da página para o idioma requerido usando o DeepL
    texto_traduzido = GoogleTranslator(source='auto', target=idioma_requerido).translate(text=conteudo_pagina)

    return texto_traduzido


def limpar_texto(texto):
    # Remover caracteres indesejados
    texto = texto.replace(r'\n', ' ')  # Substituir quebras de linha por espaços
    texto = texto.replace('{', '')  # Remover chaves abertas
    texto = texto.replace('}', '')  # Remover chaves fechadas
    texto = texto.replace("'", '')  # Remover aspas simples
    return texto


def preservar_nomes_proprios(texto, idioma='pt_core_news_sm'):
    # Carregue o modelo de linguagem spaCy
    nlp = spacy.load(idioma)

    # Processar o texto
    doc = nlp(texto)

    # Dicionário para mapear cada nome próprio para um marcador único
    nomes_proprios = {}

    # Substituir nomes próprios por um marcador único
    for ent in doc.ents:
        if ent.label_ == 'PER':
            marcador = '<NOMEPROPRIO{}>'.format(len(nomes_proprios))
            texto = texto.replace(ent.text, marcador)
            nomes_proprios[marcador] = ent.text

    return texto, nomes_proprios


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
