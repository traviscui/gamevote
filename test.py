x = 0
y = 0
z = 0

number = input("How many people are playing?")

number_int = int(number)
run = 1
run_int = int(run)

while (run_int <= number_int):
    game = input("enter a game name(cod, r6 or starb):")
    game_str = str(game)
    
    if game_str == "cod":
        x = x + 1
        run_int = run_int + 1
    elif game_str == "r6":
        y = y + 1
        run_int = run_int + 1
    elif game_str == "starb":
        z = z + 1
        run_int = run_int + 1
    else:
        print("You entered wrong game")

print("cod votes:", x,"r6 votes:", y,"starb votes:",z)