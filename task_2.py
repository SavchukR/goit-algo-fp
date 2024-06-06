import turtle
import math

def draw_pifagor_tree(t, length, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pifagor_tree(t, length * math.sqrt(2) / 2, depth - 1)
    t.right(90)
    draw_pifagor_tree(t, length * math.sqrt(2) / 2, depth - 1)
    t.left(45)
    t.backward(length)

def draw_fractal_tree(levels):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(0, -200)
    t.pendown()
    # init angle
    t.left(90)

    draw_pifagor_tree(t, 100, levels)

    t.hideturtle() 

    screen.mainloop()

if __name__ == "__main__":
    levels = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    draw_fractal_tree(levels)
