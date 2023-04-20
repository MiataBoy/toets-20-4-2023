from functies import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox # if you want to send messages to the user.

# functions
def calculate():
    textToBeCalculated = calculateInput.get('1.0', 'end') # get all the text from inputfield
    sentencesLabel.config(text =f"Zinnen: {getNumberOfSentences(textToBeCalculated)}")
    wordsLabel.config(text=f"Woorden: {getNumberOfWords(textToBeCalculated)}")
    characterLabel.config(text=f"Letters: {getNumberOfCharacters(textToBeCalculated)}")
    aviLabel.config(text=f"AVI: {getAVI(textToBeCalculated)}")



#variables TK
root = tk.Tk()              # create tkInter window
root.title('Text analyser') # set title
root.geometry('600x600')    # set dimension
calculateInput = tk.Text(root, width = 70, height = 30, background='lightgrey')            # generate imput element
calculateButton = ttk.Button(root, text='Bereken score(s)', command=calculate)        # generate button when pressed -> calculate
characterLabel = tk.Label(root, text=f'Karakters:', width=20, bg='black', fg='white') # generate characterLabel
wordsLabel = tk.Label(root, text=f'Woorden:', width=20, bg='black', fg='white')
sentencesLabel = tk.Label(root, text=f'Zinnen:', width=20, bg='black', fg='white')    # generate sentencesLabel
aviLabel = tk.Label(root, text=f'AVI:', width=20, bg='blue', fg='white')

calculateInput.place(x=20, y=20)   # place is one of the ways to put elements on root (window).
calculateButton.place(x=20, y=520)
sentencesLabel.place(x=20, y=560)
wordsLabel.place(x=180, y=560)
characterLabel.place(x=340, y=560)
aviLabel.place(x=180, y=520)

# start program
root.mainloop() # runs until stopped with default stop button.
