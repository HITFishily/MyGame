# -*- coding: utf-8 -*-
from tkinter import font
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from MainC import *
from threading import Timer
import test
import sys


class Page:
	def __init__(self, root=None):
		self.root = root
		self.root.geometry('800x600+200+200')
		self.root.resizable(0,0)
		self.root.title('TkTest')
		self.frmMain = tk.Frame(self.root)
		self.frm2 = tk.Frame(self.root)
		self.frm3 = tk.Frame(self.root)
		self.file = open(r"color.txt", "r", encoding = 'utf-8')
		self.DB   = simpleToolSql("Dta")
		self.MC   = CMainCharacter(self.DB) 
		self.text_font	 = font.Font(family='经典隶变简', size=12, weight='normal')
		self.button_font = font.Font(family='经典隶变简', size=16, weight='bold')

		tk.Label (self.frmMain, text='Title1').place(in_=self.frmMain, x=50, y=50,anchor=tk.NW)
		tk.Button(self.frmMain, text='New', height = 2, width = 10).place(in_=self.frmMain, x=600, y=400,anchor=tk.NW)
		tk.Button(self.frmMain, text='Continue', height = 2, width = 10, command=self.OnPressButton2FromFrame1).place(in_=self.frmMain, x=600, y=450,anchor=tk.NW)
		tk.Button(self.frmMain, text='Exit', height = 2, width = 10, command=self.OnPressButton3FormFrame1).place(in_=self.frmMain, x=600, y=500,anchor=tk.NW)
		self.frmMain.config(height=600, width=800)
		
		tk.Button(self.frm2, text='Readline', height = 2, width = 10, command=self.OnPressButton2FromFrame2).place(in_=self.frm2, x=200, y=250,anchor=tk.CENTER)
		tk.Button(self.frm2, text='Work', height = 2, width = 10, command=self.OnPressButton3FromFrame2).place(in_=self.frm2, x=300, y=250,anchor=tk.CENTER)
		tk.Button(self.frm2, text='Save', height = 2, width = 10, command=self.OnPressButton4FromFrame2).place(in_=self.frm2, x=400, y=250,anchor=tk.CENTER)
		self.frm2.config(height=600, width=600)
		self.text = ScrolledText(self.root, height=10, width=70, font = self.text_font, cursor='arrow', bg='Silver', exportselection='false')
		
	def MainPage(self):
		self.frmMain.place(x=0, y=0, anchor=tk.NW)

	def PrintOnSrceen(self, var):
		self.text.config(state="normal")
		self.text.insert('end', var)
		self.text.see(tk.END)
		self.text.config(state="disabled")	

	def OnPressButton2FromFrame1(self):
		self.frmMain.place_forget()

		tk.Button(self.root, text='按 钮1', height = 2, width = 10, font = self.button_font).place(in_=self.root, x=30, y=30,anchor=tk.NW)
		tk.Button(self.root, text='按 钮2', height = 2, width = 10, font = self.button_font).place(in_=self.root, x=30, y=110,anchor=tk.NW)
		tk.Button(self.root, text='按 钮3', height = 2, width = 10, font = self.button_font).place(in_=self.root, x=30, y=190,anchor=tk.NW)
		tk.Button(self.root, text='按 钮4', height = 2, width = 10, font = self.button_font).place(in_=self.root, x=30, y=270,anchor=tk.NW)
		tk.Button(self.root, text='按 钮5', height = 2, width = 10, font = self.button_font).place(in_=self.root, x=30, y=350,anchor=tk.NW)
		tk.Button(self.root, text='按 钮6', height = 2, width = 10, font = self.button_font).place(in_=self.root, x=30, y=430,anchor=tk.NW)
		tk.Button(self.root, text='退 出', height = 2, width = 10, font = self.button_font, command = self.OnPressButton3FormFrame1).place(in_=self.root, x=30, y=510,anchor=tk.NW)

		self.frm2.place(x=200, y=0, anchor=tk.NW)
		self.text.place(in_=self.root, x=490, y=485, anchor=tk.CENTER)
		self.PrintOnSrceen("Python数据可视化\n")
	
	#def OnPressButtonRock(self):

			

	def OnPressButton3FormFrame1(self):
		self.DB.close()
		sys.exit(0)

	def OnPressButton1FromFrame2(self):
		self.frm2.place_forget()
		self.text.place_forget()
		self.frmMain.place(x=0, y=0, anchor=tk.NW)

	def OnPressButton2FromFrame2(self):
		var = self.file.readline()
		self.PrintOnSrceen(var)

	def OnPressButton3FromFrame2(self):
		if self.MC.IncreaseExp(13) == True:
			self.text.config(state="normal")
			self.PrintOnSrceen("get 13 exp, Levelup!\n")
		else:
			self.PrintOnSrceen("get 13 exp!\n")

	def OnPressButton4FromFrame2(self):
		self.MC.UpdateDB()

if __name__ == '__main__':
	root = tk.Tk()
	p = Page(root)
	p.MainPage()
	tk.mainloop()