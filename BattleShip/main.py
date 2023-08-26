# =========================================================================
# ( BattleShip ):
# (Developed By): -> Otis R. Jackson IV
# =========================================================================
# ( Program Modules )
import random

# ( Global Attributes )
multi_player = False
single_player = False
p1_board, p2_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
                                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
p1_board_display, p2_board_display = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']], [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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

p1_ships = 5
cpu_ships = 5

# ( Game Functions )
# who goes first function ( Heads or Tails )
def first_play(player1_f, player2_f, cpu_f):
    if not multi_player:
        user_guess = input('\n[Player 1] Pick / Type Heads or Tails: \t')
        if user_guess == turn_array[coin_flip]:
            player1_f = True

            # Debug
            print('\n( player1_f ): ' + str(player1_f), end='\n')
            print('( cpu_f ): ' + str(cpu_f), end='\n')

            print('\nPlayer 1 Goes First !!\n')
        else:
            cpu_f = True

            # Debug
            print('\n( player1_f ): ' + str(player1_f), end='\n')
            print('( cpu_f ): ' + str(cpu_f), end='\n')

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

# board display (pass in the board)
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

# lose check / board check

print('=================================================='*2)
print('Welcome To BattleShip')
print('Developed by : Otis Ray Jackson IV')

# ( Display Ruleset )
print('--------------------------------------------------'*2)
print('( Basic Ruleset of BattleShip )')
print('--------------------------------------------------'*2)
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
    print('\n( player1_f ): ' + str(first_list[0]))
    print('( player2_f ): ' + str(first_list[1]))
    print('( cpu_f ): ' + str(first_list[2]))

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

    # Debug
    print('\n( player1_f ): ' + str(first_list[0]))
    print('( player2_f ): ' + str(first_list[1]))
    print('( cpu_f ): ' + str(first_list[2]))

    # ( Display Board )

    # ( Game Start )
    # ->    Place Coordinates
    ship_counter = 0                # for indexes of ships = [Aircraft Carrier, ....]
    ship_space_counter = 0          # for indexes of ships_spaces = [5, 4, 3, 3, 2]
    while ship_counter < 5:
        if ship_counter > 4:
            break
        print('\nPlayer_1 Enter Coordinates for [' + ships[ship_counter] + ']:')
        temp_count = 0
        while temp_count < ships_spaces[ship_counter]:
            temp_arr = []
            resp = input(str(temp_count)+ ': ')
            temp_arr.append(resp[0].upper())
            temp_arr.append(resp[2])

            # ( Update p1_board_display )
            p1_board_display[letters.index(resp[0].upper())][int(resp[2])] = game_symbols[2]

            print('temp_arr: ' + str(temp_arr))
            p1_ship_coordinates[ship_counter].append(temp_arr)
            temp_count += 1

        # End / Update
        ship_space_counter += 1
        ship_counter += 1

        print('')
        board_display(p1_board_display)
        print('\n')

        print(p1_ship_coordinates)

print('loop finished')
    # ( Game Start )
    # while game_start:
    #     # ( If Condition )
    #     if p1_ships > 0 > cpu_ships:
    #         print('\nPlayer Victory !!\n')
    #         break
    #     if p1_ships < 0 < cpu_ships:
    #         print('\nCPU Victory !!\n')
    #         break
    #
        # # ( If CPU First )
        # if cpu_f:
        #     # ( Guess )
        #     # A -> J
        #     cpu_rg = random.randint(0, 9)
        #     # 0 -> 9
        #     cpu_cg = random.randint(0, 9)
        #     cpu_temp = [str(cpu_rg), str(cpu_cg)]
        #     print('CPU coordinates:\t' + str(letters[cpu_rg]) + ' ' + str(cpu_cg))
    #
    #         # ( Board Check )
    #         # if
    #
    #         # ( Player Turn )
    #
    #
    #
    #     # ( If Player First )

# ( Game Loop )
# if game_start:
#     print('\nWAR Starts !!!')
#     while p1_ships > 0:
#         # ( Conditions )
#         if p1_ships > 0 > cpu_ships:
#             print('\nPlayer Victory !!\n')
#             break
#         if p1_ships < 0 < cpu_ships:
#             print('\nCPU Victory !!\n')
#             break
#
#         # ( If CPU First )
#         if cpu_f:
#             # ( Guess )
#             # A -> J
#             cpu_rg = random.randint(0, 9)
#             # 0 -> 9
#             cpu_cg = random.randint(0, 9)
#             cpu_temp = [str(cpu_rg), str(cpu_cg)]
#             print('CPU coordinates:\t' + str(letters[cpu_rg]) + ' ' + str(cpu_cg))

print()
print('=================================================='*2)
# =========================================================================