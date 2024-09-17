import turtle
# Função para desenhar uma estrela
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)  #  angulo para criar uma estrela
# Configurar a tartaruga
t = turtle.Turtle()
# Desenhar uma estrela de tamanho 100
draw_star(100)
turtle.done()

