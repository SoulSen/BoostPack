from tkinter import Label, Text, Button, PhotoImage, messagebox, Image, Scale, HORIZONTAL
from fetcher import Fetcher
import tkinter


class InstallerGUI:
    def __init__(self, master):
        self.master = master
        self.ram = None 
        self.fetcher = Fetcher()

        master.title('BoostPack v2 Installer')
        master.geometry('500x500')
        master.iconbitmap('assets/output_onlinepngtools_ZGQ_icon.ico')

        img = PhotoImage(file='assets/install.png')
        self.install = Button(master, image=img, command=self.install, borderwidth=0)
        self.install.image = img 
        self.install.pack()

        img = PhotoImage(file='assets/uninstall.png')
        self.uninstall = Button(master, image=img, command=self.uninstall, borderwidth=0)
        self.uninstall.image = img
        self.uninstall.pack()

        img = PhotoImage(file='assets/update.png')
        self.update = Button(master, image=img, command=self.update_patcher, borderwidth=0)
        self.update.image = img
        self.update.pack()

        self.txt = Label(master, text='Ram')
        self.txt.pack()

        self.ram = Scale(master, from_=1, to=self.fetcher.get_ram, orient=HORIZONTAL, command=self.set_ram)
        self.ram.pack()

    def install(self):
        master.title('BoostPack v2 Installer [INSTALLING]')
        self.fetcher.ram = self.ram 
        self.fetcher.install_modpack()
        messagebox.showinfo(title='BoostPack v2',
                            message='Succesfully installed BoostPack v2')
        master.title('BoostPack v2 Installer')

    def uninstall(self):
        result = messagebox.askyesno(title='BoostPack v2', 
                                     message='Are you sure you want to uninstall BoostPack v2?')

        if result == 'yes':
            master.title('BoostPack v2 Installer [UNINSTALLING]')
            patcher.uninstall_patcher()
            messagebox.showinfo(title='BoostPack v2',
                                message='Succesfully uninstalled BoostPack v2')
        master.title('BoostPack v2 Installer')

    def update_patcher(self):
        master.title('BoostPack v2 Installer [UPDATING]')
        self.fetcher.update_modpack()
        messagebox.showinfo(title='BoostPack v2',
                            message='Succesfully updated BoostPack v2')     
        master.title('BoostPack v2 Installer') 

    def set_ram(self, val):
        print('hello')
        self.ram = val 

