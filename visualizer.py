import turtle


def draw(positions, world_size):
    scale = 300 / world_size

    screen = turtle.Screen()
    screen.title("ARES Mission - Trasa Łazika")
    screen.bgcolor("black")
    screen.setup(width=700, height=700)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # granice świata
    t.color("gray")
    t.penup()
    t.goto(-world_size * scale, -world_size * scale)
    t.pendown()
    for corner in [
        (-world_size * scale,  world_size * scale),
        ( world_size * scale,  world_size * scale),
        ( world_size * scale, -world_size * scale),
        (-world_size * scale, -world_size * scale),
    ]:
        t.goto(corner)

    # osie
    t.color("#333333")
    t.penup()
    t.goto(-world_size * scale, 0)
    t.pendown()
    t.goto(world_size * scale, 0)
    t.penup()
    t.goto(0, -world_size * scale)
    t.pendown()
    t.goto(0, world_size * scale)

    # cel (0,0) — biały krzyżyk
    t.color("white")
    t.penup()
    t.goto(-8, 0)
    t.pendown()
    t.goto(8, 0)
    t.penup()
    t.goto(0, -8)
    t.pendown()
    t.goto(0, 8)

    # trasa
    t.color("orange")
    t.penup()
    t.goto(positions[0][0] * scale, positions[0][1] * scale)
    t.pendown()
    for x, y in positions[1:]:
        t.goto(x * scale, y * scale)

    # punkt startowy — zielone kółko
    t.penup()
    t.color("green")
    sx, sy = positions[0]
    t.goto(sx * scale, sy * scale - 6)
    t.pendown()
    t.circle(6)

    # punkt końcowy — czerwone kółko
    t.penup()
    t.color("red")
    ex, ey = positions[-1]
    t.goto(ex * scale, ey * scale - 6)
    t.pendown()
    t.circle(6)

    # legenda (napis)
    t.penup()
    t.color("white")
    t.goto(-world_size * scale + 5, world_size * scale + 10)
    t.write("● START", font=("Arial", 9, "normal"))

    try:
        turtle.done()
    except Exception:
        pass