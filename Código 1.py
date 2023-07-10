# Digitação da frase
frase = input()
# Dividindo a frase em uma lista de palavras
palavras = frase.split()
# Declaração de uma variável lista que conterá todas as palavras obtidas no split
lista_palavras = []
# Pegando uma palavra por vez das palavras digitadas pelo usuário e adicionando dentro da lista
for palavra in palavras: 
    lista_palavras.append(palavra)

# Invertendo a ordem das palavras
lista_palavras.reverse()
# Concatenando as palavras em uma única variável do tipo string 
frase_final = " ".join(lista_palavras)
print(frase_final)
