from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    point = random.randint(0,3)
    # 2. Print your variable to the console
    print(point)
    # 3. Get the user to enter something that they think is awesome
    Type = simpledialog.askstring(title='Codebreaker', prompt="Enter something")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if point==0:
        messagebox.showinfo(title='Codebreaker', message="What you enter is awesome")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if point==1:
      messagebox.showinfo(title='Codebreaker', message="What you enter is ok")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if point==2:
      messagebox.showinfo(title='Codebreaker', message="What you enter is boring")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if point==3:
       messagebox.showinfo(title='Codebreaker', message="What you enter is nice")
    # Run the window's .mainloop() method
    window.mainloop()
