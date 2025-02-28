# Escreva um programa que inverta uma string utilizando um laço for. Por exemplo, para a string "PAPAGAIO",
# o resultado deve ser "OIAGAPAP".

texto = "PAPAGAIO"
invertido = ""

for letra in texto:
    invertido = letra + invertido  # Adiciona cada letra na frente do texto já invertido

print(f"String original: {texto}")
print(f"String invertida: {invertido}")

# Cada letra é adicionada no início da string invertido, o que faz com que a string fique ao contrário.
