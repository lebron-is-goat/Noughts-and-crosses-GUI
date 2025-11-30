import tkinter as tk
from tkinter import messagebox
turns = 1 # X or O when button is pressed

#States of all the squares in the grid
states = [" ", " ", " ", " ", " ", " ", " ", " ", " "]



class GUI:
    def __init__(self):
        
        global turns
        global states

        #Sets up window
        root = tk.Tk()
        root.geometry("400x550")
        root.title("Noughts and Crosses Gui")
        icon = tk.PhotoImage(file="./icon.png")
        root.iconphoto(False, icon)
        #Title
        title_ = tk.Label(root, text="Noughts and Crosses", font=("Arial, 18"))
        title_.pack(pady=5)

        #Options
        use_computer =tk.BooleanVar#Use computer player or not
        note=tk.Label(root, text="First Player is X, If in Singleplayer you always play first", font=("arial", 10))
        note.pack(pady=5)
        player2=tk.Checkbutton(root, text="Singleplayer", font=("arial", 10), variable=use_computer)
        player2.pack(pady=5)
        

        #Main playing area
        grid_frame = tk.Frame(root)
        for x in range(3):
            grid_frame.columnconfigure(x, weight=1)
            grid_frame.rowconfigure(x, weight=1)

        #Buttons for X+O
        text0= tk.StringVar()
        tk.Button(grid_frame, textvariable=text0, font=("arial", 50), command=lambda:self.press(0, text0), width = 5).grid(row=0, column=0, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text1= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text1, command=lambda:self.press(1, text1), width = 5).grid(row=0, column=1, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text2= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text2, command=lambda:self.press(2, text2), width = 5).grid(row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text3= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text3, command=lambda:self.press(3, text3), width = 5).grid(row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text4= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text4, command=lambda:self.press(4, text4), width = 5).grid(row=1, column=1, sticky=tk.W+tk.E+tk.S+tk.W)
    
        text5= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text5, command=lambda:self.press(5, text5), width = 5).grid(row=1, column=2, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text6= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text6, command=lambda:self.press(6, text6), width = 5).grid(row=2, column=0, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text7= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text7, command=lambda:self.press(7, text7), width = 5).grid(row=2, column=1, sticky=tk.W+tk.E+tk.S+tk.W)
        
        text8= tk.StringVar()
        tk.Button(grid_frame, font=("arial", 50), textvariable=text8, command=lambda:self.press(8, text8), width = 5).grid(row=2, column=2, sticky=tk.W+tk.E+tk.S+tk.W)
        
        
        grid_frame.pack( fill="both")
        
        #resets grid
        reset = tk.Button(root, text = "Reset",font=("arial", 20), command=lambda:self.reset(text0, text1, text2, text3, text4, text5, text6, text7, text8))
        reset.pack(pady=5)
        
        root.mainloop()
    
    

    ################## Resets Grid #################
    def reset(self, text0, text1, text2, text3, text4, text5, text6, text7, text8):    
        globals()["states"] = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        globals()["turns"] = 1
        text0.set(" ")
        text1.set(" ")
        text2.set(" ")
        text3.set(" ")
        text4.set(" ")
        text5.set(" ")
        text6.set(" ")
        text7.set(" ")
        text8.set(" ")
    
    ############### Tracks Os And Xs in states and on gui ##############
    def press(self, button, text):
        if (turns % 2) == 0:
            globals()["states"][button]= "O"
            text.set("O")
        else:
            globals()["states"][button]= "X"
            text.set("X")
        globals()["turns"] += 1

########### Checks for winner each turn ##########
        if states[0] == "X" and states[1] =="X" and states[2] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[0] == "O" and states[1] =="O" and states[2] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")
        
        elif states[3] == "X" and states[4] =="X" and states[5] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[3] == "O" and states[4] =="O" and states[5] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")
            
        elif states[6] == "X" and states[7] =="X" and states[8] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[6] == "O" and states[7] =="O" and states[8] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")
        
        elif states[0] == "X" and states[4] =="X" and states[8] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[0] == "O" and states[4] =="O" and states[8] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")
        
        elif states[2] == "X" and states[4] =="X" and states[6] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[2] == "O" and states[4] =="O" and states[6] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")

        elif states[0] == "X" and states[3] =="X" and states[6] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[0] == "O" and states[3] =="O" and states[6] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")

        elif states[1] == "X" and states[4] =="X" and states[7] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[1] == "O" and states[4] =="O" and states[7] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")

        elif states[2] == "X" and states[5] =="X" and states[8] == "X":
            messagebox.showinfo(title="Winner!", message="Player X Wins!")
        elif states[1] == "O" and states[4] =="O" and states[7] == "O":
            messagebox.showinfo(title="Winner!", message="Player O Wins!")
        
        elif " " not in states:
            messagebox.showinfo(title="Draw!", message="Its A Draw!")

GUI()


class computer_player:
    def __init__(self):
        
        global turns 
        global states

        corners = states[0, 2, 6, 8]
        center = states[4]
        middles = [1, 3, 5, 7]

