import os
import random
from cryptography.fernet import Fernet
from tkinter import *
import tkinter as tk

root = Tk()
root.wm_title("Password Generator")

key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key)
file.close()

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_-/?[]"

def GenPass():
	password = ""
	try:
		passlength = lengthspace.get()
		passlength = int(passlength)
		if passlength <= 30 and passlength >= 5:
			errlabel.config(text = "")
			for i in range(passlength):
				password += random.choice(charset)
			passlabel.config(text = password)
			try:
				f = open("password.txt", "w")
				f.write(password)
				f.close()
			except:
				errlabel.config(text = "Error: Couldn't save password to password.txt.")
		else:
			if passlength > 30:
				errlabel.config(text = "Error: Password length is too long.")
			if passlength < 5:
				errlabel.config(text = "Error: Password length is too short.")
	except:
		errlabel.config(text = "Error: Password length was either undefined or not an integar.")

def Encryptpass():
	try:
		Encrypt()
	except:
		errlabel.config(text = "Error: No password generated and/or no password.txt file.")

def Decryptpass():
	try:
		Decrypt()
	except:
		errlabel.config(text = "Error: No password and/or key file.")

def Encrypt():
	file = open('key.key', 'rb')
	key = file.read()
	file.close()

	with open('password.txt', 'rb') as f:
		data = f.read()

	fernet = Fernet(key)
	encrypted = fernet.encrypt(data)

	with open('password.txt.encrypted', 'wb') as f:
		f.write(encrypted)

	os.remove("password.txt")

def Decrypt():
	file = open('key.key', 'rb')
	key = file.read()
	file.close()

	with open('password.txt.encrypted', 'rb') as f:
		data = f.read()

	fernet = Fernet(key)
	decrypted = fernet.decrypt(data)

	with open('password.txt', 'wb') as f:
		f.write(decrypted)

	os.remove("password.txt.encrypted")

def on_entry_click(event):
    if lengthspace.get() == 'Enter password length...':
       lengthspace.delete(0, "end")
       lengthspace.insert(0, '')
       lengthspace.config(fg = 'black')

def on_focusout(event):
    if lengthspace.get() == '':
        lengthspace.insert(0, 'Enter password length...')
        lengthspace.config(fg = 'grey')

HEIGHT = 700
WIDTH = 800

canvas = Canvas(root, height = HEIGHT, width = WIDTH, bg = "#bfbfbf")
canvas.pack()

errlabel = Label(root, font = 80, bg = "#0073e6")
errlabel.place(relx = 0.5, rely = 0.6, anchor = "center")

passlabel = Label(root, font = 80, bg = "#0073e6")
passlabel.place(relx = 0.5, rely = 0.5, anchor = "center")

lengthspace = Entry(root, bg = "#e6e6ff", font = 80, bd = 2)
lengthspace.place(relx = 0.35, rely = 0.75, anchor = "center")
lengthspace.insert(0, 'Enter password length...')
lengthspace.bind('<FocusIn>', on_entry_click)
lengthspace.bind('<FocusOut>', on_focusout)

genbutton = Button(root, font = 80, text = "Generate New Password", bd = 2, command = GenPass)
genbutton.place(relx = 0.65, rely = 0.75, anchor = "center")

encryptbutton = Button(root, font = 80, text = "Encrypt Password", bd = 2, command = Encryptpass)
encryptbutton.place(relx = 0.35, rely = 0.35, anchor = "center")

decryptbutton = Button(root, font = 80, text = "Decrypt Password", bd = 2, command = Decryptpass)
decryptbutton.place(relx = 0.65, rely = 0.35, anchor = "center")

root.mainloop()
