# Função que verifica se uma pessoa pode entrar em um clube baseado na idade e em outros fatores
def pode_entrar_clube(idade, convidado_vip, comportamento_inadequado):
    # Regras:
    # 1. A pessoa pode entrar se tiver mais de 18 anos ou for convidado VIP.
    # 2. A pessoa não pode entrar se tiver comportamento inadequado.
    
    if comportamento_inadequado:
        print("Entrada negada devido ao comportamento inadequado.")
    elif idade >= 18 or convidado_vip:  # Usando o "OR" para permitir entrada se qualquer uma das condições for verdadeira
        print("Entrada permitida.")
    else:
        print("Entrada negada devido à idade.")
        
# Exemplo de uso com dados de entrada:
idade = int(input("Digite sua idade: "))
convidado_vip = input("Você é um convidado VIP? (s/n): ").lower() == "s"
comportamento_inadequado = input("Você está com comportamento inadequado? (s/n): ").lower() == "s"

# Chamando a função
pode_entrar_clube(idade, convidado_vip, comportamento_inadequado)

# Exemplo do uso de "!=" e "not" separadamente:
# Verifica se a pessoa não é VIP e não tem comportamento inadequado
if not convidado_vip and comportamento_inadequado != False:
    print("Você não é VIP e seu comportamento é inadequado. Saída imediata.")
else:
    print("Você está liberado, seja VIP ou esteja com comportamento adequado.")