from tkinter import ttk


class HomePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Welcome to Convertsy! Get started below:").pack(pady=(15, 15))

		ttk.Button(self, text='Temperatures', width=25, command=lambda: master.change_frame(TemperaturePage)).pack(pady=10)
		
		ttk.Button(self, text='Angle', width=25, command=lambda: master.change_frame(AnglePage)).pack(pady=10)
		
		ttk.Button(self, text='Area', width=25, command=lambda: master.change_frame(AreaPage)).pack(pady=10)
		
		ttk.Button(self, text='Duration', width=25, command=lambda: master.change_frame(DurationPage)).pack(pady=10)

		self.pack()


class TemperaturePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Button(self, text='Home Page', width=25, command=lambda: master.change_frame(HomePage)).pack(pady=(15, 15))


class AnglePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Button(self, text='Home Page', width=25, command=lambda: master.change_frame(HomePage)).pack(pady=(15, 15))


class AreaPage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Button(self, text='Home Page', width=25, command=lambda: master.change_frame(HomePage)).pack(pady=(15, 15))


class DurationPage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Button(self, text='Home Page', width=25, command=lambda: master.change_frame(HomePage)).pack(pady=(15, 15))
		