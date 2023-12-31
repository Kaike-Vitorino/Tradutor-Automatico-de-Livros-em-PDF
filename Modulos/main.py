from ExtrairTexto import *
from TraducaoAPI import *
from LivroPronto import *
from PyPDF2.pdf import PageObject

def main():
    # Defina o arquivo PDF e as páginas que você deseja traduzir
    pdf_file = "seu_arquivo.pdf"
    start_page = 1
    end_page = 10
    target_language = "pt"

    # Dicionário para armazenar as páginas traduzidas
    translated_pages = {}

    # Loop através das páginas do PDF
    for page_num in range(start_page, end_page + 1):
        # Extrair a página
        page_writer = extrair_pagina(pdf_file, page_num, page_num)

        # Converter a página em texto para tradução
        page_text = convert_page_to_text(page_writer.getPage(0))

        # Traduzir o texto da página
        translated_text = texto_traduzir(page_text, target_language)

        # Converter o texto traduzido de volta para uma página PDF
        translated_page = convert_text_to_page(translated_text)

        # Adicionar a página traduzida ao dicionário
        translated_pages[page_num - 1] = translated_page

    # Adicionar as páginas traduzidas ao PDF
    add_pags_no_pdf(pdf_file, translated_pages)

if __name__ == "__main__":
    main()
