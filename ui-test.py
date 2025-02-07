from tkinter import *

def rgb_to_hex(rgb: tuple) -> str:
    hex_value: str = ""
    for value in rgb:
        current_hex: str = hex(value).replace('0x','')
        hex_value += (current_hex if len(current_hex) > 1 else f"0{current_hex}")
    return hex_value

root = Tk()
root.geometry('300x500')
root.title('Test')
root.config(bg=f"#{rgb_to_hex((170, 170, 255))}")

root.mainloop()