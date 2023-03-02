import random
import tkinter 

window = tkinter.Tk()
window.configure(background='#F3F4F8')
window.geometry('500x400')
window.title('Colourful Word Game')

smileyface = tkinter.PhotoImage(file='smileyface.png')
smileyfaceLabel = tkinter.Label(window, image=smileyface)
smileyfaceLabel.place(x=250, y=140, anchor='center')

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'black']
player_score = 0
max_time = 30
time_remaining = max_time
end = tkinter.Label(window, text='Game over', font = ('Cambria', 60))

def click():
    smileyfaceLabel.place_forget()
    word.place(x=250, y=150, anchor='center')
    next()
    startGame()

def startGame(event):
    if time_remaining == max_time:
        countdown()
    next()

def countdown():
    global time_remaining
    global end
    if time_remaining > 0:
        time_remaining -= 1
        clock.configure(text='Time remaining: '+ str(time_remaining))
        clock.after(1000, countdown) 
    
    else:
        global player_score
        score.config(text='Final score: ' + str(player_score))
        word.place_forget()
        startButton.place_forget()
        end.place(x=250, y=150, anchor='center')
        restartButton = tkinter.Button(window, text='Play again', command=restartGame)
        restartButton.place(x=250, y=250, anchor='center')

def next():
    global player_score 
    global time_remaining
    global colours
    if time_remaining > 0:
        answerbox.focus_set()
        if answerbox.get().lower() == colours[1].lower():
            player_score += 1
        answerbox.delete(0, tkinter.END)
        random.shuffle(colours)
        word.config(fg=str(colours[1]), text=str(colours[0]))
        score.config(text='Score: ' + str(player_score)) 

def restartGame():
    global time_remaining
    global player_score
    time_remaining = max_time
    player_score = 0
    end.place_forget()

    global word
    word = tkinter.Label(window, font=('Cambria', 60))
    word.place(x=250, y=150, anchor='center')

    startGame(None)

score = tkinter.Label(window, text='To begin the game, press Start.')
score.place(x=0, y=0)

clock = tkinter.Label(window, text='Time remaining: ' + str(time_remaining))
clock.place(x=375, y=0)

instructions = tkinter.Label(window, text='Type the colour of the word shown on the screen in all lowercase\n letters to score points for each correct answer. Enjoy :)')
instructions.place(x=250, y=50, anchor='center')

word = tkinter.Label(window, font = ('Cambria', 60))

answerbox = tkinter.Entry(window, width=40)
answerbox.place(x=250, y=300, anchor='center')

startButton = tkinter.Button(window, text='Start', command=click)
startButton.place(x=250, y=250, anchor='center')

window.bind('<Return>', startGame) 
answerbox.focus_set()

window.mainloop()