def divisao(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
        return None
    else:
        print("Divisão realizada com sucesso!")
        return resultado
    finally:
        print("Finalizando a tentativa de divisão.")


# O bloco finally é sempre executado,
# independentemente de ocorrer ou não uma exceção.

print("Resultado 1:", divisao(10, 2))
print("Resultado 2:", divisao(10, 0))
