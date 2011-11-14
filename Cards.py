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
    card_list = create_cards()
    card_list = shuffle_cards(card_list)
    card_list = pick_5cards(card_list)
    root.title(card_list)  # test

    # now display the card images at the proper location on the canvas
    x = 10
    y = 10
    for card in card_list:

        #print card, x, y  # test
        canvas1.create_image(x, y, image = image_dict[card], anchor = NW)

        # calculate each NW corner x, y
        x += 90

# load a sample card to get the size
photo1 = PhotoImage(file = "C2.gif")

# make canvas 5 times the width of a card + 100
width1 = 5 * photo1.width() + 100
height1 = photo1.height() + 20
canvas1 = Canvas(width = width1, height = height1)
canvas1.pack()

# now load all card images into a dictionary
image_dict = create_images()

# bind left mouse click on canvas to next_hand display
canvas1.bind('<Button-1>', next_hand)

root.mainloop()
