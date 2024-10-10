from tkinter import *
from functools import partial
import random

# Initializing the main windows and getting info about the screen height and width
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
new = Tk()

# List of all possible options
opt = ["Rock", "Paper", "Scissors"]

def main():
    # Starting the main window
    new.withdraw()
    root.geometry("%dx%d" % (width, height))
    root.title("Rock, Paper, Scissors")
    root.state("zoomed")

    # Closing button
    closeframe = Frame(root)
    closeframe.place(x = 1, y = 1)
    closebutton = Button(closeframe,
                         text = "X Close",
                         font = ("Arial Greek", int(width/80)),
                         foreground = "red4",
                         cursor = "mouse",
                         command= root.quit)
    closebutton.pack()

    # Starting text
    lb1 = Label(root,
                text= "Rock, Paper Or Scissors?",
                font = ("Century", int(width/20)),
                foreground = "lightskyblue4")
    lb1.place(x = int(width/8), y = int(height/50))

    # 3 buttons
    bt1 = Button(root,
                 text = "Rock",
                 font = ("Constantia", int(width/60)),
                 foreground = "royalblue4",
                 width = int(width/70),
                 cursor = "mouse",
                 command = rock)
    bt1.place(x = int(width/25), y = int(height/1.5))
    bt2 = Button(root,
                 text = "Paper",
                 font = ("Constantia", int(width/60)),
                 foreground = "royalblue4",
                 width = int(width/70),
                 cursor = "mouse",
                 command = paper)
    bt2.place(x = int(width/2.6), y = int(height/1.5))
    bt3 = Button(root,
                 text = "Scissors",
                 font = ("Constantia", int(width/60)),
                 foreground = "royalblue4",
                 width = int(width/70),
                 cursor = "mouse",
                 command = scissors)
    bt3.place(x = int(width/1.4), y = int(height/1.5))

    root.mainloop()

def back(this, previous):
    this.withdraw()
    previous.deiconify()
    previous.state("zoomed")

def rock():
    # Close last window and open new one
    root.withdraw()
    new = Tk()
    new.geometry("%dx%d" % (width, height))
    new.title("Rock, Paper, Scissors")
    new.state("zoomed")

    comp = random.choice(opt)

    # Top text stating who chose what
    textframe = Frame(new)
    textframe.place(x = int(width/10), y = int(height/15))
    lb1 = Label(textframe,
                text= "You Chose Rock, Computer Chose %s" %comp,
                font = ("Century", int(width/30)),
                foreground = "lightskyblue4")
    lb1.pack()

    # Function call to determine winner and print
    win = winner("Rock", comp)
    textframe2 = Frame(new)
    textframe2.place(x = int(width/2.4), y = int(height/4))
    lb2 = Label(textframe2,
                text = "%s" %win,
                font = ("Century", int(width/30)),
                foreground = "springgreen4")
    lb2.pack(expand = True)

    # Play again or no
    lb3 = Label(new,
                text = "Do You Want To Play Again?",
                font = ("Century", int(width/30)),
                foreground = "lightskyblue4")
    lb3.place(x = int(width/5), y = int(height/2))
    bt1 = Button(new,
                text = "Yes",
                font = ("Arial Greek", int(width/60)),
                width = int(width/70),
                foreground = "ivory4",
                cursor = "mouse",
                command= partial(back, new, root))
    bt1.place(x = int(width/5), y = int(height/1.5)) 
    bt2 = Button(new,
                text = "No",
                font = ("Arial Greek", int(width/60)),
                width = int(width/70),
                foreground = "ivory4",
                cursor = "mouse",
                command= new.quit)
    bt2.place(x = int(width/1.8), y = int(height/1.5)) 

def paper():
    # Close last window and open new one
    root.withdraw()
    new = Tk()
    new.geometry("%dx%d" % (width, height))
    new.title("Rock, Paper, Scissors")
    new.state("zoomed")

    comp = random.choice(opt)

    # Top text stating who chose what
    textframe = Frame(new)
    textframe.place(x = int(width/10), y = int(height/15))
    lb1 = Label(textframe,
                text= "You Chose Paper, Computer Chose %s" %comp,
                font = ("Century", int(width/30)),
                foreground = "lightskyblue4")
    lb1.pack()

    # Function call to determine winner and print
    win = winner("Paper", comp)
    textframe2 = Frame(new)
    textframe2.place(x = int(width/2.4), y = int(height/4))
    lb2 = Label(textframe2,
                text = "%s" %win,
                font = ("Century", int(width/30)),
                foreground = "springgreen4")
    lb2.pack(expand = True)

    # Play again or no
    lb3 = Label(new,
                text = "Do You Want To Play Again?",
                font = ("Century", int(width/30)),
                foreground = "lightskyblue4")
    lb3.place(x = int(width/5), y = int(height/2))
    bt1 = Button(new,
                text = "Yes",
                font = ("Arial Greek", int(width/60)),
                width = int(width/70),
                foreground = "ivory4",
                cursor = "mouse",
                command= partial(back, new, root))
    bt1.place(x = int(width/5), y = int(height/1.5)) 
    bt2 = Button(new,
                text = "No",
                font = ("Arial Greek", int(width/60)),
                width = int(width/70),
                foreground = "ivory4",
                cursor = "mouse",
                command= new.quit)
    bt2.place(x = int(width/1.8), y = int(height/1.5)) 

def scissors():
    # Close last window and open new one
    root.withdraw()
    new = Tk()
    new.geometry("%dx%d" % (width, height))
    new.title("Rock, Paper, Scissors")
    new.state("zoomed")

    comp = random.choice(opt)

    # Top text stating who chose what
    textframe = Frame(new)
    textframe.place(x = int(width/20), y = int(height/15))
    lb1 = Label(textframe,
                text= "You Chose Scissors, Computer Chose %s" %comp,
                font = ("Century", int(width/30)),
                foreground = "lightskyblue4")
    lb1.pack()

    # Function call to determine winner and print
    win = winner("Scissors", comp)
    textframe2 = Frame(new)
    textframe2.place(x = int(width/2.4), y = int(height/4))
    lb2 = Label(textframe2,
                text = "%s" %win,
                font = ("Century", int(width/30)),
                foreground = "springgreen4")
    lb2.pack(expand = True)
    # Play again or no
    lb3 = Label(new,
                text = "Do You Want To Play Again?",
                font = ("Century", int(width/30)),
                foreground = "lightskyblue4")
    lb3.place(x = int(width/5), y = int(height/2))
    bt1 = Button(new,
                text = "Yes",
                font = ("Arial Greek", int(width/60)),
                width = int(width/70),
                foreground = "ivory4",
                cursor = "mouse",
                command= partial(back, new, root))
    bt1.place(x = int(width/5), y = int(height/1.5)) 
    bt2 = Button(new,
                text = "No",
                font = ("Arial Greek", int(width/60)),
                width = int(width/70),
                foreground = "ivory4",
                cursor = "mouse",
                command= new.quit)
    bt2.place(x = int(width/1.8), y = int(height/1.5)) 
    
def winner(user, comp):
    if user == comp:
        return("It's a tie!")
    elif user == opt[0] and comp == opt[1]:
        return("Computer wins")
    elif user == opt[0] and comp == opt[2]:
        return("You win")
    elif user == opt[1] and comp == opt[0]:
        return("You win")
    elif user == opt[1] and comp == opt[2]:
        return("Computer wins")
    elif user == opt[2] and comp == opt[0]:
        return("Computer wins")
    elif user == opt[2] and comp == opt[1]:
        return("You win")

if __name__ == "__main__":
    main()