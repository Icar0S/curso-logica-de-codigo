# Função que converte temperatura de Celsius para Fahrenheit
def converter_para_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Chamando a função várias vezes com valores diferentes
temperatura1 = converter_para_fahrenheit(0)
temperatura2 = converter_para_fahrenheit(25)
temperatura3 = converter_para_fahrenheit(100)

print(f"0°C = {temperatura1}°F")
print(f"25°C = {temperatura2}°F")
print(f"100°C = {temperatura3}°F")