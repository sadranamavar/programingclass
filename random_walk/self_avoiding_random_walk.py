import random
from colorama import Fore
import os
import time


dog_walk_log = []
free_block = "."
# dog_char = "🐕"
dog_char = "*"


def print_end(END):
    print("----> end game <----", end="\n\n")
    if END:
        print("exit success", end="\n\n")
    else:
        print("exit failed", end="\n\n")
    print(f"||total move is {len(dog_walk_log)}||")
    exit()


def city_printer(x):
    print(Fore.CYAN+" ██"*(len(x)+1))

    for i in range(len(x)):
        print(end='   ')
        for j in range(len(x)):

            if [[i, j], [i, j+1]] in dog_walk_log or [[i, j+1], [i, j]] in dog_walk_log:
                print(Fore.RESET+x[i][j], end=Fore.RED+"██")
                flag = 1
            else:
                print(Fore.RESET+x[i][j], end="  ")
        print(end="\n"+Fore.CYAN+" ██")
        for k in range(len(x)):
            if [[i, k], [i+1, k]] in dog_walk_log or [[i+1, k], [i, k]] in dog_walk_log:
                print(Fore.RED+"█"+Fore.CYAN+"██", end='')
            else:
                print(Fore.CYAN+" ██", end='')
        print()


def get_dog_location(city):
    for i in range(len(city)):
        for j in range(len(city)):
            if city[i][j] == dog_char:
                return [i, j]


def get_free_move(city):
    free_move = []
    dog_location = get_dog_location(city)
    try:
        if city[dog_location[0]][dog_location[1]+1] == free_block:
            free_move.append([dog_location[0], dog_location[1]+1])
    except:
        print_end(True)
    try:
        if city[dog_location[0]][dog_location[1]-1] == free_block:
            free_move.append([dog_location[0], dog_location[1]-1])
    except:
        pass
    try:
        if city[dog_location[0]+1][dog_location[1]] == free_block:
            free_move.append([dog_location[0]+1, dog_location[1]])
    except:
        print_end(True)
    try:
        if city[dog_location[0]-1][dog_location[1]] == free_block:
            free_move.append([dog_location[0]-1, dog_location[1]])
    except:
        pass
    if not free_move:
        print_end(False)
    for i in free_move:
        if -1 in i:
            print_end(True)
    return free_move


def dog_walk(city):
    free_move = get_free_move(city)
    dog_location = get_dog_location(city)
    move = free_move[random.randrange(len(free_move))]
    dog_walk_log.append([dog_location, move])
    city[dog_location[0]][dog_location[1]] = Fore.RED+"█"
    city[move[0]][move[1]] = dog_char


def make_city(x):
    city = []
    for i in range(x):
        city.append([])
        for j in range(x):
            city[i].append(free_block)
    city[len(city)//2][len(city)//2] = dog_char

    return city


city = make_city(13)

while True:
    dog_walk(city)
    print("\n\n")
    os.system("clear")
    city_printer(city)
    time.sleep(.5)

