def print_board(xstate,ostate):
    zero="X" if xstate[0] else ("O" if ostate[0] else 0)
    one="X" if xstate[1] else ("O" if ostate[1] else 1)
    two="X" if xstate[2] else ("O" if ostate[2] else 2)
    three="X" if xstate[3] else ("O" if ostate[3] else 3)
    four="X" if xstate[4] else ("O" if ostate[4] else 4)
    five="X" if xstate[5] else ("O" if ostate[5] else 5)
    six="X" if xstate[6] else ("O" if ostate[6] else 6)
    seven="X" if xstate[7] else ("O" if ostate[7] else 7)
    eight="X" if xstate[8] else ("O" if ostate[8] else 8)
    print(f" {zero} | {one} | {two}")
    print(f" {three} | {four} | {five}")
    print(f" {six} | {seven} | {eight}")
def Sum(a,b,c):
    return a+b+c
def Win(xstate,ostate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(Sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("Hurrayh x Won the Game!!")
            return 0
        elif(Sum(ostate[win[0]],ostate[win[1]],ostate[win[2]])==3):
            print("Hurrayh x Won the Game!!")
            return 1
    return -1
if __name__=="__main__":
    print("Welcome To Tic Tac Toe Game!!")
    xstate=[0,0,0,0,0,0,0,0,0]
    ostate=[0,0,0,0,0,0,0,0,0]
    turn=1
    while(True):
        print_board(xstate,ostate)
        if turn==1:
            print("Chance of 'X':")
            value=int(input())
            xstate[value]=1
        else:
            print("Chance of 'O':")
            value=int(input())
            ostate[value]=1
        cwin=Win(xstate,ostate)
        if cwin!=-1:
            print("Match Over")
            break
        turn=1-turn

# Welcome To Tic Tac Toe Game!!
#  0 | 1 | 2
#  3 | 4 | 5
#  6 | 7 | 8
# Chance of 'X':
# 1
#  0 | X | 2
#  3 | 4 | 5
#  6 | 7 | 8
# Chance of 'O':
# 0
#  O | X | 2
#  3 | 4 | 5
#  6 | 7 | 8
# Chance of 'X':
# 4
#  O | X | 2
#  3 | X | 5
#  6 | 7 | 8
# Chance of 'O':
# 5
#  O | X | 2
#  3 | X | O
#  6 | 7 | 8
# Chance of 'X':
# 7
# Hurrayh x Won the Game!!
# Match Over
