from funcs import *

arquivo_pdf = 'Mushoku Tensei Jobless Reincarnation Vol. 17.pdf'
numero_pagina = 12

# Extrair a página do PDF
extrair_pagina(arquivo_pdf, numero_pagina)

pagina = 'pagina.pdf'

# Converter a página em texto
pagina_conteudo = converter_pagina_em_texto(pagina)
pagina_conteudo = str(pagina_conteudo)

# Preservar nomes próprios
pagina_conteudo, nomes_proprios = preservar_nomes_proprios(pagina_conteudo)

Idioma_Requerido = 'portuguese'

# Traduzir o texto
pagina_traduzida = texto_traduzir(pagina_conteudo, Idioma_Requerido)

# Substituir os marcadores pelos nomes próprios originais
for marcador, nome in nomes_proprios.items():
    pagina_traduzida = pagina_traduzida.replace(marcador, nome)

# Limpar o texto
pagina_traduzida_estilizada = limpar_texto(pagina_traduzida)

print(pagina_traduzida_estilizada)
