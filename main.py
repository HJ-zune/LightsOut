from tkinter import *
import random
#NOTE: major flaw in the code is the cells start from 1, 1 rather than 0, 0 and with the row variable
#only the columns index from 0
root = Tk()
root.title('Lights Out!')
root.geometry('950x800')
root.iconbitmap('LightBulb_Icon.ico')
root.configure(bg='light blue')
root.resizable(False, False)

#victory
def win():
    victory = Toplevel(root)
    victory.title('Congratulations!!!')
    victory.iconbitmap('LightBulb_Icon.ico')
    victory.geometry('300x200')
    victory.configure(bg='gold')
    victory.resizable(False, False)
    victorylabel = Label(victory, anchor='center', font=('Ariel', 15), bg='gold',
                         text='\n\n You Win! \n Would you like to play again?')
    victorylabel.pack()
    playagain = Button(victory, anchor='center', padx=50, pady=25, bg='light grey', text='Play again',
                       command=lightreset)
    playagain.pack()
    victoryquit = Button(victory, anchor='center', padx=50, pady=25, bg='light grey', text='Exit', command=root.quit)
    victoryquit.pack()

#rows
row1 = [0, 0, 0, 0, 0]
row2 = [0, 0, 0, 0, 0]
row3 = [0, 0, 0, 0, 0]
row4 = [0, 0, 0, 0, 0]
row5 = [0, 0, 0, 0, 0]
clickcount = 0

#description, title, whitespace, gamestate and clickcount labels
description = Label(padx=50, pady=50, bg='light blue', font=('Arial', 9), justify='left',
                    text='The rules of the game are simple:\n'
                    'By clicking on any of the light bulbs, the light bulb you click \nand all '
                    'adjacent light bulbs will switch state. meaning if they were previously on \n'
                    'they will turn off and vice versa.\n\nThe end goal:\nTurn all the lights on!')
description.grid(columnspan=5, column=1, row=6)

title = Label(padx=100, pady=20, bg='light blue', fg='gold', font=('Verdana', 30), text='Lights Out!')
title.grid(columnspan=2, column=6, row=1)

whitespace = Label(bg='light blue', font=('Arial', 1), text='')
whitespace.grid(columnspan=7, column=0, row=0)
whitespace2 = Label(bg='light blue', text='')
whitespace2.grid(rowspan=4, column=0, row=0)

gamestate = Label(bg='light blue', font=('Arial', 9), text=str(row1) + '\n' + str(row2) + '\n' + str(row3)
                   + '\n' + str(row4) + '\n' + str(row5))
gamestate.grid(columnspan=2, column=6, row=2)

clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
clickcounter.grid(columnspan=2, column=6, row=3)


#scramble
def scramble():
    global count
    global clickcount
    count = 0
    while count < 50:
        r = random.randint(1, 25)
        if r == 1:
            click1()
        if r == 2:
            click2()
        if r == 3:
            click3()
        if r == 4:
            click4()
        if r == 5:
            click5()
        if r == 6:
            click6()
        if r == 7:
            click7()
        if r == 8:
            click8()
        if r == 9:
            click9()
        if r == 10:
            click10()
        if r == 11:
            click11()
        if r == 12:
            click12()
        if r == 13:
            click13()
        if r == 14:
            click14()
        if r == 15:
            click15()
        if r == 16:
            click16()
        if r == 17:
            click17()
        if r == 18:
            click18()
        if r == 19:
            click19()
        if r == 20:
            click20()
        if r == 21:
            click21()
        if r == 22:
            click22()
        if r == 23:
            click23()
        if r == 24:
            click24()
        if r == 25:
            click25()
        clickcount = 0
        clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
        clickcounter.grid(columnspan=2, column=6, row=3)
        count += 1

#reset state
def lightreset():
    global light1
    global light2
    global light3
    global light4
    global light5
    global light6
    global light7
    global light8
    global light9
    global light10
    global light11
    global light12
    global light13
    global light14
    global light15
    global light16
    global light17
    global light18
    global light19
    global light20
    global light21
    global light22
    global light23
    global light24
    global light25

    global row1
    global row2
    global row3
    global row4
    global row5
    global clickcount

    light1.grid_forget()
    light2.grid_forget()
    light3.grid_forget()
    light4.grid_forget()
    light5.grid_forget()
    light6.grid_forget()
    light7.grid_forget()
    light8.grid_forget()
    light9.grid_forget()
    light10.grid_forget()
    light11.grid_forget()
    light12.grid_forget()
    light13.grid_forget()
    light14.grid_forget()
    light15.grid_forget()
    light16.grid_forget()
    light17.grid_forget()
    light18.grid_forget()
    light19.grid_forget()
    light20.grid_forget()
    light21.grid_forget()
    light22.grid_forget()
    light23.grid_forget()
    light24.grid_forget()
    light25.grid_forget()

    light1 = Button(padx=50, pady=50, bg='light grey', command=click1)
    light1.grid(column=1, row=1)
    light2 = Button(padx=50, pady=50, bg='light grey', command=click2)
    light2.grid(column=2, row=1)
    light3 = Button(padx=50, pady=50, bg='light grey', command=click3)
    light3.grid(column=3, row=1)
    light4 = Button(padx=50, pady=50, bg='light grey', command=click4)
    light4.grid(column=4, row=1)
    light5 = Button(padx=50, pady=50, bg='light grey', command=click5)
    light5.grid(column=5, row=1)
    light6 = Button(padx=50, pady=50, bg='light grey', command=click6)
    light6.grid(column=1, row=2)
    light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
    light7.grid(column=2, row=2)
    light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
    light8.grid(column=3, row=2)
    light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
    light9.grid(column=4, row=2)
    light10 = Button(padx=50, pady=50, bg='light grey', command=click10)
    light10.grid(column=5, row=2)
    light11 = Button(padx=50, pady=50, bg='light grey', command=click11)
    light11.grid(column=1, row=3)
    light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
    light12.grid(column=2, row=3)
    light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
    light13.grid(column=3, row=3)
    light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
    light14.grid(column=4, row=3)
    light15 = Button(padx=50, pady=50, bg='light grey', command=click15)
    light15.grid(column=5, row=3)
    light16 = Button(padx=50, pady=50, bg='light grey', command=click16)
    light16.grid(column=1, row=4)
    light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
    light17.grid(column=2, row=4)
    light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
    light18.grid(column=3, row=4)
    light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
    light19.grid(column=4, row=4)
    light20 = Button(padx=50, pady=50, bg='light grey', command=click20)
    light20.grid(column=5, row=4)
    light21 = Button(padx=50, pady=50, bg='light grey', command=click21)
    light21.grid(column=1, row=5)
    light22 = Button(padx=50, pady=50, bg='light grey', command=click22)
    light22.grid(column=2, row=5)
    light23 = Button(padx=50, pady=50, bg='light grey', command=click23)
    light23.grid(column=3, row=5)
    light24 = Button(padx=50, pady=50, bg='light grey', command=click24)
    light24.grid(column=4, row=5)
    light25 = Button(padx=50, pady=50, bg='light grey', command=click25)
    light25.grid(column=5, row=5)

    row1 = [0, 0, 0, 0, 0]
    row2 = [0, 0, 0, 0, 0]
    row3 = [0, 0, 0, 0, 0]
    row4 = [0, 0, 0, 0, 0]
    row5 = [0, 0, 0, 0, 0]

    whitespace = Label(bg='light blue', font=('Arial', 9), text=str(row1) + '\n' + str(row2) + '\n' + str(row3)
                                                                + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    clickcount = 0
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

#reset, quit and scramble buttons
button_quit = Button(padx=50, pady=25, bg='light grey', text='Quit', command=root.quit)
button_quit.grid(column=6, row=6)
button_reset = Button(padx=50, pady=25, bg='light grey', text='Reset', command=lightreset)
button_reset.grid(column=7, row=6)
button_scramble = Button(padx=100, pady=25, bg='light grey', text='Scramble!', command=scramble)
button_scramble.grid(columnspan=2, column=6, row=5)

#defining clicks
def click1(): #TOP LEFT
    global light1
    global light2
    global light6

    light1.grid_forget()
    light2.grid_forget()
    light6.grid_forget()

    if row1[0] == 0:
        row1[0] = 1
        light1 = Button(padx=50, pady=50, bg='gold', command=click1)
        light1.grid(column=1, row=1)

    elif row1[0] != 0:
        row1[0] = 0
        light1 = Button(padx=50, pady=50, bg='light grey', command=click1)
        light1.grid(column=1, row=1)

    if row1[1] == 0:
        row1[1] = 1
        light2 = Button(padx=50, pady=50, bg='gold', command=click2)
        light2.grid(column=2, row=1)

    elif row1[1] != 0:
        row1[1] = 0
        light2 = Button(padx=50, pady=50, bg='light grey', command=click2)
        light2.grid(column=2, row=1)

    if row2[0] == 0:
        row2[0] = 1
        light6 = Button(padx=50, pady=50, bg='gold', command=click6)
        light6.grid(column=1, row=2)

    elif row2[0] != 0:
        row2[0] = 0
        light6 = Button(padx=50, pady=50, bg='light grey', command=click6)
        light6.grid(column=1, row=2)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click2():
    global light2
    global light1
    global light7
    global light3

    light2.grid_forget()
    light1.grid_forget()
    light7.grid_forget()
    light3.grid_forget()

    if row1[1] == 0:
        row1[1] = 1
        light2 = Button(padx=50, pady=50, bg='gold', command=click2)
        light2.grid(column=2, row=1)

    elif row1[1] != 0:
        row1[1] = 0
        light2 = Button(padx=50, pady=50, bg='light grey', command=click2)
        light2.grid(column=2, row=1)

    if row1[0] == 0:
        row1[0] = 1
        light1 = Button(padx=50, pady=50, bg='gold', command=click1)
        light1.grid(column=1, row=1)

    elif row1[0] != 0:
        row1[0] = 0
        light1 = Button(padx=50, pady=50, bg='light grey', command=click1)
        light1.grid(column=1, row=1)

    if row2[1] == 0:
        row2[1] = 1
        light7 = Button(padx=50, pady=50, bg='gold', command=click7)
        light7.grid(column=2, row=2)

    elif row2[1] != 0:
        row2[1] = 0
        light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
        light7.grid(column=2, row=2)
    if row1[2] == 0:
        row1[2] = 1
        light3 = Button(padx=50, pady=50, bg='gold', command=click3)
        light3.grid(column=3, row=1)

    elif row1[2] != 0:
        row1[2] = 0
        light3 = Button(padx=50, pady=50, bg='light grey', command=click3)
        light3.grid(column=3, row=1)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click3(): #top
    global light3
    global light2
    global light8
    global light4

    light3.grid_forget()
    light2.grid_forget()
    light8.grid_forget()
    light4.grid_forget()

    if row1[2] == 0:
        row1[2] = 1
        light3 = Button(padx=50, pady=50, bg='gold', command=click3)
        light3.grid(column=3, row=1)

    elif row1[2] != 0:
        row1[2] = 0
        light3 = Button(padx=50, pady=50, bg='light grey', command=click3)
        light3.grid(column=3, row=1)

    if row1[1] == 0:
        row1[1] = 1
        light2 = Button(padx=50, pady=50, bg='gold', command=click2)
        light2.grid(column=2, row=1)

    elif row1[1] != 0:
        row1[1] = 0
        light2 = Button(padx=50, pady=50, bg='light grey', command=click2)
        light2.grid(column=2, row=1)

    if row2[2] == 0:
        row2[2] = 1
        light8 = Button(padx=50, pady=50, bg='gold', command=click8)
        light8.grid(column=3, row=2)

    elif row2[2] != 0:
        row2[2] = 0
        light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
        light8.grid(column=3, row=2)
    if row1[3] == 0:
        row1[3] = 1
        light4 = Button(padx=50, pady=50, bg='gold', command=click4)
        light4.grid(column=4, row=1)

    elif row1[3] != 0:
        row1[3] = 0
        light4 = Button(padx=50, pady=50, bg='light grey', command=click4)
        light4.grid(column=4, row=1)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click4():
    global light4
    global light3
    global light9
    global light5

    light4.grid_forget()
    light3.grid_forget()
    light9.grid_forget()
    light5.grid_forget()

    if row1[3] == 0:
        row1[3] = 1
        light4 = Button(padx=50, pady=50, bg='gold', command=click4)
        light4.grid(column=4, row=1)

    elif row1[3] != 0:
        row1[3] = 0
        light4 = Button(padx=50, pady=50, bg='light grey', command=click4)
        light4.grid(column=4, row=1)

    if row1[2] == 0:
        row1[2] = 1
        light3 = Button(padx=50, pady=50, bg='gold', command=click3)
        light3.grid(column=3, row=1)

    elif row1[2] != 0:
        row1[2] = 0
        light3 = Button(padx=50, pady=50, bg='light grey', command=click3)
        light3.grid(column=3, row=1)

    if row2[3] == 0:
        row2[3] = 1
        light9 = Button(padx=50, pady=50, bg='gold', command=click9)
        light9.grid(column=4, row=2)

    elif row2[3] != 0:
        row2[3] = 0
        light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
        light9.grid(column=4, row=2)

    if row1[4] == 0:
        row1[4] = 1
        light5 = Button(padx=50, pady=50, bg='gold', command=click5)
        light5.grid(column=5, row=1)

    elif row1[4] != 0:
        row1[4] = 0
        light5 = Button(padx=50, pady=50, bg='light grey', command=click5)
        light5.grid(column=5, row=1)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click5():
    global light5
    global light4
    global light10

    light5.grid_forget()
    light4.grid_forget()
    light10.grid_forget()

    if row1[4] == 0:
        row1[4] = 1
        light5 = Button(padx=50, pady=50, bg='gold', command=click5)
        light5.grid(column=5, row=1)

    elif row1[4] != 0:
        row1[4] = 0
        light5 = Button(padx=50, pady=50, bg='light grey', command=click5)
        light5.grid(column=5, row=1)

    if row1[3] == 0:
        row1[3] = 1
        light4 = Button(padx=50, pady=50, bg='gold', command=click4)
        light4.grid(column=4, row=1)

    elif row1[3] != 0:
        row1[3] = 0
        light4 = Button(padx=50, pady=50, bg='light grey', command=click4)
        light4.grid(column=4, row=1)

    if row2[4] == 0:
        row2[4] = 1
        light10 = Button(padx=50, pady=50, bg='gold', command=click10)
        light10.grid(column=5, row=2)

    elif row2[4] != 0:
        row2[4] = 0
        light10 = Button(padx=50, pady=50, bg='light grey', command=click10)
        light10.grid(column=5, row=2)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click6():
    global light6
    global light1
    global light7
    global light11

    light6.grid_forget()
    light1.grid_forget()
    light7.grid_forget()
    light11.grid_forget()

    if row2[0] == 0:
        row2[0] = 1
        light6 = Button(padx=50, pady=50, bg='gold', command=click6)
        light6.grid(column=1, row=2)

    elif row2[0] != 0:
        row2[0] = 0
        light6 = Button(padx=50, pady=50, bg='light grey', command=click6)
        light6.grid(column=1, row=2)

    if row1[0] == 0:
        row1[0] = 1
        light1 = Button(padx=50, pady=50, bg='gold', command=click1)
        light1.grid(column=1, row=1)

    elif row1[0] != 0:
        row1[0] = 0
        light1 = Button(padx=50, pady=50, bg='light grey', command=click1)
        light1.grid(column=1, row=1)

    if row2[1] == 0:
        row2[1] = 1
        light7 = Button(padx=50, pady=50, bg='gold', command=click7)
        light7.grid(column=2, row=2)

    elif row2[1] != 0:
        row2[1] = 0
        light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
        light7.grid(column=2, row=2)

    if row3[0] == 0:
        row3[0] = 1
        light11 = Button(padx=50, pady=50, bg='gold', command=click11)
        light11.grid(column=1, row=3)

    elif row3[0] != 0:
        row3[0] = 0
        light11 = Button(padx=50, pady=50, bg='light grey', command=click11)
        light11.grid(column=1, row=3)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click7():
    global light7
    global light2
    global light8
    global light12
    global light6

    light7.grid_forget()
    light2.grid_forget()
    light8.grid_forget()
    light12.grid_forget()
    light6.grid_forget()

    if row2[1] == 0:
        row2[1] = 1
        light7 = Button(padx=50, pady=50, bg='gold', command=click7)
        light7.grid(column=2, row=2)

    elif row2[1] != 0:
        row2[1] = 0
        light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
        light7.grid(column=2, row=2)

    if row1[1] == 0:
        row1[1] = 1
        light2 = Button(padx=50, pady=50, bg='gold', command=click2)
        light2.grid(column=2, row=1)

    elif row1[1] != 0:
        row1[1] = 0
        light2 = Button(padx=50, pady=50, bg='light grey', command=click2)
        light2.grid(column=2, row=1)

    if row2[2] == 0:
        row2[2] = 1
        light8 = Button(padx=50, pady=50, bg='gold', command=click8)
        light8.grid(column=3, row=2)

    elif row2[2] != 0:
        row2[2] = 0
        light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
        light8.grid(column=3, row=2)

    if row3[1] == 0:
        row3[1] = 1
        light12 = Button(padx=50, pady=50, bg='gold', command=click12)
        light12.grid(column=2, row=3)

    elif row3[1] != 0:
        row3[1] = 0
        light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
        light12.grid(column=2, row=3)

    if row2[0] == 0:
        row2[0] = 1
        light6 = Button(padx=50, pady=50, bg='gold', command=click6)
        light6.grid(column=1, row=2)

    elif row2[0] != 0:
        row2[0] = 0
        light6 = Button(padx=50, pady=50, bg='light grey', command=click6)
        light6.grid(column=1, row=2)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click8():
    global light8
    global light3
    global light9
    global light13
    global light7

    light8.grid_forget()
    light3.grid_forget()
    light9.grid_forget()
    light13.grid_forget()
    light7.grid_forget()

    if row2[2] == 0:
        row2[2] = 1
        light8 = Button(padx=50, pady=50, bg='gold', command=click8)
        light8.grid(column=3, row=2)

    elif row2[2] != 0:
        row2[2] = 0
        light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
        light8.grid(column=3, row=2)

    if row1[2] == 0:
        row1[2] = 1
        light3 = Button(padx=50, pady=50, bg='gold', command=click3)
        light3.grid(column=3, row=1)

    elif row1[2] != 0:
        row1[2] = 0
        light3 = Button(padx=50, pady=50, bg='light grey', command=click3)
        light3.grid(column=3, row=1)

    if row2[3] == 0:
        row2[3] = 1
        light9 = Button(padx=50, pady=50, bg='gold', command=click9)
        light9.grid(column=4, row=2)

    elif row2[3] != 0:
        row2[3] = 0
        light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
        light9.grid(column=4, row=2)

    if row3[2] == 0:
        row3[2] = 1
        light13 = Button(padx=50, pady=50, bg='gold', command=click13)
        light13.grid(column=3, row=3)

    elif row3[2] != 0:
        row3[2] = 0
        light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
        light13.grid(column=3, row=3)

    if row2[1] == 0:
        row2[1] = 1
        light7 = Button(padx=50, pady=50, bg='gold', command=click7)
        light7.grid(column=2, row=2)

    elif row2[1] != 0:
        row2[1] = 0
        light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
        light7.grid(column=2, row=2)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click9():
    global light9
    global light4
    global light10
    global light14
    global light8

    light9.grid_forget()
    light4.grid_forget()
    light10.grid_forget()
    light14.grid_forget()
    light8.grid_forget()

    if row2[3] == 0:
        row2[3] = 1
        light9 = Button(padx=50, pady=50, bg='gold', command=click9)
        light9.grid(column=4, row=2)

    elif row2[3] != 0:
        row2[3] = 0
        light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
        light9.grid(column=4, row=2)

    if row1[3] == 0:
        row1[3] = 1
        light4 = Button(padx=50, pady=50, bg='gold', command=click4)
        light4.grid(column=4, row=1)

    elif row1[3] != 0:
        row1[3] = 0
        light4 = Button(padx=50, pady=50, bg='light grey', command=click4)
        light4.grid(column=4, row=1)

    if row2[4] == 0:
        row2[4] = 1
        light10 = Button(padx=50, pady=50, bg='gold', command=click10)
        light10.grid(column=5, row=2)

    elif row2[4] != 0:
        row2[4] = 0
        light10 = Button(padx=50, pady=50, bg='light grey', command=click10)
        light10.grid(column=5, row=2)

    if row3[3] == 0:
        row3[3] = 1
        light14 = Button(padx=50, pady=50, bg='gold', command=click14)
        light14.grid(column=4, row=3)

    elif row3[3] != 0:
        row3[3] = 0
        light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
        light14.grid(column=4, row=3)

    if row2[2] == 0:
        row2[2] = 1
        light8 = Button(padx=50, pady=50, bg='gold', command=click8)
        light8.grid(column=3, row=2)

    elif row2[2] != 0:
        row2[2] = 0
        light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
        light8.grid(column=3, row=2)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click10():
    global light10
    global light5
    global light9
    global light15

    light10.grid_forget()
    light5.grid_forget()
    light9.grid_forget()
    light15.grid_forget()

    if row2[4] == 0:
        row2[4] = 1
        light10 = Button(padx=50, pady=50, bg='gold', command=click10)
        light10.grid(column=5, row=2)

    elif row2[4] != 0:
        row2[4] = 0
        light10 = Button(padx=50, pady=50, bg='light grey', command=click10)
        light10.grid(column=5, row=2)

    if row1[4] == 0:
        row1[4] = 1
        light5 = Button(padx=50, pady=50, bg='gold', command=click5)
        light5.grid(column=5, row=1)

    elif row1[4] != 0:
        row1[4] = 0
        light5 = Button(padx=50, pady=50, bg='light grey', command=click5)
        light5.grid(column=5, row=1)

    if row2[3] == 0:
        row2[3] = 1
        light9 = Button(padx=50, pady=50, bg='gold', command=click9)
        light9.grid(column=4, row=2)

    elif row2[3] != 0:
        row2[3] = 0
        light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
        light9.grid(column=4, row=2)

    if row3[4] == 0:
        row3[4] = 1
        light15 = Button(padx=50, pady=50, bg='gold', command=click15)
        light15.grid(column=5, row=3)

    elif row3[4] != 0:
        row3[4] = 0
        light15 = Button(padx=50, pady=50, bg='light grey', command=click15)
        light15.grid(column=5, row=3)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click11(): #left
    global light11
    global light6
    global light12
    global light16

    light11.grid_forget()
    light6.grid_forget()
    light12.grid_forget()
    light16.grid_forget()

    if row3[0] == 0:
        row3[0] = 1
        light11 = Button(padx=50, pady=50, bg='gold', command=click11)
        light11.grid(column=1, row=3)

    elif row3[0] != 0:
        row3[0] = 0
        light11 = Button(padx=50, pady=50, bg='light grey', command=click11)
        light11.grid(column=1, row=3)

    if row2[0] == 0:
        row2[0] = 1
        light6 = Button(padx=50, pady=50, bg='gold', command=click6)
        light6.grid(column=1, row=2)

    elif row2[0] != 0:
        row2[0] = 0
        light6 = Button(padx=50, pady=50, bg='light grey', command=click6)
        light6.grid(column=1, row=2)

    if row3[1] == 0:
        row3[1] = 1
        light12 = Button(padx=50, pady=50, bg='gold', command=click12)
        light12.grid(column=2, row=3)

    elif row3[1] != 0:
        row3[1] = 0
        light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
        light12.grid(column=2, row=3)

    if row4[0] == 0:
        row4[0] = 1
        light16 = Button(padx=50, pady=50, bg='gold', command=click16)
        light16.grid(column=1, row=4)

    elif row4[0] != 0:
        row4[0] = 0
        light16 = Button(padx=50, pady=50, bg='light grey', command=click16)
        light16.grid(column=1, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click12():
    global light12
    global light7
    global light13
    global light17
    global light11

    light12.grid_forget()
    light7.grid_forget()
    light13.grid_forget()
    light17.grid_forget()
    light11.grid_forget()

    if row3[1] == 0:
        row3[1] = 1
        light12 = Button(padx=50, pady=50, bg='gold', command=click12)
        light12.grid(column=2, row=3)

    elif row3[1] != 0:
        row3[1] = 0
        light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
        light12.grid(column=2, row=3)

    if row2[1] == 0:
        row2[1] = 1
        light7 = Button(padx=50, pady=50, bg='gold', command=click7)
        light7.grid(column=2, row=2)

    elif row2[1] != 0:
        row2[1] = 0
        light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
        light7.grid(column=2, row=2)

    if row3[2] == 0:
        row3[2] = 1
        light13 = Button(padx=50, pady=50, bg='gold', command=click13)
        light13.grid(column=3, row=3)

    elif row3[2] != 0:
        row3[2] = 0
        light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
        light13.grid(column=3, row=3)

    if row4[1] == 0:
        row4[1] = 1
        light17 = Button(padx=50, pady=50, bg='gold', command=click17)
        light17.grid(column=2, row=4)

    elif row4[1] != 0:
        row4[1] = 0
        light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
        light17.grid(column=2, row=4)

    if row3[0] == 0:
        row3[0] = 1
        light11 = Button(padx=50, pady=50, bg='gold', command=click11)
        light11.grid(column=1, row=3)

    elif row3[0] != 0:
        row3[0] = 0
        light11 = Button(padx=50, pady=50, bg='light grey', command=click11)
        light11.grid(column=1, row=3)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click13(): #mid
    global light13
    global light8
    global light14
    global light18
    global light12

    light13.grid_forget()
    light8.grid_forget()
    light14.grid_forget()
    light18.grid_forget()
    light12.grid_forget()

    if row3[2] == 0:
        row3[2] = 1
        light13 = Button(padx=50, pady=50, bg='gold', command=click13)
        light13.grid(column=3, row=3)

    elif row3[2] != 0:
        row3[2] = 0
        light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
        light13.grid(column=3, row=3)

    if row2[2] == 0:
        row2[2] = 1
        light8 = Button(padx=50, pady=50, bg='gold', command=click8)
        light8.grid(column=3, row=2)

    elif row2[2] != 0:
        row2[2] = 0
        light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
        light8.grid(column=3, row=2)

    if row3[3] == 0:
        row3[3] = 1
        light14 = Button(padx=50, pady=50, bg='gold', command=click14)
        light14.grid(column=4, row=3)

    elif row3[3] != 0:
        row3[3] = 0
        light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
        light14.grid(column=4, row=3)

    if row4[2] == 0:
        row4[2] = 1
        light18 = Button(padx=50, pady=50, bg='gold', command=click18)
        light18.grid(column=3, row=4)

    elif row4[2] != 0:
        row4[2] = 0
        light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
        light18.grid(column=3, row=4)

    if row3[1] == 0:
        row3[1] = 1
        light12 = Button(padx=50, pady=50, bg='gold', command=click12)
        light12.grid(column=2, row=3)

    elif row3[1] != 0:
        row3[1] = 0
        light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
        light12.grid(column=2, row=3)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click14():
    global light14
    global light9
    global light15
    global light19
    global light13

    light14.grid_forget()
    light9.grid_forget()
    light15.grid_forget()
    light19.grid_forget()
    light13.grid_forget()

    if row3[3] == 0:
        row3[3] = 1
        light14 = Button(padx=50, pady=50, bg='gold', command=click14)
        light14.grid(column=4, row=3)

    elif row3[3] != 0:
        row3[3] = 0
        light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
        light14.grid(column=4, row=3)

    if row2[3] == 0:
        row2[3] = 1
        light9 = Button(padx=50, pady=50, bg='gold', command=click9)
        light9.grid(column=4, row=2)

    elif row2[3] != 0:
        row2[3] = 0
        light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
        light9.grid(column=4, row=2)

    if row3[4] == 0:
        row3[4] = 1
        light15 = Button(padx=50, pady=50, bg='gold', command=click15)
        light15.grid(column=5, row=3)

    elif row3[4] != 0:
        row3[4] = 0
        light15 = Button(padx=50, pady=50, bg='light grey', command=click15)
        light15.grid(column=5, row=3)

    if row4[3] == 0:
        row4[3] = 1
        light19 = Button(padx=50, pady=50, bg='gold', command=click19)
        light19.grid(column=4, row=4)

    elif row4[3] != 0:
        row4[3] = 0
        light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
        light19.grid(column=4, row=4)

    if row3[2] == 0:
        row3[2] = 1
        light13 = Button(padx=50, pady=50, bg='gold', command=click13)
        light13.grid(column=3, row=3)

    elif row3[2] != 0:
        row3[2] = 0
        light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
        light13.grid(column=3, row=3)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click15(): #right
    global light15
    global light10
    global light14
    global light20

    light15.grid_forget()
    light10.grid_forget()
    light14.grid_forget()
    light20.grid_forget()

    if row3[4] == 0:
        row3[4] = 1
        light15 = Button(padx=50, pady=50, bg='gold', command=click15)
        light15.grid(column=5, row=3)

    elif row3[4] != 0:
        row3[4] = 0
        light15 = Button(padx=50, pady=50, bg='light grey', command=click15)
        light15.grid(column=5, row=3)

    if row2[4] == 0:
        row2[4] = 1
        light10 = Button(padx=50, pady=50, bg='gold', command=click10)
        light10.grid(column=5, row=2)

    elif row2[4] != 0:
        row2[4] = 0
        light10 = Button(padx=50, pady=50, bg='light grey', command=click10)
        light10.grid(column=5, row=2)

    if row3[3] == 0:
        row3[3] = 1
        light14 = Button(padx=50, pady=50, bg='gold', command=click14)
        light14.grid(column=4, row=3)

    elif row3[3] != 0:
        row3[3] = 0
        light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
        light14.grid(column=4, row=3)

    if row4[4] == 0:
        row4[4] = 1
        light20 = Button(padx=50, pady=50, bg='gold', command=click20)
        light20.grid(column=5, row=4)

    elif row4[4] != 0:
        row4[4] = 0
        light20 = Button(padx=50, pady=50, bg='light grey', command=click20)
        light20.grid(column=5, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click16():
    global light16
    global light11
    global light17
    global light21

    light16.grid_forget()
    light11.grid_forget()
    light17.grid_forget()
    light21.grid_forget()

    if row4[0] == 0:
        row4[0] = 1
        light16 = Button(padx=50, pady=50, bg='gold', command=click16)
        light16.grid(column=1, row=4)

    elif row4[0] != 0:
        row4[0] = 0
        light16 = Button(padx=50, pady=50, bg='light grey', command=click16)
        light16.grid(column=1, row=4)

    if row3[0] == 0:
        row3[0] = 1
        light11 = Button(padx=50, pady=50, bg='gold', command=click11)
        light11.grid(column=1, row=3)

    elif row3[0] != 0:
        row3[0] = 0
        light11 = Button(padx=50, pady=50, bg='light grey', command=click11)
        light11.grid(column=1, row=3)

    if row4[1] == 0:
        row4[1] = 1
        light17 = Button(padx=50, pady=50, bg='gold', command=click17)
        light17.grid(column=2, row=4)

    elif row4[1] != 0:
        row4[1] = 0
        light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
        light17.grid(column=2, row=4)

    if row5[0] == 0:
        row5[0] = 1
        light21 = Button(padx=50, pady=50, bg='gold', command=click21)
        light21.grid(column=1, row=5)

    elif row5[0] != 0:
        row5[0] = 0
        light21 = Button(padx=50, pady=50, bg='light grey', command=click21)
        light21.grid(column=1, row=5)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click17():
    global light17
    global light12
    global light18
    global light22
    global light16

    light17.grid_forget()
    light12.grid_forget()
    light18.grid_forget()
    light22.grid_forget()
    light16.grid_forget()

    if row4[1] == 0:
        row4[1] = 1
        light17 = Button(padx=50, pady=50, bg='gold', command=click17)
        light17.grid(column=2, row=4)

    elif row4[1] != 0:
        row4[1] = 0
        light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
        light17.grid(column=2, row=4)

    if row3[1] == 0:
        row3[1] = 1
        light12 = Button(padx=50, pady=50, bg='gold', command=click12)
        light12.grid(column=2, row=3)

    elif row3[1] != 0:
        row3[1] = 0
        light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
        light12.grid(column=2, row=3)

    if row4[2] == 0:
        row4[2] = 1
        light18 = Button(padx=50, pady=50, bg='gold', command=click18)
        light18.grid(column=3, row=4)

    elif row4[2] != 0:
        row4[2] = 0
        light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
        light18.grid(column=3, row=4)

    if row5[1] == 0:
        row5[1] = 1
        light22 = Button(padx=50, pady=50, bg='gold', command=click22)
        light22.grid(column=2, row=5)

    elif row5[1] != 0:
        row5[1] = 0
        light22 = Button(padx=50, pady=50, bg='light grey', command=click22)
        light22.grid(column=2, row=5)

    if row4[0] == 0:
        row4[0] = 1
        light16 = Button(padx=50, pady=50, bg='gold', command=click16)
        light16.grid(column=1, row=4)

    elif row4[0] != 0:
        row4[0] = 0
        light16 = Button(padx=50, pady=50, bg='light grey', command=click16)
        light16.grid(column=1, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click18():
    global light18
    global light13
    global light19
    global light23
    global light17

    light18.grid_forget()
    light13.grid_forget()
    light19.grid_forget()
    light23.grid_forget()
    light17.grid_forget()

    if row4[2] == 0:
        row4[2] = 1
        light18 = Button(padx=50, pady=50, bg='gold', command=click18)
        light18.grid(column=3, row=4)

    elif row4[2] != 0:
        row4[2] = 0
        light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
        light18.grid(column=3, row=4)

    if row3[2] == 0:
        row3[2] = 1
        light13 = Button(padx=50, pady=50, bg='gold', command=click13)
        light13.grid(column=3, row=3)

    elif row3[2] != 0:
        row3[2] = 0
        light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
        light13.grid(column=3, row=3)

    if row4[3] == 0:
        row4[3] = 1
        light19 = Button(padx=50, pady=50, bg='gold', command=click19)
        light19.grid(column=4, row=4)

    elif row4[3] != 0:
        row4[3] = 0
        light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
        light19.grid(column=4, row=4)

    if row5[2] == 0:
        row5[2] = 1
        light23 = Button(padx=50, pady=50, bg='gold', command=click23)
        light23.grid(column=3, row=5)

    elif row5[2] != 0:
        row5[2] = 0
        light23 = Button(padx=50, pady=50, bg='light grey', command=click23)
        light23.grid(column=3, row=5)

    if row4[1] == 0:
        row4[1] = 1
        light17 = Button(padx=50, pady=50, bg='gold', command=click17)
        light17.grid(column=2, row=4)

    elif row4[1] != 0:
        row4[1] = 0
        light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
        light17.grid(column=2, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click19():
    global light19
    global light14
    global light20
    global light24
    global light18

    light19.grid_forget()
    light14.grid_forget()
    light20.grid_forget()
    light24.grid_forget()
    light18.grid_forget()

    if row4[3] == 0:
        row4[3] = 1
        light19 = Button(padx=50, pady=50, bg='gold', command=click19)
        light19.grid(column=4, row=4)

    elif row4[3] != 0:
        row4[3] = 0
        light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
        light19.grid(column=4, row=4)

    if row3[3] == 0:
        row3[3] = 1
        light14 = Button(padx=50, pady=50, bg='gold', command=click14)
        light14.grid(column=4, row=3)

    elif row3[3] != 0:
        row3[3] = 0
        light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
        light14.grid(column=4, row=3)

    if row4[4] == 0:
        row4[4] = 1
        light20 = Button(padx=50, pady=50, bg='gold', command=click20)
        light20.grid(column=5, row=4)

    elif row4[4] != 0:
        row4[4] = 0
        light20 = Button(padx=50, pady=50, bg='light grey', command=click20)
        light20.grid(column=5, row=4)

    if row5[3] == 0:
        row5[3] = 1
        light24 = Button(padx=50, pady=50, bg='gold', command=click24)
        light24.grid(column=4, row=5)

    elif row5[3] != 0:
        row5[3] = 0
        light24 = Button(padx=50, pady=50, bg='light grey', command=click24)
        light24.grid(column=4, row=5)

    if row4[2] == 0:
        row4[2] = 1
        light18 = Button(padx=50, pady=50, bg='gold', command=click18)
        light18.grid(column=3, row=4)

    elif row4[2] != 0:
        row4[2] = 0
        light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
        light18.grid(column=3, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click20():
    global light20
    global light15
    global light19
    global light25

    light20.grid_forget()
    light15.grid_forget()
    light19.grid_forget()
    light25.grid_forget()

    if row4[4] == 0:
        row4[4] = 1
        light20 = Button(padx=50, pady=50, bg='gold', command=click20)
        light20.grid(column=5, row=4)

    elif row4[4] != 0:
        row4[4] = 0
        light20 = Button(padx=50, pady=50, bg='light grey', command=click20)
        light20.grid(column=5, row=4)

    if row3[4] == 0:
        row3[4] = 1
        light15 = Button(padx=50, pady=50, bg='gold', command=click15)
        light15.grid(column=5, row=3)

    elif row3[4] != 0:
        row3[4] = 0
        light15 = Button(padx=50, pady=50, bg='light grey', command=click15)
        light15.grid(column=5, row=3)

    if row4[3] == 0:
        row4[3] = 1
        light19 = Button(padx=50, pady=50, bg='gold', command=click19)
        light19.grid(column=4, row=4)

    elif row4[3] != 0:
        row4[3] = 0
        light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
        light19.grid(column=4, row=4)

    if row5[4] == 0:
        row5[4] = 1
        light25 = Button(padx=50, pady=50, bg='gold', command=click25)
        light25.grid(column=5, row=5)

    elif row5[4] != 0:
        row5[4] = 0
        light25 = Button(padx=50, pady=50, bg='light grey', command=click25)
        light25.grid(column=5, row=5)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click21():
    global light21
    global light22
    global light16

    light21.grid_forget()
    light22.grid_forget()
    light16.grid_forget()

    if row5[0] == 0:
        row5[0] = 1
        light21 = Button(padx=50, pady=50, bg='gold', command=click21)
        light21.grid(column=1, row=5)

    elif row5[0] != 0:
        row5[0] = 0
        light21 = Button(padx=50, pady=50, bg='light grey', command=click21)
        light21.grid(column=1, row=5)

    if row5[1] == 0:
        row5[1] = 1
        light22 = Button(padx=50, pady=50, bg='gold', command=click22)
        light22.grid(column=2, row=5)

    elif row5[1] != 0:
        row5[1] = 0
        light22 = Button(padx=50, pady=50, bg='light grey', command=click22)
        light22.grid(column=2, row=5)

    if row4[0] == 0:
        row4[0] = 1
        light16 = Button(padx=50, pady=50, bg='gold', command=click16)
        light16.grid(column=1, row=4)

    elif row4[0] != 0:
        row4[0] = 0
        light16 = Button(padx=50, pady=50, bg='light grey', command=click16)
        light16.grid(column=1, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click22():
    global light22
    global light21
    global light17
    global light23

    light22.grid_forget()
    light21.grid_forget()
    light17.grid_forget()
    light23.grid_forget()

    if row5[1] == 0:
        row5[1] = 1
        light22 = Button(padx=50, pady=50, bg='gold', command=click22)
        light22.grid(column=2, row=5)

    elif row5[1] != 0:
        row5[1] = 0
        light22 = Button(padx=50, pady=50, bg='light grey', command=click22)
        light22.grid(column=2, row=5)

    if row5[0] == 0:
        row5[0] = 1
        light21 = Button(padx=50, pady=50, bg='gold', command=click21)
        light21.grid(column=1, row=5)

    elif row5[0] != 0:
        row5[0] = 0
        light21 = Button(padx=50, pady=50, bg='light grey', command=click21)
        light21.grid(column=1, row=5)

    if row4[1] == 0:
        row4[1] = 1
        light17 = Button(padx=50, pady=50, bg='gold', command=click17)
        light17.grid(column=2, row=4)

    elif row4[1] != 0:
        row4[1] = 0
        light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
        light17.grid(column=2, row=4)

    if row5[2] == 0:
        row5[2] = 1
        light23 = Button(padx=50, pady=50, bg='gold', command=click23)
        light23.grid(column=3, row=5)

    elif row5[2] != 0:
        row5[2] = 0
        light23 = Button(padx=50, pady=50, bg='light grey', command=click23)
        light23.grid(column=3, row=5)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click23(): #bottom
    global light23
    global light22
    global light18
    global light24

    light23.grid_forget()
    light22.grid_forget()
    light18.grid_forget()
    light24.grid_forget()

    if row5[2] == 0:
        row5[2] = 1
        light23 = Button(padx=50, pady=50, bg='gold', command=click23)
        light23.grid(column=3, row=5)

    elif row5[2] != 0:
        row5[2] = 0
        light23 = Button(padx=50, pady=50, bg='light grey', command=click23)
        light23.grid(column=3, row=5)

    if row5[1] == 0:
        row5[1] = 1
        light22 = Button(padx=50, pady=50, bg='gold', command=click22)
        light22.grid(column=2, row=5)

    elif row5[1] != 0:
        row5[1] = 0
        light22 = Button(padx=50, pady=50, bg='light grey', command=click22)
        light22.grid(column=2, row=5)

    if row4[2] == 0:
        row4[2] = 1
        light18 = Button(padx=50, pady=50, bg='gold', command=click18)
        light18.grid(column=3, row=4)

    elif row4[2] != 0:
        row4[2] = 0
        light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
        light18.grid(column=3, row=4)

    if row5[3] == 0:
        row5[3] = 1
        light24 = Button(padx=50, pady=50, bg='gold', command=click24)
        light24.grid(column=4, row=5)

    elif row5[3] != 0:
        row5[3] = 0
        light24 = Button(padx=50, pady=50, bg='light grey', command=click24)
        light24.grid(column=4, row=5)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click24():
    global light24
    global light23
    global light19
    global light25

    light24.grid_forget()
    light23.grid_forget()
    light19.grid_forget()
    light25.grid_forget()

    if row5[3] == 0:
        row5[3] = 1
        light24 = Button(padx=50, pady=50, bg='gold', command=click24)
        light24.grid(column=4, row=5)

    elif row5[3] != 0:
        row5[3] = 0
        light24 = Button(padx=50, pady=50, bg='light grey', command=click24)
        light24.grid(column=4, row=5)

    if row5[2] == 0:
        row5[2] = 1
        light23 = Button(padx=50, pady=50, bg='gold', command=click23)
        light23.grid(column=3, row=5)

    elif row5[2] != 0:
        row5[2] = 0
        light23 = Button(padx=50, pady=50, bg='light grey', command=click23)
        light23.grid(column=3, row=5)

    if row4[3] == 0:
        row4[3] = 1
        light19 = Button(padx=50, pady=50, bg='gold', command=click19)
        light19.grid(column=4, row=4)

    elif row4[3] != 0:
        row4[3] = 0
        light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
        light19.grid(column=4, row=4)

    if row5[4] == 0:
        row5[4] = 1
        light25 = Button(padx=50, pady=50, bg='gold', command=click25)
        light25.grid(column=5, row=5)

    elif row5[4] != 0:
        row5[4] = 0
        light25 = Button(padx=50, pady=50, bg='light grey', command=click25)
        light25.grid(column=5, row=5)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

def click25():
    global light25
    global light24
    global light20

    light25.grid_forget()
    light24.grid_forget()
    light20.grid_forget()

    if row5[4] == 0:
        row5[4] = 1
        light25 = Button(padx=50, pady=50, bg='gold', command=click25)
        light25.grid(column=5, row=5)

    elif row5[4] != 0:
        row5[4] = 0
        light25 = Button(padx=50, pady=50, bg='light grey', command=click25)
        light25.grid(column=5, row=5)

    if row5[3] == 0:
        row5[3] = 1
        light24 = Button(padx=50, pady=50, bg='gold', command=click24)
        light24.grid(column=4, row=5)

    elif row5[3] != 0:
        row5[3] = 0
        light24 = Button(padx=50, pady=50, bg='light grey', command=click24)
        light24.grid(column=4, row=5)

    if row4[4] == 0:
        row4[4] = 1
        light10 = Button(padx=50, pady=50, bg='gold', command=click20)
        light10.grid(column=5, row=4)

    elif row4[4] != 0:
        row4[4] = 0
        light20 = Button(padx=50, pady=50, bg='light grey', command=click20)
        light20.grid(column=5, row=4)

    whitespace = Label(bg='light blue', font=('Arial', 9),
                       text=str(row1) + '\n' + str(row2) + '\n' + str(row3) + '\n' + str(row4) + '\n' + str(row5))
    whitespace.grid(columnspan=2, column=6, row=2)

    if (row1 == [1, 1, 1, 1, 1] and row2 == [1, 1, 1, 1, 1] and row3 == [1, 1, 1, 1, 1] and
            row4 == [1, 1, 1, 1, 1] and row5 == [1, 1, 1, 1, 1]):
        win()

    global clickcount
    clickcount += 1
    clickcounter = Label(bg='light blue', font=('Arial', 15), text='Click Counter:\n' + str(clickcount))
    clickcounter.grid(columnspan=2, column=6, row=3)

#lights
light1 = Button(padx=50, pady=50, bg='light grey', command=click1)
light1.grid(column=1, row=1)
light2 = Button(padx=50, pady=50, bg='light grey', command=click2)
light2.grid(column=2, row=1)
light3 = Button(padx=50, pady=50, bg='light grey', command=click3)
light3.grid(column=3, row=1)
light4 = Button(padx=50, pady=50, bg='light grey', command=click4)
light4.grid(column=4, row=1)
light5 = Button(padx=50, pady=50, bg='light grey', command=click5)
light5.grid(column=5, row=1)
light6 = Button(padx=50, pady=50, bg='light grey', command=click6)
light6.grid(column=1, row=2)
light7 = Button(padx=50, pady=50, bg='light grey', command=click7)
light7.grid(column=2, row=2)
light8 = Button(padx=50, pady=50, bg='light grey', command=click8)
light8.grid(column=3, row=2)
light9 = Button(padx=50, pady=50, bg='light grey', command=click9)
light9.grid(column=4, row=2)
light10 = Button(padx=50, pady=50, bg='light grey', command=click10)
light10.grid(column=5, row=2)
light11 = Button(padx=50, pady=50, bg='light grey', command=click11)
light11.grid(column=1, row=3)
light12 = Button(padx=50, pady=50, bg='light grey', command=click12)
light12.grid(column=2, row=3)
light13 = Button(padx=50, pady=50, bg='light grey', command=click13)
light13.grid(column=3, row=3)
light14 = Button(padx=50, pady=50, bg='light grey', command=click14)
light14.grid(column=4, row=3)
light15 = Button(padx=50, pady=50, bg='light grey', command=click15)
light15.grid(column=5, row=3)
light16 = Button(padx=50, pady=50, bg='light grey', command=click16)
light16.grid(column=1, row=4)
light17 = Button(padx=50, pady=50, bg='light grey', command=click17)
light17.grid(column=2, row=4)
light18 = Button(padx=50, pady=50, bg='light grey', command=click18)
light18.grid(column=3, row=4)
light19 = Button(padx=50, pady=50, bg='light grey', command=click19)
light19.grid(column=4, row=4)
light20 = Button(padx=50, pady=50, bg='light grey', command=click20)
light20.grid(column=5, row=4)
light21 = Button(padx=50, pady=50, bg='light grey', command=click21)
light21.grid(column=1, row=5)
light22 = Button(padx=50, pady=50, bg='light grey', command=click22)
light22.grid(column=2, row=5)
light23 = Button(padx=50, pady=50, bg='light grey', command=click23)
light23.grid(column=3, row=5)
light24 = Button(padx=50, pady=50, bg='light grey', command=click24)
light24.grid(column=4, row=5)
light25 = Button(padx=50, pady=50, bg='light grey', command=click25)
light25.grid(column=5, row=5)

root.mainloop()