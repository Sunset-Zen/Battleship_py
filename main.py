# =========================================================================
# ( BattleShip ):
# (Developed By): -> Otis R. Jackson IV
# =========================================================================
# ( Program Modules )
import random

# ( Global Attributes )
multi_player = False
single_player = False
p1_board, p2_board, cpu_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
p1_board_display, p2_board_display, cpu_board_display = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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
player1_f, player2_f, cpu_f = False, False, False
player_1_ships, player_2_ships, player_3_ships = 5, 5, 5
game_start = True

game_symbols = ['X', '-', '#']
turn_array = ['Heads', 'Tails']
coin_flip = random.randint(0, 1)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ships = ['Aircraft Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
ships_spaces = [5, 4, 3, 3, 2]
p1_ship_coordinates = [[], [], [], [], []]
p2_ship_coordinates = [[], [], [], [], []]
cpu_ship_coordinates = [[], [], [], [], []]

p1_ships = 5
cpu_ships = 5


# ( Game Functions )
# ( Who goes first function ( Heads or Tails ) )
def first_play(player1_f, player2_f, cpu_f):
    if not multi_player:
        user_guess = input('\n[Player 1] Pick / Type Heads or Tails: \t')
        if user_guess == turn_array[coin_flip]:
            player1_f = True

            # Debug
            # print('\n( player1_f ): ' + str(player1_f), end='\n')
            # print('( cpu_f ): ' + str(cpu_f), end='\n')

            print('\nPlayer 1 Goes First !!\n')
        else:
            cpu_f = True

            # Debug
            # print('\n( player1_f ): ' + str(player1_f), end='\n')
            # print('( cpu_f ): ' + str(cpu_f), end='\n')

            print('\nCPU Player Goes First !!\n')
    else:
        user_guess = input('\n[Player 1] Pick / Type Heads or Tails: \t')
        user_guess2 = input('\n[Player 2] Pick / Type Heads or Tails: \t')
        if user_guess == turn_array[coin_flip]:
            player1_f = True
            # Debug
            print('\n( player1_f ): ' + str(player1_f), end='\n')
            print('( player2_f ): ' + str(player2_f), end='\n')

            print('\nPlayer 1 Goes First !!')
        else:
            player2_f = True
            # Debug
            print('\n( player1_f ): ' + str(player1_f), end='\n')
            print('( player2_f ): ' + str(player2_f), end='\n')

            print('\nPlayer 2 Goes First !!\n')
    return [player1_f, player2_f, cpu_f]


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
    # print('')


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

# ( Multiplayer ??? )
multiplayer_option = input('\nMultiplayer ?: Type A for [Yes] and B for [No]:\t')
if multiplayer_option == 'A':
    multi_player = True
    single_player = False
else:
    multi_player = False
    single_player = True

# ( Multi Player:  [player-1 vs player-2] Game Loop )
if multi_player:
    # ( Determine Who Goes First )
    first_list = first_play(player1_f, player2_f, cpu_f)

    # ( Display Board )
    print('--------------------------------------------------')
    print('( Board Display )')
    print('--------------------------------------------------')
    board_display(p1_board_display)
    print('--------------------------------------------------')

    # Debug
    # print('\n( player1_f ): ' + str(first_list[0]))
    # print('( player2_f ): ' + str(first_list[1]))
    # print('( cpu_f ): ' + str(first_list[2]))

    print('\nMultiplayer Mode Under Maintenance....')

    # ( Battleship Management : Board placement of Ships)
    # ( Update Board )

# ( Single Player: [player-1 vs cpu_player] Game Loop )
if single_player:
    # ( Determine Who Goes First )
    first_list = first_play(player1_f, player2_f, cpu_f)
    # ( Display Board )
    print('--------------------------------------------------')
    print('( Board Display )')
    print('--------------------------------------------------')
    board_display(p1_board_display)
    print('--------------------------------------------------')

    while game_start:
        # ( Game Start )
        ship_counter = 0  # for indexes of ships = [Aircraft Carrier, ....]
        ship_space_counter = 0  # for indexes of ships_spaces = [5, 4, 3, 3, 2]
        # ( Place Coordinates ( Player_1 && Player_2 ) )
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
            if direction == 'horizontal' and cpu_row < 5:
                if cpu_board[cpu_row][cpu_column + 1] == 1:
                    # ( reroll )
                    cpu_row = random.randint(0, 9)
                    cpu_column = random.randint(0, 9)

            cpu_location = [letters[cpu_row], str(cpu_column)]
            cpu_board[cpu_row][cpu_column] = 1
            cpu_board_display[cpu_row][cpu_column] = game_symbols[2]
            cpu_ship_coordinates[ship_counter].append(cpu_location)

            if direction == 'horizontal':
                print("\ncpu horizontal alignment at: " + str(cpu_location))
            if direction == 'vertical':
                print('\ncpu vertical alignment at: ' + str(cpu_location))
            print('\nPlayer_1 Enter Coordinates for [' + ships[ship_counter] + ']:')

            temp_count = 0
            cpu_tcount = 1

            #  ( Player Turn  && CPU Turn )
            for j in range(ships_spaces[ship_counter]):
                # while temp_count < ships_spaces[ship_counter]:
                temp_arr = []

                # ( Player Coordinates )
                resp = input(str(temp_count) + ': ')
                temp_arr.append(resp[0].upper())
                temp_arr.append(resp[2])

                # ( Update p1_board_display )
                p1_board_display[letters.index(resp[0].upper())][int(resp[2])] = game_symbols[2]
                p1_board[letters.index(resp[0].upper())][int(resp[2])] = 1

                # ( Update Coordinates )
                p1_ship_coordinates[ship_counter].append(temp_arr)

                # ( Plot Remaining CPU Coordinates )
                if cpu_tcount < ships_spaces[ship_counter]:
                    if direction == 'horizontal' and cpu_column <= 5:
                        cpu_board[cpu_row][cpu_column + cpu_tcount] = 1
                        cpu_board_display[cpu_row][cpu_column + cpu_tcount] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row], cpu_column + cpu_tcount])
                    elif direction == 'horizontal' and cpu_column >= 5:
                        # ( Overlap Check )
                        cpu_board[cpu_row][cpu_column - cpu_tcount] = 1
                        cpu_board_display[cpu_row][cpu_column - cpu_tcount] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row], cpu_column - cpu_tcount])
                    elif direction == 'vertical' and cpu_row <= 5:
                        # ( Overlap Check )
                        cpu_board[cpu_row + cpu_tcount][cpu_column] = 1
                        cpu_board_display[cpu_row + cpu_tcount][cpu_column] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row + cpu_tcount], cpu_column])
                    elif direction == 'vertical' and cpu_row >= 5:
                        # ( Overlap Check )
                        cpu_board[cpu_row - cpu_tcount][cpu_column] = 1
                        cpu_board_display[cpu_row - cpu_tcount][cpu_column] = game_symbols[2]
                        cpu_ship_coordinates[ship_counter].append([letters[cpu_row - cpu_tcount], cpu_column])
                    cpu_tcount += 1

            # ( End / Update Ship Location Placement )
            ship_space_counter += 1
            ship_counter += 1
            print('')
            print('PLAYER BOARD')
            board_display(p1_board_display)
            print('\n')
            print('CPU BOARD')
            board_display(cpu_board_display)
            print('\n')

        # ( Coordinate Warfare Begins )
        print('--------------------------------------------------')
        print('!!!! WAR BEGINS !!!!')
        print('--------------------------------------------------')

        # ( If Player Goes First )
        if first_list[0]:
            print('P1 Ship Coordinates:\t' + str(p1_ship_coordinates))
            print('CPU Ship Coordinates:\t' + str(cpu_ship_coordinates))
            while player_1_ships > 0 or cpu_ships > 0:
                # ( Player Enter Guess )
                player_input = input('\nPlayer_1 Enter Strike Coordinates:\t')
                pr = letters.index(player_input[0])
                pc = player_input[2]
                player_guess = [pr, pc]

                # ( Check Board )
                if cpu_board[player_guess[0]][int(player_guess[1])] == 1:
                    print('( CPU: HIT !!!! )')
                else:
                    print('( CPU: Miss !!!! )')

                # ( Generate CPU Guess )
                cpu_rowg = random.randint(0, 9)
                cpu_colg = random.randint(0, 9)
                cpu_guess = [letters[cpu_rowg], cpu_colg]
                print('\nCPU Entered Strike Coordinates: ' + str(cpu_guess[0]) + ' ' + str(cpu_guess[1]))

                # ( Check Board )
                if p1_board[letters.index(cpu_guess[0])][int(cpu_guess[1])] == 1:
                    print('( Player: HIT !!!! )')
                else:
                    print('( Player: Miss !!!! )')
        # ( If CPU Goes First )
        if first_list[2]:
            print('P1 Ship Coordinates:\t' + str(p1_ship_coordinates))
            print('CPU Ship Coordinates:\t' + str(cpu_ship_coordinates))
            while player_1_ships > 0 or cpu_ships > 0:
                # ( Generate CPU Guess )
                cpu_rowg = random.randint(0, 9)
                cpu_colg = random.randint(0, 9)
                cpu_guess = [letters[cpu_rowg], cpu_colg]
                print('\nCPU Entered Strike Coordinates: ' + str(cpu_guess[0]) + ' ' + str(cpu_guess[1]))

                # ( Check Board )
                if p1_board[cpu_guess[0]][int(cpu_guess[1])] == 1:
                    print('( Player: HIT !!!! )')
                else:
                    print('( Player: Miss !!!! )')

                # ( Player Enter Guess )
                player_input = input('\nPlayer_1 Enter Strike Coordinates:\t')
                pr = letters.index(player_input[0])
                pc = player_input[2]
                player_guess = [pr, pc]

                # ( Check Board )
                if cpu_board[player_guess[0]][int(player_guess[1])] == 1:
                    print('( CPU: HIT !!!! )')
                else:
                    print('( Player: Miss !!!! )')

    print('GAME OVER !!!!')
print('==================================================' * 2)
# =========================================================================
