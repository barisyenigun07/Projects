import numpy as np
arr = np.array(["_","_","_","_","_","_","_","_","_"])
def parseGame(arr):
    arr = arr.reshape(3,3)
    return arr
def changeTurn(turn):
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    return turn
def turnOfX(arr,x,y):
    if arr[x][y] == "_":
        arr[x][y] = "X"
    else:
        print("Error!")
    return arr
def turnOfO(arr,x,y):
    if arr[x][y] == "_":
        arr[x][y] = "O"
    else:
        print("Error!")
    return arr
def checkRow(arr):
    case1 = arr[0][0] == arr[0][1] == arr[0][2] == "X"
    case2 = arr[1][0] == arr[1][1] == arr[1][2] == "X"
    case3 = arr[2][0] == arr[2][1] == arr[2][2] == "X"
    case4 = arr[0][0] == arr[0][1] == arr[0][2] == "O"
    case5 = arr[0][0] == arr[0][1] == arr[0][2] == "O"
    case6 = arr[0][0] == arr[0][1] == arr[0][2] == "O"
    if case1 or case2 or case3:
        print("X wins!!!")
        return True
    elif case4 or case5 or case6:
        print("O wins!!!")
        return True
def checkCol(arr):
    case1 = arr[0][0] == arr[1][0] == arr[2][0] == "X"
    case2 = arr[0][1] == arr[1][1] == arr[2][1] == "X"
    case3 = arr[0][2] == arr[1][2] == arr[2][2] == "X"
    case4 = arr[0][0] == arr[1][0] == arr[2][0] == "O"
    case5 = arr[0][1] == arr[1][1] == arr[2][1] == "O"
    case6 = arr[0][2] == arr[1][2] == arr[2][2] == "O"
    if case1 or case2 or case3:
        print("X wins!!!")
        return True
    elif case4 or case5 or case6:
        print("O wins!!!")
        return True
def checkCross(arr):
    case1 = arr[0][0] == arr[1][1] == arr[2][2] == "X"
    case2 = arr[0][2] == arr[1][1] == arr[2][0] == "X"
    case3 = arr[0][0] == arr[1][1] == arr[2][2] == "O"
    case4 = arr[0][2] == arr[1][1] == arr[2][0] == "O"
    if case1 or case2:
        print("X wins!!!")
        return True
    elif case3 or case4:
        print("O wins!!!")
        return True
game = parseGame(arr)
print(game)
turn = "X"
coor = [int(x) for x in input("Enter coordinates seperated by space:").split()]
x = coor[0]
y = coor[1]
upgame = turnOfX(game,x,y)
print(upgame)
turn = changeTurn(turn)
while True:
    coor = [int(x) for x in input("Enter coordinates seperated by space:").split()]
    x = coor[0]
    y = coor[1]
    if turn == "X":
        up_game1 = (turnOfX(upgame, x, y))
        print(up_game1)
        if checkRow(up_game1) or checkCol(up_game1) or checkCross(up_game1):
            break
        else:
            if "_" not in up_game1:
                print("Draw!!!")
                break
        turn = changeTurn(turn)
    else:
        up_game1 = (turnOfO(upgame, x, y))
        print(up_game1)
        if checkRow(up_game1) or checkCol(up_game1) or checkCross(up_game1):
           break
        else:
            if "_" not in up_game1:
                print("Draw!!!")
                break
        turn = changeTurn(turn)




