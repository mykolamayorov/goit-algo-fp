import turtle
import math

def draw_square(t, p1, p2, p3, p4):
    """Малює квадрат за 4 точками"""
    t.up()
    t.goto(p1)
    t.down()
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)
    t.goto(p1)
    t.end_fill()

def draw_tree(t, p1, p2, level):
    if level == 0:
        return

    # Вектор сторони
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    # Точки квадрата
    p3 = (p2[0] - dy, p2[1] + dx)
    p4 = (p1[0] - dy, p1[1] + dx)

    # Малюємо квадрат
    draw_square(t, p1, p2, p3, p4)

    # Вершина трикутника (гіпотенуза квадрата)
    px = p4[0] + (dx - dy) / 2
    py = p4[1] + (dy + dx) / 2

    # Рекурсивно малюємо ліве та праве піддерево
    draw_tree(t, p4, (px, py), level - 1)
    draw_tree(t, (px, py), p3, level - 1)

def main():
    try:
        level = int(input("Введіть рівень рекурсії (рекомендується 5–10): "))
        if level < 1 or level > 12:
            print("Рівень має бути в межах 1–12.")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    turtle.speed(0)
    turtle.hideturtle()
    turtle.color("green", "lightgreen")
    turtle.bgcolor("white")

    side = 100
    p1 = (-side // 2, -250)
    p2 = (side // 2, -250)

    draw_tree(turtle, p1, p2, level)

    turtle.done()

if __name__ == "__main__":
    main()