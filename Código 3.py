texto = input()
palindromos = []
# dentro desta variável, serão executados todos estes passos:
# 1 - Remove pontuação e espaços em branco para auxiliar na execução do código
# 2 - comando isalnum(): checagem que retorna booleano para saber se todos os caracteres da string são alfanuméricos
texto_formatado = ''.join(c for c in texto if c.isalnum())

# Verificar trechos de texto
for i in range(len(texto_formatado)):
    # é necessário o i + 2 pela questão do palíndromo. Se não tiver esse  + 2 e for + 1, ele vai entender qualquer caractere como palíndromo.
    #o + 1 garante que o laço percorrerá toda a string
    for j in range(i + 2, len(texto_formatado) + 1):
        trecho = texto_formatado[i:j]

        if trecho == trecho[::-1]:
            palindromos.append(trecho)

if palindromos:
    print("Palíndromos encontrados:")
    print(palindromos)
else:
    print("Nenhum palíndromo encontrado.")