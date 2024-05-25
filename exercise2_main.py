import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / (2 * 3**0.5))
    t.pendown()

    draw_koch_snowflake(t, order, size)

    window.mainloop()

if __name__ == "__main__":

    while True:
        try:
            order = int(input("Введіть рівень рекурсії: "))
            if order < 0:
                raise ValueError
            break
        except ValueError:
            print("Будь ласка, введіть коректне число.")
    

    draw_koch_curve(order)
