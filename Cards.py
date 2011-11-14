# using Tkinter to display a hand of 5 random card images
# each time you click the canvas
# (images are in GIF format for Tkinter to display properly)

from Tkinter import *
import random
import os

root = Tk()
root.title("Click me!")
os.chdir("Images")

def create_cards():
    """
    create a list of 52 cards
    suit: club=C, diamond=D, heart=H spade=S
    rank: ace=A, 10=T, jack=J, queen=Q, king=K, numbers=2..9
    ace of spade would be SA, 8 of heart would be H8 and so on ...
    """
    return [ suit + rank for suit in "CDHS" for rank in "A23456789TJQK" ]

def shuffle_cards(card_list):
    """random shuffle a list of cards"""
    # make a copy of the original list
    card_list1 = card_list[:]
    random.shuffle(card_list1)
    return card_list1

def pick_5cards(card_list):
    """pick five cards from the shuffled list"""
    return card_list[:5]

def create_images():
    """create all card images as a card_name:image_object dictionary"""
    card_list = create_cards()
    image_dict = {}
    for card in card_list:

        # all images have filenames the match the card_list names + extension .gif
        image_dict[card] = PhotoImage(file = card + ".gif")

    return image_dict

def next_hand(event):
    """create the card list, shuffle, pick five cards and display them"""
    deck = create_cards()
    shuffled_cards = shuffle_cards(deck)
    card_list = pick_5cards(shuffled_cards)
    root.title(shuffled_cards)  # test

    # now display the card images at the proper location on the canvas
    x = canvas1.winfo_width() / 7
    y = 10
    hor_count = 0
    ver_count = 0

    canvas1.delete(ALL)

    for card in shuffled_cards:

        if hor_count < 6:
            ver_count = 0
            hor_count += 1
            x += canvas1.winfo_width() / 7
            y = 10

        if ver_count < 6:
        #if x < canvas1.winfo_width() - image_dict[card].width():
            canvas1.create_image(x, y, image = image_dict[card], anchor = NE)

            # calculate each NW corner x, y
            y += 25
            ver_count += 1

        hor_count += 1

   # load a sample card to get the size
photo1 = PhotoImage(file = "C2.gif")

# make canvas 5 times the width of a card + 100
#width1 = 5 * photo1.width() + 100
#height1 = photo1.height() + 20
canvas1 = Canvas(root, width = 1440, height = 900)
canvas1.pack(expand = 1, fill = BOTH)

# now load all card images into a dictionary
image_dict = create_images()

# bind left mouse click on canvas to next_hand display
canvas1.bind('<Button-1>', next_hand)

root.mainloop()
