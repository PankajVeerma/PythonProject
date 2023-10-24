def add(a, b, c):
    return a + b + c


def Board(xstate, zstate):
    R0 = "x" if xstate[0] else ("0" if zstate[0] else 0)
    R1 = "x" if xstate[1] else ("0" if zstate[1] else 1)
    R2 = "x" if xstate[2] else ("0" if zstate[2] else 2)
    R3 = "x" if xstate[3] else ("0" if zstate[3] else 3)
    R4 = "x" if xstate[4] else ("0" if zstate[4] else 4)
    R5 = "x" if xstate[5] else ("0" if zstate[5] else 5)
    R6 = "x" if xstate[6] else ("0" if zstate[6] else 6)
    R7 = "x" if xstate[7] else ("0" if zstate[7] else 7)
    R8 = "x" if xstate[8] else ("0" if zstate[8] else 8)
    print(f"{R0} | {R1} | {R2} ")
    print(f"--|---|---")
    print(f"{R3} | {R4} | {R5} ")
    print(f"--|---|---")
    print(f"{R6} | {R7} | {R8} ")


def check(xstate, zstate):
    wons = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for won in wons:
        if add(xstate[won[0]], xstate[won[1]], xstate[won[2]]) == 3:
            print("X won the the game")
            return 1
        if add(zstate[won[0]], zstate[won[1]], zstate[won[2]]) == 3:
            print("Z won the the game")
            return 0
    return -1


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    chance = 1
    print("Wellcome to Tic Tac Toe")

    while True:
        Board(xstate, zstate)
        if chance == 1:
            print("x's chance")
            num = int(input("Enter the number"))
            xstate[num] = 1
        else:
            print("0's chance")
            num = int(input("Enter the number"))
            xstate[num] = 1
        chwon = check(xstate, zstate)
        if chwon != -1:
            print("Game Over")
            break
        chance = 1 - chance
