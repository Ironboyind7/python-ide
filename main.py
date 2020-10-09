from tkinter import *
import keyboard
from pynput.keyboard import Key, Listener
root = Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    # print(inputValue)
    return inputValue
def run():
    exec(retrieve_input())
    print(exec(retrieve_input()))
    
root.geometry(f"{600}x{500}")
textBox=Text(root,height=30,bg= "dark grey")    
textBox.pack(fill=BOTH)
textbox=Text(root,bg="grey")
textbox.pack(fill=BOTH)
def redirector(inputStr):
    textbox.insert(INSERT, inputStr)
sys.stdout.write = redirector 
keyboard.add_hotkey("ctrl+r",lambda :exec(retrieve_input()))
root.mainloop()
