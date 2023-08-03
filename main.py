from tkinter import *


class Converter:
	def __init__(self):
		# Button fonts and colour
		button_font = ("Arial", "12", "bold")
		button_fg = "#FFFFFF"

		# Set up GUI frame
		self.temp_frame = Frame(padx=10, pady=10)
		self.temp_frame.grid()

		# Title and Headings
		self.temp_title = Label(self.temp_frame,
														 text=("(Quiz Game Title)"),
														 font=("Arial", "16", "bold"))
		self.temp_title.grid(row=0)

		sub_heading = "New players click the 'NEW PLAYER' button " \
					"Returning players click the 'RETURNING PLAYER' button"
		self.temp_heading = Label(self.temp_frame,
														 text=sub_heading,
														 wrap=322,
														 width=40,
														 justify="center")
		self.temp_heading.grid(row=1)
		# Main Menu Buttons
		self.button_frame = Frame(self.temp_frame)
		self.button_frame.grid(row=2)

		NP_Text = "NEW " \
					"PLAYER"

		RP_Text = "RETURNING " \
					"PLAYER"
		self.New_Player_Button = Button(self.button_frame,
																	 text=NP_Text,
																	 bg="#FF66B3",
																	 fg=button_fg,
																	 font=button_font,
																	 wrap=100,
																	 width=12,
																	 command=self.New_Player)
		self.New_Player_Button.grid(row=0, column=1, padx=5, pady=5)

		self.Returning_Player_Button = Button(self.button_frame,
																	 text=RP_Text,
																	 bg="#FF66FF",
																	 fg=button_fg,
																	 font=button_font,
																	 wrap=110,
																	 width=12,
																	 state=DISABLED)
		self.Returning_Player_Button.grid(row=0, column=2, padx=5, pady=5)

	@staticmethod
	def New_Player ():
		DisplayINST()

class DisplayINST:

	def __init__(self):
		background = "#FFE6CC"

		self.INST_box = Toplevel()

		self.INST_frame = Frame(self.INST_box,
													 width=300,
													 height=200,
													 bg=background)
		self.INST_frame.grid()
# Main Routine
if __name__ == "__main__":
	root = Tk()
	root.title("(Quiz Game Title)")
	Converter()
	root.mainloop()