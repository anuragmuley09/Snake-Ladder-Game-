import tkinter as tk

# PIL == python imaging library
from PIL import ImageTk, Image
import random

'''
DESIGNING PART :
    1. SHOW BOARD
    2. PLACE TOKENS AT START
    3. CREATING WINDOW AND PLACING BOARD INT IT 
    4. CREATING BUTTONS FOR PLAYER 1 AND PLAYER 2
    5. CREATING BUTTON TO ROLL DIE
    6. CREATING BUTTON TO EXIT THE GAME

    ---------------------------------
    TASKS:

'''

# snakes
snakes = {
    47:9,
    62:40,
    96:75
}

# ladder
ladder = {
    6:46,
    19:43,  
    52:71,
    57:98
}


# function to display board
def show_board():
    # if we dont do this then we will not be able to see the initial status of dice
    global initial_Dice
    global player1_button
    global player2_button

    # now we will add buttons for player 1 and player 2
    # for player 1
    # now we have created a button for player 1, but in order to display it on the window, we must place it using .place
    # goto players buttons for more info
    player1_button.place(x=920, y=250)

    # similarly for player 2
    player2_button.place(x=920, y=350)
 
    # DICE
    initial_Dice = Image.open("Project helper\dice-final.png")
    initial_Dice = initial_Dice.resize((65, 65))
    initial_Dice = ImageTk.PhotoImage(initial_Dice)

    # this button dosent rolls the dice; but we are using button to display dice status cause its easy to implement
    roll_Dice_button = tk.Button(window, image=initial_Dice, height=80, width=80)
    roll_Dice_button.place(x=920, y=500)

    # exit button
    exit_button = tk.Button(window, text="EXIT - ENDGAME", height=3, width=15, activebackground="#e39fb4", command=window.destroy)
    exit_button.place(x=920, y=100)





# function to put tokens at there initial positions
def place_tokens_at_start():
    global player1_token, player2_token
    global player1_position
    global player2_position
    player1_token.place(x=0, y=650)
    player2_token.place(x=50, y=650)

    # initilizing players starting position
    player1_position = 0
    player2_position = 0






# loading dice images and putting them into a constant variable(list) dice.
def load_dice_images():
    global dice
    dice_images = ["\dice1.png", "\dice2.png", "\dice3.png", "\dice4.png", "\dice5.png", "\dice6.png"]
    for img in dice_images:
        Dice_image = Image.open("Project helper"+img)
        Dice_image = Dice_image.resize((65, 65))
        Dice_image = ImageTk.PhotoImage(Dice_image)
        dice.append(Dice_image)





# The main logic of the game
def roll_dice():
    global dice
    global turn
    global player1_position
    global player2_position
    global player1_button
    global player2_button

    # generate a random number between 1-6 
    random_num = random.randint(1, 6)

    # according to the number generated (random_num), display respective dice image on the roll_dice_image button
    roll_Dice_button = tk.Button(window, image=dice[random_num-1], height=80, width=80)
    roll_Dice_button.place(x=920, y=500)

    # now check if turn is 1
    # if turn in 1 then this means its player 1 chance (blue)
    # now add this random_num to the players position, after addition of random_num, check following conditions
    # 1. if player1's updated position is 100 (win case) then display "win" and stop
    # 2. if player position is greater than 100 then subtract random number from the new position (to stay on same cell)
    # 3. now, if current position is present in ladder then reassign position 
    # 4. if position in snake...
    # now call function "move_token" with arguments as turn and player1 position
    # assign turn to 2, indicating its second player turn
    # disable player1's button and enable player2's button

    # same algo if turn == 2
    if turn == 1:
        player1_position += random_num
        if player1_position == 100:
            player2_button.config(state="disabled")
            player1_button.config(state="disabled")
            display_won = tk.Message(text="player 1 won", background="blue",fg="#BFF906", font=("Monospace", 20, "bold"))
            display_won.place(x=600, y=400)

            
        if player1_position > 100:
            player1_position -= random_num
        if player1_position in ladder:
            player1_position = ladder[player1_position]
        elif player1_position in snakes:
            player1_position = snakes[player1_position]

        move_token(turn, player1_position)
        turn = 2
        player1_button.config(state="disabled")
        player2_button.config(state="normal")


    else:
        player2_position += random_num
        if player2_position == 100:
            player1_button.config(state="disabled")
            player2_button.config(state="disabled")
            display_won = tk.Message(text="player 2 won", background="red",fg="#1ECBE1", font=("Monospace", 20, "bold"))
            display_won.place(x=600, y=400)

            
        if player2_position > 100:
            player2_position -= random_num
        if player2_position in ladder:
            player2_position = ladder[player2_position]
        elif player2_position in snakes:
            player2_position = snakes[player2_position]

        move_token(turn, player2_position)
        turn = 1
        player2_button.config(state="disabled")
        player1_button.config(state="normal")









# this is the function behind movement of token. 
def move_token(turn, random_num):
    global player1_token, player2_token
    global Index

    # check is turn is 1, if yes then place token accordingly
    if(turn == 1):
        player1_token.place(x=Index[random_num][0], y=Index[random_num][1])
    
    else:
        player2_token.place(x=Index[random_num][0], y=Index[random_num][1])
        





# this will store dice images, like ,1,2,3...
# after calling load_dice_images function, this variable(here list) will contain
# path for every image of dice
# const variable
dice = []






# x diff = 85 --> col
# y diff = 60 --> row
def get_index_of_Cell():
    # global player1_token
    # global player2_token
    Number = [
        100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    # row = 20
    # col = 35
    # player1_token.place(x=35, y=20)
    # player2_token.place(x=205, y=140)
    row = 20
    i = 0
    for x in range(1, 11):
        col = 35
        for y in range(1, 11):
            Index[Number[i]]=(col, row)
            col += 85
            i += 1
        row += 60
    # print(Index)
    





# this variable (constant type) will store all the co-ordinates
Index = {}





# initial positions of player 1 and player 2
player1_position = None
player2_position = None




#------------------------------------------------------
# creating a window
window = tk.Tk()
window.title("Snake and Ladder Game")
window.geometry("1200x800") 
# we will be using this frame object to display board
frame1 = tk.Frame(
    window,
    width=1200,
    height=800,
    relief='raised'
)
frame1.place(x=0, y=0)
# now setting board into the frame
board_image = ImageTk.PhotoImage(Image.open("Project helper\snake and ladder.png")) 
label = tk.Label(frame1, image=board_image)
label.place(x=0, y=0)



# players buttons
player1_button = tk.Button(window, text="player 1", height=3, width=10, activebackground="#e39fb4", command=roll_dice)
player2_button = tk.Button(window, text="player 2", height=3, width=10, activebackground="#e39fb4", command=roll_dice)



# creating tokens for player 1 and player 2
player1_token = tk.Canvas(window, width=30, height=30)
player1_token.create_oval(10, 10, 30, 30, fill="blue")




player2_token = tk.Canvas(window, width=30, height=30)
player2_token.create_oval(10, 10, 30, 30, fill="red")




# whose first turn? if turn == 1 then first player, if 2 second player
turn = 1

place_tokens_at_start()

get_index_of_Cell()

# loading dice images
load_dice_images()

show_board()
window.mainloop()