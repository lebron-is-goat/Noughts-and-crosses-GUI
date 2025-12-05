import tkinter as tk
from tkinter import messagebox
import random
turns = 1 # X or O when button is pressed
computer_first = ...
#States of all the squares in the grid
states = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

texts = [None]

class Gui:
    def __init__(self):
        
        global turns, states, computer_first

        #Sets up window
        root = tk.Tk()
        root.geometry("400x475")
        root.title("Noughts and Crosses Gui")
        icon = tk.PhotoImage(file="./icon.png")
        root.iconphoto(False, icon)
        #Title
        title_ = tk.Label(root, text="Noughts and Crosses", font=("Arial, 18"))
        title_.pack(pady=5)
        
        
        #Options
        self.use_computer=tk.BooleanVar()
        self.computer_first = tk.BooleanVar()
        note=tk.Label(root, text="First Player is X", font=("arial", 10))
        note.pack(pady=5)
        optionsframe = tk.Frame(root)
        optionsframe.columnconfigure(0 , weight=1)
        optionsframe.columnconfigure(1 , weight=1)
        singleplayer=tk.Checkbutton(optionsframe, text="Singleplayer", font=("arial", 10), variable=self.use_computer, command=self.use_computer_player)
        singleplayer.grid(column=0, row=0)
        first_player=tk.Checkbutton(optionsframe, text="Computer Play First", font=("arial", 10), variable=self.computer_first, command=self.first_player)
        first_player.grid(column=1, row=0)
        optionsframe.pack(pady=5)
        
        ######### Sets up Frame for the Grid #########
        grid_frame = tk.Frame(root)
        for x in range(3):
            grid_frame.columnconfigure(x, weight=1)
            grid_frame.rowconfigure(x, weight=1)

        ################# Sets up Grid with Buttons ###############                   
        text0= tk.StringVar()                                                             
        tk.Button(grid_frame, textvariable=text0, font=("arial", 50), command=lambda:self.press(0), width = 5).grid(row=0, column=0, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text1= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text1, command=lambda:self.press(1), width = 5).grid(row=0, column=1, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text2= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text2, command=lambda:self.press(2), width = 5).grid(row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text3= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text3, command=lambda:self.press(3), width = 5).grid(row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text4= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text4, command=lambda:self.press(4), width = 5).grid(row=1, column=1, sticky=tk.W+tk.E+tk.S+tk.W)
    
        text5= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text5, command=lambda:self.press(5), width = 5).grid(row=1, column=2, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text6= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text6, command=lambda:self.press(6), width = 5).grid(row=2, column=0, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text7= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text7, command=lambda:self.press(7), width = 5).grid(row=2, column=1, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text8 =tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text8, command=lambda:self.press(8), width = 5).grid(row=2, column=2, sticky=tk.W+tk.E+tk.S+tk.W)
        
        grid_frame.pack( fill="both")
        
        self.resetB = tk.Button(root, text = "Reset",font=("arial", 20), command=self.reset)
        self.resetB.pack(pady=5)
        globals()["texts"] = [text0, text1, text2, text3, text4, text5, text6, text7, text8]
        
        root.mainloop()
    
        

    def use_computer_player(self):
         if self.use_computer.get() == True:
            ComputerPlayer()
    def first_player(self):
        if self.computer_first.get() == True:
            globals()["computer_first"] = True
        else:
            globals()["computer_first"] = False


    ################## Resets Grid #################
    def reset(self):    
        globals()["states"] = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        globals()["turns"] = 1
        for x in range(0,9):
            texts[x].set(" ")
        

    ########### Checks for winner after a winner is possible every turn after##########
    def check_winner(self):
        
        def o_wins():
            messagebox.showinfo(title="Winner!", message="Player O Wins!")
            Gui.reset(self)

        def x_wins():
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
            Gui.reset(self)
        if states[0] == "X" and states[1] =="X" and states[2] == "X":
            x_wins()
        elif states[0] == "O" and states[1] =="O" and states[2] == "O":
            o_wins()
        
        elif states[3] == "X" and states[4] =="X" and states[5] == "X":
            x_wins()
        elif states[3] == "O" and states[4] =="O" and states[5] == "O":
            o_wins()
            
        elif states[6] == "X" and states[7] =="X" and states[8] == "X":
            x_wins()
        elif states[6] == "O" and states[7] =="O" and states[8] == "O":
            o_wins()
        
        elif states[0] == "X" and states[4] =="X" and states[8] == "X":
            x_wins()
        elif states[0] == "O" and states[4] =="O" and states[8] == "O":
            o_wins()
        
        elif states[2] == "X" and states[4] =="X" and states[6] == "X":
            x_wins()
        elif states[2] == "O" and states[4] =="O" and states[6] == "O":
            o_wins()

        elif states[0] == "X" and states[3] =="X" and states[6] == "X":
            x_wins()
        elif states[0] == "O" and states[3] =="O" and states[6] == "O":
            o_wins()

        elif states[1] == "X" and states[4] =="X" and states[7] == "X":
            x_wins()
        elif states[1] == "O" and states[4] =="O" and states[7] == "O":
            o_wins()

        elif states[2] == "X" and states[5] =="X" and states[8] == "X":
            x_wins()
        elif states[1] == "O" and states[4] =="O" and states[7] == "O":
            o_wins()
        
        elif " " not in states:
            messagebox.showinfo(title="Draw!", message="Its A Draw!")
            Gui.reset(self)
        
        
    
    ############### Tracks Os And Xs in states and on gui ##############
    def press(self, button):
        global texts
        if (turns % 2) == 0:
            globals()["states"][button]= "O"
            texts[button].set("O")
        else:
            globals()["states"][button]= "X"
            texts[button].set("X")
        globals()["turns"] += 1
        if turns >= 6:
            Gui.check_winner(self)
        print(turns)
        if self.computer_player == True and (turns % 2) == 0:
            ComputerPlayer()

class ComputerPlayer():
    def __init__(self):
        from time import sleep
        global turns, states, computer_first, texts
        
        corners = [[0, 8], [2, 6]]
        center = [4]
        edges = [1, 3, 5, 7]

        if computer_first == True:
            seed1 = random.randint(0,1)
            seed2 = random.randint(0,1)
            pair = corners[seed1]
            corner1 = pair[seed2]
            self.computer_press(corner1)
            while states == 3: 
                if states[4] == "O":
                    print("hi")
                

    def computer_press(self, button):
        Gui.press(self, button)

            

                   
        






Gui()

