# Função para converter de quilômetros para milhas
def km_para_milhas(km):
    return km * 0.621371

# Função para converter de milhas para quilômetros
def milhas_para_km(milhas):
    return milhas / 0.621371

# Função para selecionar o tipo de conversão
def escolher_conversao():
    print("Escolha o tipo de conversão:")
    print("1 - Quilômetros para Milhas")
    print("2 - Milhas para Quilômetros")
    opcao = int(input("Digite sua opção (1 ou 2): "))
    return opcao

# Função principal
def main():
    opcao = escolher_conversao()
    
    if opcao == 1:
        km = float(input("Digite a distância em quilômetros: "))
        milhas = km_para_milhas(km)
        print(f"{km} quilômetros equivalem a {milhas:.2f} milhas.")
    elif opcao == 2:
        milhas = float(input("Digite a distância em milhas: "))
        km = milhas_para_km(milhas)
        print(f"{milhas} milhas equivalem a {km:.2f} quilômetros.")
    else:
        print("Opção inválida. Tente novamente.")

# Executando o programa
main()
