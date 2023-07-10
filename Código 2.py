frase = input()
# declarada uma string como vazia para que sejam adicionados caracteres dentro desta variável
frase_sem_repeticao = ""
#percorre todas as letras dentro da frase
for letras in frase:
    # se a letra não tá dentro da outra variável, ele adiciona. Se ela já está inserida
    # não adicionará de novo
    if letras not in frase_sem_repeticao:
        frase_sem_repeticao += letras
print(frase_sem_repeticao)