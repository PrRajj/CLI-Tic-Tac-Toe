from rich import print

def print_grid(grid):
    print(grid[0], grid[1], grid[2], grid[3], grid[4])

def check_win():
    if grid[0] == "X" and grid[2] == "X" and grid[4] == "X":
        print(f"[bold green]X[/bold green] | [bold green]X[/bold green] | [bold green]X[/bold green]")
        print("---------")
        print_grid(grid2)
        print("---------")
        print_grid(grid3)
        print("X Wins")
        return True
    elif grid2[0] == "X" and grid2[2] == "X" and grid2[4] == "X":
        print_grid(grid)
        print("---------")
        print(f"[bold green]X[/bold green] | [bold green]X[/bold green] | [bold green]X[/bold green]")
        print("---------")
        print_grid(grid3)
        print("X Wins")
        return True
    elif grid3[0] == "X" and grid3[2] == "X" and grid3[4] == "X":
        print_grid(grid)
        print("---------")
        print_grid(grid2)
        print("---------")
        print(f"[bold green]X[/bold green] | [bold green]X[/bold green] | [bold green]X[/bold green]")
        print("X Wins")
        return True
    elif grid[0] == "X" and grid2[0] == "X" and grid3[0] == "X":
        print(f"[bold green]X[/bold green] | {grid[2]} | {grid[4]}")
        print("---------")
        print(f"[bold green]X[/bold green] | {grid2[2]} | {grid2[4]}")
        print("---------")
        print(f"[bold green]X[/bold green] | {grid3[2]} | {grid3[4]}")
        print("X Wins")
        return True
    elif grid[2] == "X" and grid2[2] == "X" and grid3[2] == "X":
        print(f"{grid[0]} | [bold green]X[/bold green] | {grid[4]}")
        print("---------")
        print(f"{grid2[0]} | [bold green]X[/bold green] | {grid2[4]}")
        print("---------")
        print(f"{grid3[0]} | [bold green]X[/bold green] | {grid3[4]}")
        print("X Wins")
        return True
    elif grid[4] == "X" and grid2[4] == "X" and grid3[4] == "X":
        print(f"{grid[0]} | {grid[2]} | [bold green]X[/bold green]")
        print("---------")
        print(f"{grid2[0]} | {grid2[2]} | [bold green]X[/bold green]")
        print("---------")
        print(f"{grid3[0]} | {grid3[2]} | [bold green]X[/bold green]")
        print("X Wins")
        return True
    elif grid[0] == "X" and grid2[2] == "X" and grid3[4] == "X":
        print(f"[bold green]X[/bold green] | {grid[2]} | {grid[4]}")
        print("---------")
        print(f"{grid2[0]} | [bold green]X[/bold green] | {grid2[4]}")
        print("---------")
        print(f"{grid3[0]} | {grid3[2]} | [bold green]X[/bold green]")
        print("X Wins")
        return True
    elif grid[4] == "X" and grid2[2] == "X" and grid3[0] == "X":
        print(f"{grid[0]} | {grid[2]} | [bold green]X[/bold green]")
        print("---------")
        print(f"{grid2[0]} | [bold green]X[/bold green] | {grid2[4]}")
        print("---------")
        print(f"[bold green]X[/bold green] | {grid3[2]} | {grid3[4]}")
        print("X Wins")
        return True
    elif grid[0] == "O" and grid[2] == "O" and grid[4] == "O":
        print(f"[bold green]O[/bold green] | [bold green]O[/bold green] | [bold green]O[/bold green]")
        print("---------")
        print_grid(grid2)
        print("---------")
        print_grid(grid3)
        print("O Wins")
        return True
    elif grid2[0] == "O" and grid2[2] == "O" and grid2[4] == "O":
        print_grid(grid)
        print("---------")
        print(f"[bold green]O[/bold green] | [bold green]O[/bold green] | [bold green]O[/bold green]")
        print("---------")
        print_grid(grid3)
        print("O Wins")
        return True
    elif grid3[0] == "O" and grid3[2] == "O" and grid3[4] == "O":
        print_grid(grid)
        print("---------")
        print_grid(grid2)
        print("---------")
        print(f"[bold green]O[/bold green] | [bold green]O[/bold green] | [bold green]O[/bold green]")
        print("O Wins")
        return True
    elif grid[0] == "O" and grid2[0] == "O" and grid3[0] == "O":
        print(f"[bold green]O[/bold green] | {grid[2]} | {grid[4]}")
        print("---------")
        print(f"[bold green]O[/bold green] | {grid2[2]} | {grid2[4]}")
        print("---------")
        print(f"[bold green]O[/bold green] | {grid3[2]} | {grid3[4]}")
        print("O Wins")
        return True
    elif grid[2] == "O" and grid2[2] == "O" and grid3[2] == "O":
        print(f"{grid[0]} | [bold green]O[/bold green] | {grid[4]}")
        print("---------")
        print(f"{grid2[0]} | [bold green]O[/bold green] | {grid2[4]}")
        print("---------")
        print(f"{grid3[0]} | [bold green]O[/bold green] | {grid3[4]}")
        print("O Wins")
        return True
    elif grid[4] == "O" and grid2[4] == "O" and grid3[4] == "O":
        print(f"{grid[0]} | {grid[2]} | [bold green]O[/bold green]")
        print("---------")
        print(f"{grid2[0]} | {grid2[2]} | [bold green]O[/bold green]")
        print("---------")
        print(f"{grid3[0]} | {grid3[2]} | [bold green]O[/bold green]")
        print("O Wins")
        return True
    elif grid[0] == "O" and grid2[2] == "O" and grid3[4] == "O":
        print(f"[bold green]O[/bold green] | {grid[2]} | {grid[4]}")
        print("---------")
        print(f"{grid2[0]} | [bold green]O[/bold green] | {grid2[4]}")
        print("---------")
        print(f"{grid3[0]} | {grid3[2]} | [bold green]O[/bold green]")
        print("O Wins")
        return True
    elif grid[4] == "O" and grid2[2] == "O" and grid3[0] == "O":
        print(f"{grid[0]} | {grid[2]} | [bold green]O[/bold green]")
        print("---------")
        print(f"{grid2[0]} | [bold green]O[/bold green] | {grid2[4]}")
        print("---------")
        print(f"[bold green]O[/bold green] | {grid3[2]} | {grid3[4]}")
        print("O Wins")
        return True
    else:
        return False

grid = ["1", "|", "2", "|", "3"]
grid2 = ["4", "|", "5", "|", "6"]
grid3 = ["7", "|", "8", "|", "9"]

turn = "X"
chance = True
lt  = []
while True:
    print()
    over = check_win()
    if over == True:
        break
    print(f"{turn} Turn")
    print_grid(grid)
    print("---------")
    print_grid(grid2)
    print("---------")
    print_grid(grid3)
    pos = int(input("Enter the position: "))
    if pos not in lt:
        pass
    else:
        print("Position Already Occupied!")
        continue
    lt.append(pos)
    if pos in range(1, 4):
        if pos == 1:
            if chance == True:
                grid[0] = "X"
                chance = False
                turn = "O"
            else:
                grid[0] = "O"
                chance = True
                turn = "X"
        elif pos == 2:
            if chance == True:
                grid[2] = "X"
                chance = False
                turn = "O"
            else:
                grid[2] = "O"
                chance = True
                turn = "X"
        elif pos == 3:
            if chance == True:
                grid[4] = "X"
                chance = False
                turn = "O"
            else:
                grid[4] = "O"
                chance = True
                turn = "X"
    elif pos in range(4, 7):
        if pos == 4:
            if chance == True:
                grid2[0] = "X"
                chance = False
                turn = "O"
            else:
                grid2[0] = "O"
                chance = True
                turn = "X"
        elif pos == 5:
            if chance == True:
                grid2[2] = "X"
                chance = False
                turn = "O"
            else:
                grid2[2] = "O"
                chance = True
                turn = "X"
        elif pos == 6:
            if chance == True:
                grid2[4] = "X"
                chance = False
                turn = "O"
            else:
                grid2[4] = "O"
                chance = True
                turn = "X"
    elif pos in range(7, 10):
        if pos == 7:
            if chance == True:
                grid3[0] = "X"
                chance = False
                turn = "O"
            else:
                grid3[0] = "O"
                chance = True
                turn = "X"
        elif pos == 8:
            if chance == True:
                grid3[2] = "X"
                chance = False
                turn = "O"
            else:
                grid3[2] = "O"
                chance = True
                turn = "X"
        elif pos == 9:
            if chance == True:
                grid3[4] = "X"
                chance = False
                turn = "O"
            else:
                grid3[4] = "O"
                chance = True
                turn = "X"
    else:
        print("INVALID!")
