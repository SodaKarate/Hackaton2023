import random

# pályaméretek
WIDTH = 60
HEIGHT = 30

# Kigyó kezdőpozíciója
snake_x = random.randint(1, WIDTH-2)
snake_y = random.randint(1, HEIGHT-2)

# pálya inditása
board = []
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        if x != 0 and x != WIDTH-1 and y != 0 and y != HEIGHT-1:
            row.append(" ")
        else:
            row.append("*")
    board.append(row)

# piton elhelyezése a pályán
board[snake_y][snake_x] = "@"

# pálya felirása
def draw_board():
    for row in board:
        print("".join(row))
    print("Hova?")

# mozgatás
def move_snake(direction):
    global snake_x, snake_y

    # előző pozició törlése
    board[snake_y][snake_x] = " "

    if direction == "balra":
        snake_x -= 1
    elif direction == "jobbra":
        snake_x += 1
    elif direction == "fel":
        snake_y -= 1
    elif direction == "le":
        snake_y += 1

    # Ellenőrzés, hogy a piton hozzáért-e a kerítéshez
    if board[snake_y][snake_x] == "*":
        print("A piton hozzáért a kerítéshez! Játék vége.")
        print("Most ennyi volt, szép napot!")
        exit()

    # Piton új pozíciójának beállítása
    board[snake_y][snake_x] = "@"

# játék főciklusa
while True:
    draw_board()
    command = input().lower()

    if command == "meguntam":
        print("Most ennyi volt, szép napot!")
        break

    if command in ["balra", "jobbra", "fel", "le"]:
        move_snake(command)
    else:
        print("Nem értem a parancsot. Próbáld újra!")