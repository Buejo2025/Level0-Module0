from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score =0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    User = simpledialog.askstring(title='Codebreaker', prompt="Do I listen to For King and Country music?")
    if User=="No":
        messagebox.showinfo(title="Greeter", message="yes " + "subtract a point")
        score-=1
    else:
        score+=2
        messagebox.showinfo(title="Greeter", message="no " + "Add two points")
    #      // 3.  Use an if statement to check if their answer is correct
    Answer = simpledialog.askstring(title='Codebreaker', prompt="Do I listen to BTS?")
    if Answer=="yes":
        messagebox.showinfo(title="Greeter", message="yes " + "Add one points")
        score+=1
    else:
        score-=2
        messagebox.showinfo(title="Greeter", message="no " + "Subtract two points")

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
