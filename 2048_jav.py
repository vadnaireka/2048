import os
import sys
import random
import shutil
import readchar

FINAL_POINT = 16

def move_down():
    for j in range(0,4):
        for i in range(3, 0, -1):
            if board[i][j] == 0:
                for z in range(1, i + 1):
                    if board[i][j] == 0 and board[i - z][j] != 0:
                        board[i][j] = board[i - z][j]
                        if i - (z + 1) > -1:
                            board[i - z][j] = board[i - (z + 1)][j]
                            if i - (z + 2) > -1:
                                board[i - (z + 1)][j] = board[i - (z + 2)][j]
                                board[i - (z + 2)][j] = 0
                            else:
                                board[i - (z + 1)][j] = 0
                        else:
                            board[i - z][j] = 0
                    else:
                        pass
            if i > 0:
                for z in range(1, i + 1):
                    if board[i][j] == board[i - z][j]:
                        board[i][j] = board[i][j] + board[i - z][j]
                        if i - (z + 1) > -1:
                            board[i - z][j] = board[i - (z + 1)][j]
                            if i - (z + 2) > -1:
                                board[i - (z + 1)][j] = board[i - (z + 2)][j]
                                board[i - (z + 2)][j] = 0
                            else:
                                board[i - (z + 1)][j] = 0
                        else:
                            board[i - z][j] = 0
                    else:
                        pass        

def move_up():
    for j in range(0,4):
        for i in range(0,4):
            if board[i][j] == 0:
                for z in range(1, 4):
                    try:
                        if board[i][j] == 0 and board[i+z][j] != 0:
                            board[i][j] = board[i+z][j]
                            board[i +z][j] = 0
                            board[i +z][j] = board[i +(z+1)][j]
                            board[i + (z+1)][j] =0
                            board[i+(z+1)][j] = board[i+(z+2)][j]
                            board[i +(z+2)][j] = 0
                    except IndexError:
                        pass
            if board[i][j] != 0 and i <3:
                try:
                    if board[i][j] == board[i+1][j]:
                        board[i][j] = board[i][j] + board[i+1][j]
                        board[i+1][j] =0
                        board[i+1][j] = board[i+2][j]
                        board[i+2][j ] =0
                        board[i+2][j] = board[i+3][j ]
                        board[i+3][j] = 0
                    if board[i+1][j] == 0:
                        if board[i][j] == board[i+2][j]:
                            board[i][j] = board[i][j] + board[i+2][j]
                            board[i+2][j] = 0
                            board[i+1][j] = board[i+3][j]
                            board[i+3][j] = 0
                        if board[i + 2][j] == 0:
                            if board[i][j] == board[i + 3][j]:
                                board[i][j] = board[i][j] + board[i+3][j]
                                board[i][j + 3] = 0         
                except IndexError:
                    pass

def move_left():
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == 0:
                for z in range(1, 4):
                    try:
                        if board[i][j] == 0 and board[i][j+z] != 0:
                            board[i][j] = board[i][j+z]
                            board[i][j+z] = 0
                            board[i][j+z] = board[i][j +(z+1)]
                            board[i][j +(z+1)] =0
                            board[i][j +(z+1)] = board[i][j +(z+2)]
                            board[i][j +(z+2)] = 0
                    except IndexError:
                        pass
            if j <3 and board[i][j] != 0:
                #for z in range(1, 3 - j):
                try:
                    if board[i][j] == board[i][j + 1]:
                        board[i][j] = board[i][j] + board[i][j + 1]
                        board[i][j + 1] =0
                        board[i][j + 1] = board[i][j + 2]
                        board[i][j + 2] =0
                        board[i][j + 2] = board[i][j + 3]
                        board[i][j + 3] = 0
                    if board[i][j + 1] == 0:
                        if board[i][j] == board[i][j + 2]:
                            board[i][j] = board[i][j] + board[i][j + 2]
                            board[i][j + 2] = 0
                            board[i][j + 1] = board[i][j + 3]
                            board[i][j + 3] = 0
                        elif board[i][j] == board[i][j + 3]:
                            board[i][j] = board[i][j] + board[i][j + 3]
                            board[i][j + 3] = 0
                except IndexError:
                    pass  

def move_right():
    for i in range(0,4):
        for j in range(3, -1, -1):
            if board[i][j] == 0:
                for z in range(1, j + 1):
                    if board[i][j] == 0 and board[i][j-z] != 0:
                        board[i][j] = board[i][j-z]
                        if j - (z + 1) > -1:
                            board[i][j - z] = board[i][j - (z + 1)]
                            if j - (z + 2) > -1:
                                board[i][j - (z + 1)] = board[i ][j- (z + 2)]
                                board[i][j - (z + 2)] = 0
                            else:
                                board[i][j - (z + 1)] = 0
                        else:
                            board[i][j - z] = 0
                    else:
                        pass
            if j > 0:
                for z in range(1, j + 1):
                    if board[i][j] == board[i][j - z]:
                        board[i][j] = board[i][j] + board[i][j - z]
                        if j - (z + 1) > -1:
                            board[i][j- z] = board[i][j - (z + 1)]
                            if j - (z + 2) > -1:
                                board[i][j - (z + 1)] = board[i][j - (z + 2)]
                                board[i][j - (z + 2)] = 0
                            else:
                                board[i][j - (z + 1)] = 0
                        else:
                            board[i][j - z] = 0
                    else:
                        pass          

def set_new_cell():
    x = True
    c = board[0].count(0) + board[1].count(0) + board[2].count(0) + board[3].count(0)
    if c == 0:
        x=False
    while x:
        new = [2,4,2,2]
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] == 0:
            board[i][j] = random.choice(new)
            x = False
        
def export_list(filename, table):
    table_str = ""
    for line in table:
        for i in range(len(line)):
            line[i] = str(line[i])
        line_str = ''.join(line)
        table_str += line_str + ','
    with open(filename, 'w') as f:
        f.write(table_str[:-1])

def import_list(filename):
    board = []
    with open(filename , 'r') as f:
        x = f.read()
        x = str(x)
        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []
        for i in range(0,4):
            lista1.append(int(x[i]))
        for i in range(5,9):
            lista2.append(int(x[i]))
        for i in range(10,14):
            lista3.append(int(x[i]))
        for i in range(15,19):
            lista4.append(int(x[i]))
        board = [lista1, lista2, lista3, lista4]

def menu():
    columns= shutil.get_terminal_size().columns
    print(" __  __           _             __  __                        ".center(columns))                  
    print("|  \/  |   __ _  (_)  _ __     |  \/  |   ___   _ __    _   _ ".center(columns))
    print("| |\/| |  / _` | | | | '_ \    | |\/| |  / _ \ | '_ \  | | | |".center(columns))
    print("| |  | | | (_| | | | | | | |   | |  | | |  __/ | | | | | |_| |".center(columns))
    print("|_|  |_|  \__,_| |_| |_| |_|   |_|  |_|  \___| |_| |_|  \__,_|".center(columns))
    print("______________________________________________________________".center(columns))
    print("")
    print(' ____             ____              ____       '.center(columns))
    print('||1 ||           ||2 ||            ||3 ||      '.center(columns))
    print('||__|| New Game  ||__|| Load Game  ||__|| Quit '.center(columns))
    print('|/__\|           |/__\|            |/__\|      '.center(columns))

    
    
    
    
    #print(("1. New Game"+"       "+"2. Load Game"+"       "+"3. Quit").center(columns))
    #print("2. Load Game".center(columns))
    #print("3. Quit ".center(columns))

sp = '        '
t_2048_top = ('\x1b[1;31;40m''\u250f''\u2513'   '\u250f''\u2513'  '\u257b'' '   '\u250f''\u2513''\x1b[0m')
t_2048_mid = ('\x1b[1;31;40m''\u250f''\u251b'   '\u2503''\u2503'  '\u2517''\u252b' '\u2523''\u252b''\x1b[0m')
t_2048_down = ('\x1b[1;31;40m''\u2517''\u251b'  '\u2517' '\u251b' ' ' '\u2579'     '\u2517' '\u251b''\x1b[0m')
t_2048=[t_2048_top,t_2048_mid,t_2048_down]
t_1024_top = ('\x1b[1;34;41m'' ''\u257b'  '\u250f''\u2513'  '\u250f''\u2513'  '\u257b'' ''\x1b[0m')
t_1024_mid = ('\x1b[1;34;41m'' ''\u2503'  '\u2503''\u2503'  '\u250f''\u251b'  '\u2517''\u252b''\x1b[0m')
t_1024_down = ('\x1b[1;34;41m'' ' '\u2579' '\u2517' '\u251b' '\u2517' '\u251b' ' ' '\u2579''\x1b[0m')
t_1024=[t_1024_top,t_1024_mid,t_1024_down]
t_512_top = ('\x1b[1;33;42m''  ''\u250f' '\u2578' '\u257b''\u250f''\u2513'' ''\x1b[0m')
t_512_mid = ('\x1b[1;33;42m''  ''\u2517''\u2513''\u2503''\u250f''\u251b'' ''\x1b[0m')
t_512_down = ('\x1b[1;33;42m''  ' '\u2517' '\u251b' '\u2579' '\u2517' '\u251b' ' ''\x1b[0m')
t_512=[t_512_top,t_512_mid,t_512_down]
t_256_top = ('\x1b[1;32;43m'' ' '\u250f''\u2513''\u250f' '\u2578''\u250f' '\u2578'' ''\x1b[0m')
t_256_mid = ('\x1b[1;32;43m'' ' '\u250f''\u251b''\u2517''\u2513''\u2523''\u2513'' ''\x1b[0m')
t_256_down = ('\x1b[1;32;43m'' ' '\u2517' '\u251b' '\u2517' '\u251b' '\u2517' '\u251b' ' ''\x1b[0m')
t_256=[t_256_top,t_256_mid,t_256_down]
t_128_top = ('\x1b[1;37;46m'' ''\u257b''\u250f''\u2501''\u2513''\u250f''\u2501''\u2513''' '\x1b[0m')
t_128_mid = ('\x1b[1;37;46m'' ''\u2503''\u250f''\u2501''\u251b''\u2523''\u2501''\u252b''' '\x1b[0m')
t_128_down = ('\x1b[1;37;46m'' ' '\u2579' '\u2517' '\u2501''\u251b' '\u2517' '\u2501''\u251b' '' '\x1b[0m')
t_128=[t_128_top,t_128_mid,t_128_down]
t_64_top = ('\x1b[1;30;42m'' ''\u250f''\u2501' '\u2578''\u257b''   ''\x1b[0m')
t_64_mid = ('\x1b[1;30;42m'' ''\u2523''\u2501''\u2513''\u2517''\u2501''\u252b'' ''\x1b[0m')
t_64_down = ('\x1b[1;30;42m'' ''\u2517''\u2501' '\u251b''  ' '\u2579'' ''\x1b[0m')
t_64=[t_64_top,t_64_mid,t_64_down]
t_32_top = ('\x1b[1;33;44m''  ''\u2501''\u2513''\u250f''\u2501''\u2513'' ''\x1b[0m')
t_32_mid = ('\x1b[1;33;44m''  ''\u257a''\u252b''\u250f''\u2501''\u251b' ' ''\x1b[0m')
t_32_down = ('\x1b[1;33;44m''  ' '\u2501' '\u251b' '\u2517' '\u2501' '\u251b' ' ''\x1b[0m')
t_32=[t_32_top,t_32_mid,t_32_down]
t_16_top = ('\x1b[1;32;41m''  ''\u257b''\u250f''\u2501''\u2578''  ''\x1b[0m')
t_16_mid = ('\x1b[1;32;41m''  ''\u2503''\u2523''\u2501''\u2513''  ''\x1b[0m')
t_16_down = ('\x1b[1;32;41m''  ' '\u2579' '\u2517' '\u2501' '\u251b' '  ''\x1b[0m')
t_16=[t_16_top,t_16_mid,t_16_down]
t_8_top = ('\x1b[1;33;45m''   ''\u250f''\u2501''\u2513''  ''\x1b[0m')
t_8_mid = ('\x1b[1;33;45m''   ''\u2523''\u2501''\u252b''  ''\x1b[0m')
t_8_down = ('\x1b[1;33;45m''   ' '\u2517' '\u2501' '\u251b' '  ''\x1b[0m')
t_8=[t_8_top,t_8_mid,t_8_down]
t_4_top = ('\x1b[1;30;46m' '  ' '\u257b''     ''\x1b[0m')
t_4_mid = ('\x1b[1;30;46m''  ''\u2517''\u2501''\u2501''\u252b''  ''\x1b[0m')
t_4_down = ('\x1b[1;30;46m''     ' '\u2579 '' ''\x1b[0m')
t_4=[t_4_top,t_4_mid,t_4_down]
t_2_top = ('\x1b[0;32;47m''  ' '\u250f'    '\u2501' '\u2501' '\u2513' '  ''\x1b[0m')
t_2_mid = ('\x1b[0;32;47m''  ''\u250f'    '\u2501'  '\u2501' '\u251b' '  ''\x1b[0m')
t_2_down = ('\x1b[0;32;47m''  ' '\u2517'   '\u2501'  '\u2501' '\u251b' '  ''\x1b[0m')
t_2 = [t_2_top, t_2_mid, t_2_down]
t_0=[sp,sp,sp]

num = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
num_draw = [t_0, t_2, t_4, t_8, t_16, t_32, t_64, t_128, t_256, t_512, t_1024, t_2048]
cell=[[[sp,sp,sp],[sp,sp,sp],[sp,sp,sp],[sp,sp,sp]],[[sp,sp,sp],[sp,sp,sp],[sp,sp,sp],[sp,sp,sp]],
        [[sp,sp,sp],[sp,sp,sp],[sp,sp,sp],[sp,sp,sp]],[[sp,sp,sp],[sp,sp,sp],[sp,sp,sp],[sp,sp,sp]]]
        
def table():
    for j in range(0, 4):
        for i in range(0, 4):
            for z in range(0,12):
                if board[i][j] == num[z]:
                    for y in range(0, 3):
                        cell[i][j][y] = num_draw[z][y]
    columns= shutil.get_terminal_size().columns
    print(('\u250f'+'\u2501' * 8+'\u2533'+'\u2501' * 8+'\u2533'+'\u2501' * 8+'\u2533'+'\u2501' * 8+'\u2513').center(columns))
    print(('\u2503'+cell[0][0][0]+'\u2503'+cell[0][1][0]+'\u2503'+cell[0][2][0]+'\u2503'+cell[0][3][0]+'\u2503').center(columns))
    print(('\u2503'+cell[0][0][1]+'\u2503'+cell[0][1][1]+'\u2503'+cell[0][2][1]+'\u2503'+cell[0][3][1]+'\u2503').center(columns))
    print(('\u2503'+cell[0][0][2]+'\u2503'+cell[0][1][2]+'\u2503'+cell[0][2][2]+'\u2503'+cell[0][3][2]+'\u2503').center(columns))
    print(('\u2523'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u252b').center(columns))
    print(('\u2503'+cell[1][0][0]+'\u2503'+cell[1][1][0]+'\u2503'+cell[1][2][0]+'\u2503'+cell[1][3][0]+'\u2503').center(columns))
    print(('\u2503'+cell[1][0][1]+'\u2503'+cell[1][1][1]+'\u2503'+cell[1][2][1]+'\u2503'+cell[1][3][1]+'\u2503').center(columns))
    print(('\u2503'+cell[1][0][2]+'\u2503'+cell[1][1][2]+'\u2503'+cell[1][2][2]+'\u2503'+cell[1][3][2]+'\u2503').center(columns))
    print(('\u2523'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u252b').center(columns))
    print(('\u2503'+cell[2][0][0]+'\u2503'+cell[2][1][0]+'\u2503'+cell[2][2][0]+'\u2503'+cell[2][3][0]+'\u2503').center(columns))
    print(('\u2503'+cell[2][0][1]+'\u2503'+cell[2][1][1]+'\u2503'+cell[2][2][1]+'\u2503'+cell[2][3][1]+'\u2503').center(columns))
    print(('\u2503'+cell[2][0][2]+'\u2503'+cell[2][1][2]+'\u2503'+cell[2][2][2]+'\u2503'+cell[2][3][2]+'\u2503').center(columns))
    print(('\u2523'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u254b'+'\u2501' * 8+'\u252b').center(columns))
    print(('\u2503'+cell[3][0][0]+'\u2503'+cell[3][1][0]+'\u2503'+cell[3][2][0]+'\u2503'+cell[3][3][0]+'\u2503').center(columns))
    print(('\u2503'+cell[3][0][1]+'\u2503'+cell[3][1][1]+'\u2503'+cell[3][2][1]+'\u2503'+cell[3][3][1]+'\u2503').center(columns))
    print(('\u2503'+cell[3][0][2]+'\u2503'+cell[3][1][2]+'\u2503'+cell[3][2][2]+'\u2503'+cell[3][3][2]+'\u2503').center(columns))
    print(('\u2517'+'\u2501' * 8+'\u253b'+'\u2501' * 8+'\u253b'+'\u2501' * 8+'\u253b'+'\u2501' * 8+'\u251b').center(columns))

def logo():
    columns= shutil.get_terminal_size().columns
    print('\033[94m'+".d888b.  .d88b.    j88D  .d888b. ".center(columns))
    print("VP  `8D .8P  88.  j8~88  88   8D ".center(columns))
    print("   odD' 88  d'88 j8' 88  `VoooY' ".center(columns))
    print(" .88'   88 d' 88 V88888D .d~~~b. ".center(columns))
    print("j88.    `88  d8'     88  88   8D ".center(columns))
    print("888888D  `Y88P'      VP  `Y888P' ".center(columns)+ '\033[0m')
    print('\n')

os.system('clear')
columns= shutil.get_terminal_size().columns
logo()
#newgame = input('Would you like to start a new game? Y/N  ')
menu()
print('\n')
print('Please choose an option.'.center(columns))
menu_choice = readchar.readkey()


while True:
    if menu_choice=='1':
        board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif menu_choice == '2':
        board = []
        with open('export_game.csv' , 'r') as f:
            x = f.read()
            x = str(x)
            lista1 = []
            lista2 = []
            lista3 = []
            lista4 = []
            for i in range(0,4):
                lista1.append(int(x[i]))
            for i in range(5,9):
                lista2.append(int(x[i]))
            for i in range(10,14):
                lista3.append(int(x[i]))
            for i in range(15,19):
                lista4.append(int(x[i]))
            board = [lista1, lista2, lista3, lista4]
    while (board[0].count(FINAL_POINT) + board[1].count(FINAL_POINT) + board[2].count(FINAL_POINT)+ board[3].count(FINAL_POINT) < 1):
        os.system('clear')
        set_new_cell()
        logo()
        table()
        answer = False
        while answer == False:
            print("  ____".center(columns))  
            print("            ||\033[91mW \033[0m||".center(columns))
            print("  ||__||".center(columns))
            print("   ____ |/__\| ____".center(columns))
            print("                             ||\033[91mA \033[0m||||\033[91mS \033[0m||||\033[91mD \033[0m||".center(columns))
            print("   ||__||||__||||__||".center(columns))
            print("       Press |/__\||/__\||/__\| to move: ".center(columns))
            press = readchar.readkey()
            if press == '':
                os.system('clear')
                logo()
                table()
            elif press in 'aAsSdDwWpP':
                answer = True
            else:
                os.system('clear')
                logo()
                table()
        if press == 'a' or press == 'A':
            move_left()
        if press == 's' or press == 'S':
            move_down()
        if press == 'd' or press == 'D':
            move_right()
        if press == 'w' or press == 'W':
            move_up()
        if press == 'p' or press =='P':
            export_list('export_game.csv',board)
        os.system('clear')
        logo()
        table()
        c = board[0].count(0) + board[1].count(0) + board[2].count(0) + board[3].count(0)
        if c == 0:
            move=0
            for i in range(0,4):
                for j in range(0,4):
                    try:
                        if i > 0 and j>0:
                            if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j] or board[i][j] == board[i][j - 1] or board[i][j] == board[i][j+1]:
                                move += 1
                        elif i == 0 and j>0:
                            if board[i][j] == board[i][j - 1] or board[i][j] == board[i][j+1]:                                             
                                move += 1
                        elif j == 0 and i > 0:
                            if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j]:
                                move += 1
                    except IndexError:
                        pass
            if move == 0:
                break
    if (board[0].count(FINAL_POINT) + board[1].count(FINAL_POINT) 
            + board[2].count(FINAL_POINT) + board[3].count(FINAL_POINT) > 0):
        print('Congratulations! You won.')
    else:
        print('You lost.')            
    #newgame = input('Would you like to start a new game? Y/N ')
    #if newgame == "Y" or newgame == "y":
    #    continue
    #if newgame == "N" or newgame == "n":
    #    os.system('clear')
    #    break
    #else:
    #    pass