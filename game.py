from tkinter import *
from textblob import TextBlob


def clearAll():
	word1_field.delete(0, END)
	word2_field.delete(0, END)


def correction():
	input_word = word1_field.get()

	blob_obj = TextBlob(input_word)

	corrected_word = str(blob_obj.correct())

	word2_field.insert(10, corrected_word)

if 'name' :

	root = Tk()
	root.configure(background='turquoise')

	
	root.geometry("1000x500+40+40")

	f = ("Calibri", 20, "bold")
	root.title("Spell Corrector")

	
	headlabel = Label(root, text='Welcome to Spell Corrector Application',
					fg='white', bg="black", font = f)

	label1 = Label(root, text="Input Word",
				fg='red', bg='pink', font = f)

	label2 = Label(root, text="Corrected Word",
				fg='red', bg='pink', font = f)

	headlabel.grid(row=0, column=1)
	label1.grid(row=1, column=0)
	label2.grid(row=3, column=0, padx=10)
	word1_field = Entry()
	word2_field = Entry()

	
	word1_field.grid(row=1, column=1, padx=10, pady=10)
	word2_field.grid(row=3, column=1, padx=10, pady=10)

	
	button1 = Button(root, text="Correction", bg="black", fg="white",
					command=correction, font = f)

	button1.grid(row=2, column=1)
	button2 = Button(root, text="Clear", bg="black",
					fg="white", command=clearAll, font = f)

	button2.grid(row=4, column=1)


	root.mainloop(
