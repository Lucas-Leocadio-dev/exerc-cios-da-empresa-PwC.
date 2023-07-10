#NOTA: maiúsculas e minúsculas diferem no palíndromo. Caso não seja para diferenciar, retire o "#" após o "input()".
frase = input()#.upper()
#técnica do slicing reverso para checar a frase
if frase == frase[::-1]: 
    print("True")
else:
    print("False")