# =========================================================================
# ( BattleShip ):
# (Developed By): -> Otis R. Jackson IV
# =========================================================================
# ( Program Modules )
import random

# ( Global Attributes )
single_player = False
p1_board, cpu_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
p1_board_display, cpu_board_display = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']], [
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
player1_f, cpu_f = False, False
player_1_health, cpu_health = 5, 5
game_start = True
game_symbols = ['X', '-', '#']
turn_array = ['Heads', 'Tails']
coin_flip = random.randint(0, 1)
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ships = ['Aircraft Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
ships_spaces = [5, 4, 3, 3, 2]
p1_ship_coordinates = [[], [], [], [], []]
cpu_ship_coordinates = [[], [], [], [], []]
p1_ships = [p1_ship_coordinates[0],
            p1_ship_coordinates[1],
            p1_ship_coordinates[2],
            p1_ship_coordinates[3],
            p1_ship_coordinates[4]]
cpu_ships = [cpu_ship_coordinates[0],
             cpu_ship_coordinates[1],
             cpu_ship_coordinates[2],
             cpu_ship_coordinates[3],
             cpu_ship_coordinates[4]]

# -> ( Game Functions )
# ( Who goes first function ( Heads or Tails ) )
def first_play(player1_f, cpu_f):
    user_guess = input('\n[Player 1] Pick / Type Heads or Tails: \t')
    if user_guess == turn_array[coin_flip]:
        player1_f = True
        print('\nPlayer 1 Goes First !!\n')
    else:
        cpu_f = True
        print('\nCPU Player Goes First !!\n')
    return [player1_f, cpu_f]

# ( Board Display ( Pass in the Board ) )
def board_display(x):
    # Iterate through x and display 2D list contents
    tracker = 0
    letter_tracker = 0
    print('\t 0\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9')
    for row in x:
        print(letters[letter_tracker], end=': | ')
        letter_tracker += 1
        for element in row:
            if tracker == 10:
                print(element, end=' | ')
                tracker -= 10
            else:
                print(element, end=' | ')
                tracker += 1
        print()

# ( Lose Check / Board Check )
def reroll():
    print('reroll')

print('==================================================' * 2)
print('Welcome To BattleShip')
print('Developed by : Otis Ray Jackson IV')

# ( Display Ruleset )
print('--------------------------------------------------' * 2)
print('( Basic Ruleset of BattleShip )')
print('--------------------------------------------------' * 2)
print('100% Indexed && Turn Based application.\t\t\t\t\t\t ** ( Indexes start from A-J & 0-9 ) **')
print('Select Box Example : => \t\t\t\t\t\t\t\t\t A 9\t [Row, Column]')
print('Hit Box Example : => \t\t\t\t\t\t\t\t\t\t X\t\t at [Row, Column]')
print('Miss Box Example : => \t\t\t\t\t\t\t\t\t\t -\t\t at [Row, Column]\n')


# ( Single Player: [player-1 vs cpu_player] Game Loop )
if single_player:
    # ( Determine Who Goes First )
    first_list = first_play(player1_f, cpu_f)

    # ( Display Board )
    print('--------------------------------------------------')
    print('( Board Display )')
    print('--------------------------------------------------')
    board_display(p1_board_display)
    print('--------------------------------------------------')

    while game_start:
        # ( Game Start )
        ship_counter = 0        # for indexes of ships = [Aircraft Carrier, ....]
        ship_space_counter = 0  # for indexes of ships_spaces = [5, 4, 3, 3, 2]

        # ( Break Conditions )
        if player_1_health <= 0:
            break
        elif cpu_health <= 0:
            break

        # ( Place Coordinates ( Player_1 && CPU ) )
        for i in range(5):
            # ( CPU Direction )
            direct_arr = ['horizontal', 'vertical']
            direction = direct_arr[random.randint(0, 1)]

            # ( CPU Location )
            cpu_row = random.randint(0, 9)
            cpu_column = random.randint(0, 9)

            if cpu_board[cpu_row].count(1) >= 1:
                cpu_row = random.randint(0, 9)
                cpu_column = random.randint(0, 9)
            if direction == 'vertical' and cpu_row >= 5:
                if cpu_board[cpu_row - 1][cpu_column] == 1 or cpu_board[cpu_row - 2][cpu_column] == 1:
                    # ( reroll )
                    cpu_row = random.randint(0, 9)
                    cpu_column = random.randint(0, 9)
            if direction == 'vertical' and cpu_row < 5:
                if cpu_board[cpu_row + 1][cpu_column] == 1 or cpu_board[cpu_row + 2][cpu_column] == 1:
                    # ( reroll )
                    cpu_row = random.randint(0, 9)
                    cpu_column = random.randint(0, 9)
            if direction == 'horizontal' and cpu_row >= 5:
                if cpu_board[cpu_row][cpu_column - 1] == 1 or cpu_board[cpu_row][cpu_column - 2] == 1:
                    # ( reroll )
                    cpu_row = random.randint(0, 9)
                    cpu_column = random.randint(0, 9)
            cpu_location = [letters[cpu_row], str(cpu_column)]
            cpu_board[cpu_row][cpu_column] = 1
            cpu_board_display[cpu_row][cpu_column] = game_symbols[2]
            cpu_ship_coordinates[ship_counter].append(cpu_location)
            # if direction == 'horizontal':
            #     print("\ncpu horizontal alignment at: " + str(cpu_location))
            # if direction == 'vertical':
            #     print('\ncpu vertical alignment at: ' + str(cpu_location))
            print('\nPlayer_1 Enter Coordinates for [' + ships[ship_counter] + ']:')
            temp_count = 0
            cpu_tcount = 1

            #  ( Player Turn  && CPU Turn )
            for j in range(ships_spaces[ship_counter]):
                temp_arr = []

                # ( Player Coordinates )
                resp = input(str(temp_count) + ': ')
                temp_arr.append(resp[0].upper())
                temp_arr.append(resp[2])

                # ( Update p1_board_display )
                p1_board_display[letters.index(resp[0].upper())][int(resp[2])] = game_symbols[2]
                p1_board[letters.index(resp[0].upper())][int(resp[2])] = 1

                # ( Update Coordinates )
                p1_ship_coordinates[ship_counter].append(temp_arr)  # may need to be a set

                # ( Plot Remaining CPU Coordinates )
                if cpu_tcount < ships_spaces[ship_counter]:
                    if direction == 'horizontal' and cpu_column <= 5:
                        cpu_board[cpu_row][cpu_column + cpu_tcount] = 1
                        cpu_board_display[cpu_row][cpu_column + cpu_tcount] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row], str(cpu_column + cpu_tcount)])
                    elif direction == 'horizontal' and cpu_column >= 5:
                        # ( Overlap Check )
                        cpu_board[cpu_row][cpu_column - cpu_tcount] = 1
                        cpu_board_display[cpu_row][cpu_column - cpu_tcount] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row], str(cpu_column - cpu_tcount)])
                    elif direction == 'vertical' and cpu_row <= 5:
                        # ( Overlap Check )
                        cpu_board[cpu_row + cpu_tcount][cpu_column] = 1
                        cpu_board_display[cpu_row + cpu_tcount][cpu_column] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row + cpu_tcount], str(cpu_column)])
                    elif direction == 'vertical' and cpu_row >= 5:
                        # ( Overlap Check )
                        cpu_board[cpu_row - cpu_tcount][cpu_column] = 1
                        cpu_board_display[cpu_row - cpu_tcount][cpu_column] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row - cpu_tcount], str(cpu_column)])
                    cpu_tcount += 1

            # ( End / Update Ship Location Placement )
            ship_space_counter += 1
            ship_counter += 1
            print('')
            print('PLAYER BOARD')
            board_display(p1_board_display)
            print('')

        # ( Coordinate Warfare Begins )
        print('--------------------------------------------------')
        print('!!!! WAR BEGINS !!!!')
        print('--------------------------------------------------')

        # ( If Player Goes First )
        if first_list[0]:
            print('P1 Ship Coordinates:\t' + str(p1_ship_coordinates))
            print('CPU Ship Coordinates:\t' + str(cpu_ship_coordinates))
            while player_1_health > 0 or cpu_health > 0:

                # ( Player Enter Guess )
                player_input = input('\nPlayer_1 Enter Strike Coordinates:\t')
                pr = letters.index(player_input[0])
                pc = player_input[2]
                player_guess = [pr, pc]

                ca = 0
                pa = 0

                # ( Check Board ) -> Hit / Miss
                if cpu_board[player_guess[0]][int(player_guess[1])] == 1:
                    cpu_board_display[player_guess[0]][int(player_guess[1])] = game_symbols[0]
                    cpu_board[player_guess[0]][int(player_guess[1])] = 0
                    # ( Compare )
                    i = 0
                    for ship in cpu_ships:
                        for coordinate in ship:
                            if len(coordinate) > 0:
                                if letters[player_guess[0]] == coordinate[0] and player_guess[1] == coordinate[1]:
                                    coordinate.pop(0)
                                    coordinate.pop(0)
                                    ship.remove([])
                        i += 1

                    print('')
                    board_display(p1_board_display)
                    print('\n( CPU : HIT !!!! )\n')
                    if len(cpu_ships[0]) == 0:
                        ca += 1
                        print('(CPU) Aircraft Carrier:\tSunken...')
                    else:
                        print('(CPU) Aircraft Carrier:\tActive')
                    if len(cpu_ships[1]) == 0:
                        ca += 1
                        print('(CPU) Battleship:\t\tSunken...')
                    else:
                        print('(CPU) Battleship:\t\tActive')
                    if len(cpu_ships[2]) == 0:
                        ca += 1
                        print('(CPU) Cruiser:\t\t\tSunken...')
                    else:
                        print('(CPU) Cruiser:\t\t\tActive')
                    if len(cpu_ships[3]) == 0:
                        ca += 1
                        print('(CPU) Submarine:\t\tSunken...')
                    else:
                        print('(CPU) Submarine:\t\tActive')
                    if len(cpu_ships[4]) == 0:
                        ca += 1
                        print('(CPU) Destroyer:\t\tSunken...')
                    else:
                        print('(CPU) Destroyer:\t\tActive')

                    cpu_health = 5 - ca
                    if cpu_health == 0:
                        break
                    print('(Sunken #): ' + str(ca))
                    print('(CPU Health): ' + str(cpu_health))
                else:
                    cpu_board_display[player_guess[0]][int(player_guess[1])] = game_symbols[1]

                    print('')
                    board_display(p1_board_display)
                    print('\n( CPU : Miss !!!! )\n')
                    if len(cpu_ships[0]) == 0:
                        ca += 1
                        print('(CPU) Aircraft Carrier:\tSunken...')
                    else:
                        print('(CPU) Aircraft Carrier:\tActive')
                    if len(cpu_ships[1]) == 0:
                        ca += 1
                        print('(CPU) Battleship:\t\tSunken...')
                    else:
                        print('(CPU) Battleship:\t\tActive')
                    if len(cpu_ships[2]) == 0:
                        ca += 1
                        print('(CPU) Cruiser:\t\t\tSunken...')
                    else:
                        print('(CPU) Cruiser:\t\t\tActive')
                    if len(cpu_ships[3]) == 0:
                        ca += 1
                        print('(CPU) Submarine:\t\tSunken...')
                    else:
                        print('(CPU) Submarine:\t\tActive')
                    if len(cpu_ships[4]) == 0:
                        ca += 1
                        print('(CPU) Destroyer:\t\tSunken...')
                    else:
                        print('(CPU) Destroyer:\t\tActive')

                    cpu_health = 5 - ca
                    if cpu_health == 0:
                        break
                    print('(Sunken #): ' + str(ca))
                    print('(CPU Health): ' + str(cpu_health))

                # ( Generate CPU Guess )
                cpu_rowg = random.randint(0, 9)
                cpu_colg = random.randint(0, 9)
                cpu_guess = [letters[cpu_rowg], cpu_colg]
                print('\nCPU Entered Strike Coordinates: ' + str(cpu_guess[0]) + ' ' + str(cpu_guess[1]), end='\n')

                # ( Check Board ) -> Hit / Miss
                if p1_board[letters.index(cpu_guess[0])][int(cpu_guess[1])] == 1:
                    p1_board_display[letters.index(cpu_guess[0])][int(cpu_guess[1])] = game_symbols[0]
                    p1_board[letters.index(cpu_guess[0])][int(cpu_guess[1])] = 0
                    # ( Compare )
                    i = 0
                    for ship in p1_ships:
                        for coordinate in ship:
                            if len(coordinate) > 0:
                                if str(cpu_guess[0]) == coordinate[0] and str(cpu_guess[1]) == coordinate[1]:
                                    coordinate.pop(0)
                                    coordinate.pop(0)
                                    ship.remove([])
                        i += 1
                    print('\n( Player: HIT !!!! )\n')
                    if len(p1_ships[0]) == 0:
                        pa += 1
                        print('(P1) Aircraft Carrier:\tSunken...')
                    else:
                        print('(P1) Aircraft Carrier:\t' + str(p1_ships[0]))
                    if len(p1_ships[1]) == 0:
                        pa += 1
                        print('(P1) Battleship:\t\tSunken...')
                    else:
                        print('(P1) Battleship:\t' + str(p1_ships[1]))
                    if len(p1_ships[2]) == 0:
                        pa += 1
                        print('(P1) Cruiser:\t\t\tSunken...')
                    else:
                        print('(P1) Cruiser:\t' + str(p1_ships[2]))
                    if len(p1_ships[3]) == 0:
                        pa += 1
                        print('(P1) Submarine:\t\tSunken...')
                    else:
                        print('(P1) Submarine:\t' + str(p1_ships[3]))
                    if len(p1_ships[4]) == 0:
                        pa += 1
                        print('(P1) Destroyer:\t\tSunken...')
                    else:
                        print('(P1) Destroyer:\t' + str(p1_ships[4]))

                    player_1_health = 5 - pa
                    if player_1_health == 0:
                        break
                    print('(Sunk #): ' + str(pa))
                    print('(Player Health): ' + str(player_1_health))
                else:
                    p1_board_display[letters.index(cpu_guess[0])][int(cpu_guess[1])] = game_symbols[1]
                    print('\n( Player: Miss !!!! )\n')
                    if len(p1_ships[0]) == 0:
                        pa += 1
                        print('(P1) Aircraft Carrier:\tSunken...')
                    else:
                        print('(P1) Aircraft Carrier:\t' + str(p1_ships[0]))
                    if len(p1_ships[1]) == 0:
                        pa += 1
                        print('(P1) Battleship:\t\tSunken...')
                    else:
                        print('(P1) Battleship:\t' + str(p1_ships[1]))
                    if len(p1_ships[2]) == 0:
                        pa += 1
                        print('(P1) Cruiser:\t\t\tSunken...')
                    else:
                        print('(P1) Cruiser:\t' + str(p1_ships[2]))
                    if len(p1_ships[3]) == 0:
                        pa += 1
                        print('(P1) Submarine:\t\tSunken...')
                    else:
                        print('(P1) Submarine:\t' + str(p1_ships[3]))
                    if len(p1_ships[4]) == 0:
                        pa += 1
                        print('(P1) Destroyer:\t\tSunken...')
                    else:
                        print('(P1) Destroyer:\t' + str(p1_ships[4]))

                    player_1_health = 5 - pa
                    if player_1_health == 0:
                        break
                    print('(Sunk #): ' + str(pa))
                    print('(Player Health): ' + str(player_1_health))

        # ( If CPU Goes First )
        if first_list[2]:
            print('P1 Ship Coordinates:\t' + str(p1_ship_coordinates))
            print('CPU Ship Coordinates:\t' + str(cpu_ship_coordinates))
            while player_1_health > 0 or cpu_health > 0:
                # ( Generate CPU Guess )
                cpu_rowg = random.randint(0, 9)
                cpu_colg = random.randint(0, 9)
                cpu_guess = [letters[cpu_rowg], cpu_colg]
                ca = 0
                pa = 0

                print('\nCPU Entered Strike Coordinates: ' + str(cpu_guess[0]) + ' ' + str(cpu_guess[1]), end='\n')

                # ( Check Board ) -> Hit / Miss
                if p1_board[letters.index(cpu_guess[0])][int(cpu_guess[1])] == 1:
                    p1_board_display[letters.index(cpu_guess[0])][int(cpu_guess[1])] = game_symbols[0]
                    p1_board[letters.index(cpu_guess[0])][int(cpu_guess[1])] = 0
                    # ( Compare )
                    i = 0
                    for ship in p1_ships:
                        for coordinate in ship:
                            if len(coordinate) > 0:
                                if str(cpu_guess[0]) == coordinate[0] and str(cpu_guess[1]) == coordinate[1]:
                                    coordinate.pop(0)
                                    coordinate.pop(0)
                                    ship.remove([])
                        i += 1

                    print('( Player: HIT !!!! )\n')

                    if len(p1_ships[0]) == 0:
                        pa += 1
                        print('(P1) Aircraft Carrier:\tSunken...')
                    else:
                        print('(P1) Aircraft Carrier:\t' + str(p1_ships[0]))
                    if len(p1_ships[1]) == 0:
                        pa += 1
                        print('(P1) Battleship:\t\tSunken...')
                    else:
                        print('(P1) Battleship:\t' + str(p1_ships[1]))
                    if len(p1_ships[2]) == 0:
                        pa += 1
                        print('(P1) Cruiser:\t\t\tSunken...')
                    else:
                        print('(P1) Cruiser:\t' + str(p1_ships[2]))
                    if len(p1_ships[3]) == 0:
                        pa += 1
                        print('(P1) Submarine:\t\tSunken...')
                    else:
                        print('(P1) Submarine:\t' + str(p1_ships[3]))
                    if len(p1_ships[4]) == 0:
                        pa += 1
                        print('(P1) Destroyer:\t\tSunken...')
                    else:
                        print('(P1) Destroyer:\t' + str(p1_ships[4]))

                    player_1_health = 5 - pa
                    if player_1_health == 0:
                        break
                    print('(Sunk #): ' + str(pa))
                    print('(Player Health): ' + str(player_1_health))
                else:
                    p1_board_display[letters.index(cpu_guess[0])][int(cpu_guess[1])] = game_symbols[1]
                    print('( Player: MISS !!!! )\n')

                    if len(p1_ships[0]) == 0:
                        pa += 1
                        print('(P1) Aircraft Carrier:\tSunken...')
                    else:
                        print('(P1) Aircraft Carrier:\t' + str(p1_ships[0]))
                    if len(p1_ships[1]) == 0:
                        pa += 1
                        print('(P1) Battleship:\t\tSunken...')
                    else:
                        print('(P1) Battleship:\t' + str(p1_ships[1]))
                    if len(p1_ships[2]) == 0:
                        pa += 1
                        print('(P1) Cruiser:\t\t\tSunken...')
                    else:
                        print('(P1) Cruiser:\t' + str(p1_ships[2]))
                    if len(p1_ships[3]) == 0:
                        pa += 1
                        print('(P1) Submarine:\t\tSunken...')
                    else:
                        print('(P1) Submarine:\t' + str(p1_ships[3]))
                    if len(p1_ships[4]) == 0:
                        pa += 1
                        print('(P1) Destroyer:\t\tSunken...')
                    else:
                        print('(P1) Destroyer:\t' + str(p1_ships[4]))

                    player_1_health = 5 - pa
                    if player_1_health == 0:
                        break
                    print('(Sunk #): ' + str(pa))
                    print('(Player Health): ' + str(player_1_health))

                # ( Player Enter Guess )
                player_input = input('\nPlayer_1 Enter Strike Coordinates:\t')
                pr = letters.index(player_input[0])
                pc = player_input[2]
                player_guess = [pr, pc]

                # ( Check Board ) -> Hit / Miss
                if cpu_board[player_guess[0]][int(player_guess[1])] == 1:
                    cpu_board_display[player_guess[0]][int(player_guess[1])] = game_symbols[0]
                    cpu_board[player_guess[0]][int(player_guess[1])] = 1
                    # ( Compare )
                    i = 0
                    for ship in cpu_ships:
                        for coordinate in ship:
                            if len(coordinate) > 0:
                                if letters[player_guess[0]] == coordinate[0] and player_guess[1] == coordinate[1]:
                                    coordinate.pop(0)
                                    coordinate.pop(0)
                                    ship.remove([])
                        i += 1
                    print('(CPU Sunk #): ' + str(ca))

                    print('\n')
                    board_display(p1_board_display)
                    print('\n( CPU: HIT !!!! )\n')

                    if len(cpu_ships[0]) == 0:
                        ca += 1
                        print('(CPU) Aircraft Carrier:\tSunken...')
                    else:
                        print('(CPU) Aircraft Carrier:\tActive')
                    if len(cpu_ships[1]) == 0:
                        ca += 1
                        print('(CPU) Battleship:\t\tSunken...')
                    else:
                        print('(CPU) Battleship:\t\tActive')
                    if len(cpu_ships[2]) == 0:
                        ca += 1
                        print('(CPU) Cruiser:\t\t\tSunken...')
                    else:
                        print('(CPU) Cruiser:\t\t\tActive')
                    if len(cpu_ships[3]) == 0:
                        ca += 1
                        print('(CPU) Submarine:\t\tSunken...')
                    else:
                        print('(CPU) Submarine:\t\tActive')
                    if len(cpu_ships[4]) == 0:
                        ca += 1
                        print('(CPU) Destroyer:\t\tSunken...')
                    else:
                        print('(CPU) Destroyer:\t\tActive')

                    cpu_health = 5 - ca
                    if cpu_health == 0:
                        break
                    print('(Sunk #): ' + str(ca))
                    print('(CPU Health): ' + str(cpu_health))
                else:
                    cpu_board_display[player_guess[0]][int(player_guess[1])] = game_symbols[1]
                    print('\n')
                    board_display(p1_board_display)
                    print('\n( CPU: Miss !!!! )\n')
                    if len(cpu_ships[0]) == 0:
                        ca += 1
                        print('(CPU) Aircraft Carrier:\tSunken...')
                    else:
                        print('(CPU) Aircraft Carrier:\tActive')
                    if len(cpu_ships[1]) == 0:
                        ca += 1
                        print('(CPU) Battleship:\t\tSunken...')
                    else:
                        print('(CPU) Battleship:\t\tActive')
                    if len(cpu_ships[2]) == 0:
                        ca += 1
                        print('(CPU) Cruiser:\t\t\tSunken...')
                    else:
                        print('(CPU) Cruiser:\t\t\tActive')
                    if len(cpu_ships[3]) == 0:
                        ca += 1
                        print('(CPU) Submarine:\t\tSunken...')
                    else:
                        print('(CPU) Submarine:\t\tActive')
                    if len(cpu_ships[4]) == 0:
                        ca += 1
                        print('(CPU) Destroyer:\t\tSunken...')
                    else:
                        print('(CPU) Destroyer:\t\tActive')

                    cpu_health = 5 - ca
                    print('(Sunk #): ' + str(ca))
                    print('(CPU Health): ' + str(cpu_health))

    print('\nGAME OVER !!!!\n')

    if player_1_health > cpu_health:
        print('Player 1:\tVICTORY')
    elif cpu_health > player_1_health:
        print('CPU :\tVICTORY')
print('==================================================' * 2)
# =========================================================================
