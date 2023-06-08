# Crie um programa que leia o nome de uma cidade e diga se ela começa com "SANTO"
cid = str(input('Em que Cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

# .strip() tiro os espaços do começo e do fim da frase
# Usei o Upper() para colocar o nome em Maiusculo para independer da forma que escrevo