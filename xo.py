# tic-tac-toe
# author : Madhav

import os
import sys
import random
import time

import platform
OS = platform.system().lower()
SYS = "cls" if 'win' in OS else "clear"

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
all_moves = ['11','22','33','12','13','21','23','31','32']
positions = []

def show_board(board):
    os.system(SYS)
    print("+---+---+---+")
    for i in board:
        print("|",end=" ")
        for j in i:
            print(j,end=" | ")
        print("\n+---+---+---+")
    print()

def all_orientations(board):
    a = board.copy()
    temp1 = [board[i][i] for i in range(3)]
    temp2 = [board[i][2-i] for i in range(3)]
    for i in range(3):
        a.append([board[j][i] for j in range(3)])
    a.append(temp1)
    a.append(temp2)
    return a

def insert(x,y):
    return str(x+1)+str(y+1)

def set_value(j,i,arr,brd):
    a = arr(brd).index(i)
    b = i.index(j)
    if a<3: return insert(a%3,b)
    elif 2<a<6: return insert(b,a%3)
    elif a==6: return insert(b,b)
    elif a==7:
        if b==0: return insert(0,2)
        elif b==1: return insert(1,1)
        elif b==2: return insert(2,0)
    else: return

def take_input(player):
    n = input((f"{player} : "))
    if 'exit' in n.lower() or n.lower() == 'q':
        print("\nexitting game...")
        input()
        sys.exit()
    if n in positions or n not in all_moves:
        print("enter valid unoccupied position")
        return take_input(player)
    return int(n)

def play(move,player):
    n = take_input(player)
    positions.append(str(n))
    board[int(n/10 -1)][int(n%10 -1)] = move
    check_score(l:=all_orientations(board),player)

def check_score(l,player):
    show_board(board)
    if ['X', 'X', 'X'] in l: print(f"{player} wins!\n")
    elif ['O', 'O', 'O'] in l: print(f"{player} wins!\n")
    elif "' '" not in str(board): print("Match Drawn!\n")
    else: return
    input()
    sys.exit()

def count(arr,move):
        return(len([i for i in str(arr) if i==move]))

def block():
    for i in all_orientations(board):
        if count(i,"X")==2 and count(i,"O")==0:
            for j in i:
                if j!="X": return set_value(j,i,all_orientations,board)

def win():
    for i in all_orientations(board):
        if count(i,"O")==2 and count(i,"X")==0:
            for j in i:
                if j!="O": return set_value(j,i,all_orientations,board)

def bot_move(arr):
    moves = [i for i in all_moves if i not in arr]
    if win() is not None:
        return win()
    elif block() is not None:
        return block()
    return random.choice(tuple(moves))

def cplay():
    global turn
    turn = True
    win()
    if turn:
        block()
        if turn:
            m = int(bot_move(positions))
            positions.append(str(m))
            board[int(m/10 -1)][int(m%10 -1)] = "O"
            check_score(l:=all_orientations(board),"computer")

def playing():
    temp = "computer playing....."
    for i in range(5):
        show_board(board)
        print(temp[:17+i])
        time.sleep(0.2)

def main():
    os.system(SYS)
    game = input("Select Your Game:\n\n(1) : Player v/s Player\n\n(2) : Player v/s Computer\n\n(type '1' or '2') : ")
    while game not in ['1','2']:
        os.system(SYS)
        try: game = input("Select Your Game:\n\n(1) : Player v/s Player\n\n(2) : Player v/s Computer\n\nplease type '1' or '2' : ")
        except: pass
    os.system(SYS)
    if game == "2":
        move = "X"
        name1 = input("Enter your name : ")
        show_board(board)
        while True:
            play(move,name1)
            playing()
            cplay()
    elif game == "1":
        name1 = input("Enter name of player 1 : ")
        name2 = input("\nEnter name of player 2 : ")
        show_board(board)
        while True:
            play("X",name1)
            play("O",name2)

if __name__ == "__main__":
    main()
