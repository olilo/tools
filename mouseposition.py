import time
from Xlib import display
from thread import start_new_thread

import Tkinter as tk

def update_mouse_position(var):
	screen = display.Display().screen().root
	while True:
		data = screen.query_pointer()._data
		pos = "(%s, %s)" % (data["root_x"], data["root_y"])
		var.set(pos)
		time.sleep(0.1)


if __name__ == '__main__':
	win=tk.Tk()
	win.wm_attributes('-topmost', 1)
	pos = tk.StringVar()
	win.geometry("120x20")
	lab = tk.Label(win, textvariable=pos)
	lab.pack()
	start_new_thread(update_mouse_position, (pos,))
	win.mainloop()

