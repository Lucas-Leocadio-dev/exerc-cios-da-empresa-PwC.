frase = input()
caracteres = []
# Aqui, é declarada uma variável booleana para indicar que a próxima letra será maiúscula
prox_letra_maiuscula = True
# Percorrerá todos os caracteres dentro da frase
for caractere in frase:
    # checa se o caractere encontrado é um destes três (pontuação que indica o começo de uma próxima frase)
    if caractere in [ '.', '!', '?']:
        #adiciona a pontuação
        caracteres.append(caractere)
        # é necessário permanecer com essa declaração porque, caso caia aqui, garantirá a condição de verdadeiro.
        prox_letra_maiuscula = True
    # se o caractere encontrado for alfanumérico, cairá na continuação, se não for, será adicionado da mesma forma
    # fora necessário adicionar "caractere.isalnum", pois se vier um número, o caractere alfabético próximo não ficará maiúsculo
    elif caractere.isalnum():
        if prox_letra_maiuscula:
            # adicionará como letra maiúscula e logo em seguida nega que o próximo deve ser maiúscula
            # pois senão todas as letras seriam maiúsculas
            caracteres.append(caractere.upper())
            prox_letra_maiuscula = False
        else:
            caracteres.append(caractere)
    else:
        caracteres.append(caractere)
# une tudo em uma string só e mostra o resultado ao usuário
print(''.join(caracteres))