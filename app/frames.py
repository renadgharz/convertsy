from tkinter import ttk


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