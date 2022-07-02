#!/usr/bin/env python3


def GUI_Calculator_Program(created_by="Ruben Leonardo Sigalingging"):
	# IMPORT MODUL PYTHON3
	import os
	from os import system
	system("clear")
	# system("pip install tk")
	# system("pip install pyfiglet")
	system("clear")
	import pyfiglet
	from pyfiglet import figlet_format
	from time import time,sleep
	import math
	print("")


	# BUAT TAMPILAN AWAL PROGRAM GUI NYA.
	tampilan_program_kalkulator_gui=figlet_format("GCP",font="3-d")
	print(tampilan_program_kalkulator_gui)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Sabtu, 2 Juli, 2022, Pukul 12:55 PM.")
	print("[!] Fungsi: Kalkulator Program GUI")
	print("[!] Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10\n")


	# BUAT FUNGSI BARU UNTUK SCRIPT PEMROSES NYA.
	def program_pemroses(created_by="Ruben Leonardo Sigalingging"):
		pemroses=tombol_input_program_kalkulator.get()
		pemroses=int(pemroses)
		pemroses_ke_2=tombol_input_program_kalkulator_ke_2.get()
		pemroses_ke_2=int(pemroses_ke_2)
		tombol_hasil_penjumlahan.set(int(pemroses+pemroses_ke_2))
		label_program_kalkulator_gui_ke_dua.config(font=("Times New Roman",15,"bold","italic","roman"),fg="darkcyan")


	# BUAT TAMPILAN AWAL GUI PROGRAM NYA, MENGGUNAKAN TKINTER.
	import tkinter as alat_kalkulator_gui
	program_kalkulator_gui=alat_kalkulator_gui.Tk()


	# UBAH WARNA LATAR BELAKANG PROGRAM KALKULATOR PROGRAM GUI NYA,
	# DENGAN METODE .CONFIG(BG="WARNA YANG KAMU PILIH.")
	program_kalkulator_gui.configure(bg="black",cursor="crosshair")


	# UBAH JUDUL ATAU TITLE PROGRAM GUI NYA, DENGAN METODE .TITLE
	program_kalkulator_gui.title("PROGRAM KALKULATOR GUI RUBEN LEONARDO SIGALINGGING")


	# UBAH UKURAN LAYAR PROGRAM GUI NYA.
	program_kalkulator_gui.geometry("1266x768")


	# UBAH TAMPILAN PROGRAM NYA, DENGAN METODE LABEL.
	# GASSS EAAAA, SUPAYA JADI KEREN TAMPILAN PROGRAM NYA, EAAA
	label_program_kalkulator_gui=alat_kalkulator_gui.Label(program_kalkulator_gui,text="GUI Calculator Program By\nRuben Leonardo Sigalingging.",font=("Ubuntu Condensed",25,"bold","italic"),cursor="watch",bd=3,width=50,height=5,bg="darkcyan",fg="darkred",justify=alat_kalkulator_gui.CENTER)
	# BUAT LABEL PROGRAM NYA ON
	label_program_kalkulator_gui.pack()


	# Python - Tkinter Entry
	# Python - Tkinter Entry, AKU UMPAMAKAN SEBAGAI TOMBOL INPUT USER
	tombol_input_program_kalkulator=alat_kalkulator_gui.Entry(program_kalkulator_gui,font=("Times",19,"italic","underline"),width=25,bd=3,justify=alat_kalkulator_gui.CENTER,cursor="exchange",bg="darkgray",fg="darkred")
	tombol_input_program_kalkulator.pack(side="top")


	tombol_input_program_kalkulator_ke_2=alat_kalkulator_gui.Entry(program_kalkulator_gui,font=("Times",19,"italic","underline"),width=25,bd=3,justify=alat_kalkulator_gui.CENTER,cursor="exchange",bg="darkgray",fg="darkred")
	tombol_input_program_kalkulator_ke_2.pack(side="top")


	# BUAT TOMBOL BUTTON ATAU TOMBOL PEMROSES DATA NYA.
	tombol_pemroses_data_user=alat_kalkulator_gui.Button(program_kalkulator_gui,text="Let's Go!",font=("Ubuntu Condensed",19,"underline"),command=program_pemroses,width=25,bd=3,cursor="shuttle",fg="darkgray",bg="darkcyan")
	tombol_pemroses_data_user.pack()


	# TOMBOL HASIL PENJUMLAHAN
	tombol_hasil_penjumlahan=alat_kalkulator_gui.IntVar()
	tombol_hasil_penjumlahan.set("-> Hasil Penjumlahan!")


	# LABEL PROGRAM KE 2:
	label_program_kalkulator_gui_ke_dua=alat_kalkulator_gui.Label(program_kalkulator_gui,font=("Courier",25,"bold","italic"),cursor="pirate",bd=3,width=25,height=5,bg="darkgray",fg="darkred",justify=alat_kalkulator_gui.CENTER,textvariable=tombol_hasil_penjumlahan)
	label_program_kalkulator_gui_ke_dua.pack()


	# BUAT PROGRAM BERJALAN TERUS ATAU TANPA BERHENTI.
	# MENGGUNAKAN METODE .MAINLOOP()
	program_kalkulator_gui.mainloop()
GUI_Calculator_Program()