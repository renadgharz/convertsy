import tkinter as tk
from tkinter import ttk


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


class HomePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		self.label = ttk.Label(self, text="Welcome to Convertsy! Get started below:")
		self.label.pack()
		
		ttk.Button(self, text='Angle', command=lambda: master.change_frame(AnglePage)).pack()

		ttk.Button(self, text='Area', command=lambda: master.change_frame(AreaPage)).pack()
		
		self.pack()


class AnglePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Angle").pack()


class AreaPage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Area").pack()


if __name__ == "__main__":
	app = App()
	app.mainloop()
