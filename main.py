from funcs import *

# Escreva abaixo o nome do arquivo do PDF a ser traduzido (Ele precisa estar nesta pasta)
arquivo_pdf = 'Mushoku Tensei Jobless Reincarnation Vol. 17.pdf'

# Diga a partir de que página se tem o início (Ignore páginas sem nada escrito)
numero_pagina = 11

# Criando variável com nome do PDF e Word traduzido
arquivo_pdf_pronto = f'Traduzido_{arquivo_pdf}'
arquivo_word_pronto = 'temporario.docx'

# Criando PDF e adicionando as páginas que não precisam de tradução
add_pages_anteriores_pdf(arquivo_pdf, numero_pagina, arquivo_pdf_pronto)

# Criando arquivo Word temporário
criar_arquivo_word(arquivo_word_pronto)

while True:
    # Pega a página do livro
    extrair_pagina(arquivo_pdf, numero_pagina)
    pagina = 'pagina.pdf'

    # Verifica se a página existe (se não existir, encerra o loop)
    # if not os.path.exists(pagina):
    #     break

    if numero_pagina == 17:
        break

    # Converter a página em texto
    pagina_conteudo = converter_pagina_em_texto(pagina)
    pagina_conteudo = str(pagina_conteudo)

    print(f"Pagina numero {numero_pagina} convertida em texto!")

    # Preservar nomes próprios
    pagina_conteudo, nomes_proprios = preservar_nomes_proprios(pagina_conteudo)

    # Escolher idioma ao qual vai ser traduzido
    Idioma_Requerido = 'portuguese'

    # Traduzir o texto com repetição
    pagina_traduzida = traduzir_com_repeticao(pagina_conteudo, Idioma_Requerido, tentativas=3)

    # Substituir os marcadores pelos nomes próprios normais
    for marcador, nome in nomes_proprios.items():
        pagina_traduzida = pagina_traduzida.replace(marcador, nome)

    # Limpar resquícios de código do texto
    pagina_traduzida_estilizada = limpar_texto(pagina_traduzida)

    print(f"Pagina numero {numero_pagina} traduzida e estilizada!")

    # Chame a função para adicionar as páginas traduzidas no PDF final
    add_pags_no_word(arquivo_word_pronto, pagina_traduzida_estilizada)

    print(f"Pagina numero {numero_pagina} adicionada no arquivo Word!")

    # Lógica para que as páginas continuem aumentando até chegar na última
    numero_pagina += 1

# Processar arquivos (converter Word para PDF e juntar PDFs)
processar_arquivos(arquivo_word_pronto, arquivo_pdf_pronto)
