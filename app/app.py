import tkinter as tk
from frames import *


class App(tk.Tk):
	def __init__(self):
		super(App, self).__init__()
		
		self.title("Convertsy - Welcome!")
		self.geometry("450x450")
		self.resizable(False, False)

		self._frame = None
		self.change_frame(HomePage)
		
	def change_frame(self, frame_class):
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()


if __name__ == "__main__":
	app = App()
	app.mainloop()
