from tkinter import ttk


class HomePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		self.label = ttk.Label(self, text="Welcome to Convertsy! Get started below:")
		self.label.pack()

		ttk.Button(self, text='Temperatures', width=25, command=lambda: master.change_frame(TemperaturePage)).pack()
		
		ttk.Button(self, text='Angle', width=25, command=lambda: master.change_frame(AnglePage)).pack()
		
		ttk.Button(self, text='Area', width=25, command=lambda: master.change_frame(AreaPage)).pack()

		ttk.Button(self, text='Currencies', width=25, command=lambda: master.change_frame(CurrencyPage)).pack()

		ttk.Button(self, text='Time', width=25, command=lambda: master.change_frame(CurrencyPage)).pack()
		
		ttk.Button(self, text='Duration', width=25, command=lambda: master.change_frame(CurrencyPage)).pack()

		self.pack()


class TemperaturePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Temperatures").pack()


class AnglePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Angle").pack()


class AreaPage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Area").pack()


class CurrencyPage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Currencies").pack()


class TimeZonePage(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Timezones").pack()


class Duration(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		
		ttk.Label(self, text="Duration").pack()
		