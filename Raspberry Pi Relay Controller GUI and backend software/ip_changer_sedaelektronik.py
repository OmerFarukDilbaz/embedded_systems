#!/bin/bash
#dos2unix must be setup and convert this file
import tkinter
from tkinter import *
from PIL import Image, ImageTk #ImageTK hatası için terminale şu kodun girilmesi gerekmektedir. sudo apt-get install python3-pil.imagetk
from tkinter import messagebox
import requests
from tkinter import ttk
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

root = Tk()
root.title("SEDA ELEKTRONİK")
root.geometry("700x800")
root.config(bd=0)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady = 15)

my_frame_1 = Frame(my_notebook, width = 700,height=800,bd=0)
my_frame_2 = Frame(my_notebook, width = 700,height=800,bd=0)

my_frame_1.pack(fill="both",expand=1)
my_frame_2.pack(fill="both",expand=1)

my_notebook.add(my_frame_1,text="RELAY/BUTON KONTROL")
my_notebook.add(my_frame_2,text="KONTROL IP DÜZENLEME")



is_on_1 = False
is_on_2 = False
is_on_3 = False
is_on_4 = False
is_on_5 = False
is_on_6 = False
is_on_7 = False
is_on_8 = False
is_on_9 = False
is_on_10 = False
is_on_11 = False
is_on_12 = False
is_on_13 = False
is_on_14 = False
is_on_15 = False
is_on_16 = False

loc = r"./role_urls"

button_in_1 =  9
button_in_2 =  10 
button_in_3 =  11
button_in_4 =  12
button_in_5 =  13
button_in_6 =  16
button_in_7 =  17
button_in_8 =  18
button_in_9 =  19
button_in_10 =  20
button_in_11 =  21
button_in_12 =  22
button_in_13 =  23
button_in_14 =  24
button_in_15 =  25
button_in_16 =  26

GPIO.setup(button_in_1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_5,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_6,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_7,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_8,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_9,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_10,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_11,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_12,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_13,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_14,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_15,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_in_16,GPIO.IN,pull_up_down = GPIO.PUD_UP)
try:
    def ip_list():
        role_keys = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','L','f','g','h','j','k','l','m','n','o','p','q','t','u','v','w','M']
        
        urls_role = list()
        for key in role_keys:
            role_ip = enter_txt.get()
            role_ip = "http://" + role_ip + ":3000" + "/" + key
            urls_role.append(role_ip)
        return urls_role

    def deafult_ip_list():
        role_keys = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','L','f','g','h','j','k','l','m','n','o','p','q','t','u','v','w','M']
        
        urls_role = list()
        for key in role_keys:
            role_ip = "169.254.1.2"
            role_ip = "http://" + role_ip + ":3000" + "/" + key
            urls_role.append(role_ip)
        return urls_role


    def change_ip():
        
        ip = enter_txt.get()
        ip +=":3000"
        info_ip.config(text=ip)
        
        role_urls = ip_list()

        with open(loc, 'r') as file :
            filedata = file.read()
            splitfile = filedata.split(' , ')

        role_urls = ip_list()

        c=0
        for url in role_urls:
            if c==32: c=0
            filedata = filedata.replace(splitfile[c], url,1)
            c+=1
        
        with open(loc, 'w') as file:
            file.write(filedata)
            

       
        
    def default_ip():
        with open(loc, 'r') as file :
            filedata = file.read()
            splitfile = filedata.split(' , ')
      
        ip = "169.254.1.2"
        ip +=":3000"
        info_ip.config(text=ip)
        
        role_urls = deafult_ip_list()

        with open(loc, 'r') as file :
            filedata = file.read()
            splitfile = filedata.split(' , ')
        c=0
        for url in role_urls:
            if c==32: c=0
            filedata = filedata.replace(splitfile[c], url,1)
            c+=1
        
        with open(loc, 'w') as file:
            file.write(filedata)
        messagebox.showinfo("BAŞARILI","YENİ IP = " + ip)

    def button_click(args):
        global is_on_1
        global is_on_2
        global is_on_3
        global is_on_4
        global is_on_5
        global is_on_6
        global is_on_7
        global is_on_8
        global is_on_9
        global is_on_10
        global is_on_11
        global is_on_12
        global is_on_13
        global is_on_14
        global is_on_15
        global is_on_16
        
        with open(loc, 'r') as file :
                filedata = file.read()
                urls = filedata.split(' , ')
            
        if (args == 1 and is_on_1 == False):
            try:
                request = requests.get(urls[0],timeout = 3)
                button_1.config(image = on)
                request.raise_for_status()
                is_on_1 = True
                button_1_label.config(fg="green")
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası","Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
           
        elif (args == 1 and is_on_1 == True):
            try:
                
                button_1.config(image = off)
                request = requests.get(urls[16],timeout=3)
                request.raise_for_status()
                is_on_1 = False
                button_1_label.config(fg="red")
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası","Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 2 and is_on_2 == False):
            try:
                request = requests.get(urls[1],timeout=3)
                request.raise_for_status()
                button_2.config(image = on)
                button_2_label.config(fg="green")
                is_on_2 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 2 and is_on_2 == True):
            try:
                request = requests.get(urls[17],timeout=3)
                request.raise_for_status()
                button_2.config(image = off)
                button_2_label.config(fg="red")
                is_on_2 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 3 and is_on_3 == False):
            try:
                request = requests.get(urls[2],timeout=3)
                request.raise_for_status()
                button_3.config(image = on)
                is_on_3 = True
                button_3_label.config(fg="green")
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
        elif (args == 3 and is_on_3 == True):
            try:
                request = requests.get(urls[18],timeout=3)
                request.raise_for_status()
                button_3.config(image = off)
                button_3_label.config(fg="red")
                is_on_3 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
         
        
        if (args == 4 and is_on_4 == False):
            try:
                request = requests.get(urls[3],timeout=3)
                request.raise_for_status()
                button_4.config(image = on)
                button_4_label.config(fg="green")
                is_on_4 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 4 and is_on_4 == True):
            try:
                request = requests.get(urls[19],timeout=3)
                request.raise_for_status()
                button_4.config(image = off)
                button_4_label.config(fg="red")
                is_on_4 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 5 and is_on_5 == False):
            try:
                request = requests.get(urls[4],timeout=3)
                request.raise_for_status()
                button_5.config(image = on)
                button_5_label.config(fg="green")
                is_on_5 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 5 and is_on_5 == True):
            try:
                request = requests.get(urls[20],timeout=3)
                request.raise_for_status()
                button_5.config(image = off)
                button_5_label.config(fg="red")
                is_on_5 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
            
        if (args == 6 and is_on_6 == False):
            try:
                request = requests.get(urls[5],timeout=3)
                request.raise_for_status()
                button_6.config(image = on)
                button_6_label.config(fg="green")
                is_on_6 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 6 and is_on_6 == True):
            try:
                request = requests.get(urls[21],timeout=3)
                request.raise_for_status()
                button_6.config(image = off)
                button_6_label.config(fg="red")
                is_on_6 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 7 and is_on_7 == False):
            try:
                request = requests.get(urls[6],timeout=3)
                request.raise_for_status()
                button_7.config(image = on)
                button_7_label.config(fg="green")
                is_on_7 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 7 and is_on_7 == True):
            try:
                request = requests.get(urls[22],timeout=3)
                request.raise_for_status()
                button_7.config(image = off)
                button_7_label.config(fg="red")
                is_on_7 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 8 and is_on_8 == False):
            try:
                request = requests.get(urls[7],timeout=3)
                request.raise_for_status()
                button_8.config(image = on)
                button_8_label.config(fg="green")
                is_on_8 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 8 and is_on_8 == True):
            try:
                request = requests.get(urls[23],timeout=3)
                request.raise_for_status()
                button_8.config(image = off)
                button_8_label.config(fg="red")
                is_on_8 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 9 and is_on_9 == False):
            try:
                request = requests.get(urls[8],timeout=3)
                request.raise_for_status()
                button_9.config(image = on)
                button_9_label.config(fg="green")
                is_on_9 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 9 and is_on_9 == True):
            try:
                request = requests.get(urls[24],timeout=3)
                request.raise_for_status()
                button_9.config(image = off)
                button_9_label.config(fg="red")
                is_on_9 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 10 and is_on_10 == False):
            try:
                request = requests.get(urls[9],timeout=3)
                request.raise_for_status()
                button_10.config(image = on)
                button_10_label.config(fg="green")
                is_on_10 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 10 and is_on_10 == True):
            try:
                request = requests.get(urls[25],timeout=3)
                request.raise_for_status()
                button_10.config(image = off)
                button_10_label.config(fg="red")
                is_on_10 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 11 and is_on_11 == False):
            try:
                request = requests.get(urls[10],timeout=3)
                request.raise_for_status()
                button_11.config(image = on)
                button_11_label.config(fg="green")
                is_on_11 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 11 and is_on_11 == True):
            try:
                request = requests.get(urls[26],timeout=3)
                request.raise_for_status()
                button_11.config(image = off)
                button_11_label.config(fg="red")
                is_on_11 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 12 and is_on_12 == False):
            try:
                request = requests.get(urls[11],timeout=3)
                request.raise_for_status()
                button_12.config(image = on)
                button_12_label.config(fg="green")
                is_on_12 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 12 and is_on_12 == True):
            try:
                request = requests.get(urls[27],timeout=3)
                request.raise_for_status()
                button_12.config(image = off)
                button_12_label.config(fg="red")
                is_on_12 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 13 and is_on_13 == False):
            try:
                request = requests.get(urls[12],timeout=3)
                request.raise_for_status()
                button_13.config(image = on)
                button_13_label.config(fg="green")
                is_on_13 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 13 and is_on_13 == True):
            try:
                request = requests.get(urls[28],timeout=3)
                request.raise_for_status()
                button_13.config(image = off)
                button_13_label.config(fg="red")
                is_on_13 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 14 and is_on_14 == False):
            try:
                request = requests.get(urls[13],timeout=3)
                request.raise_for_status()
                button_14.config(image = on)
                button_14_label.config(fg="green")
                is_on_14 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 14 and is_on_14 == True):
            try:
                request = requests.get(urls[29],timeout=3)
                request.raise_for_status()
                button_14.config(image = off)
                button_14_label.config(fg="red")
                is_on_14 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 15 and is_on_15 == False):
            try:
                request = requests.get(urls[14],timeout=3)
                request.raise_for_status()
                button_15.config(image = on)
                button_15_label.config(fg="green")
                is_on_15 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 15 and is_on_15 == True):
            try:
                request = requests.get(urls[30],timeout=3)
                request.raise_for_status()
                button_15.config(image = off)
                button_15_label.config(fg="red")
                is_on_15 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        
        if (args == 16 and is_on_16 == False):
            try:
                request = requests.get(urls[15],timeout=3)
                request.raise_for_status()
                button_16.config(image = on)
                button_16_label.config(fg="green")
                is_on_16 = True
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
        elif (args == 16 and is_on_16 == True):
            try:
                request = requests.get(urls[31],timeout=3)
                request.raise_for_status()
                button_16.config(image = off)
                button_16_label.config(fg="red")
                is_on_16 = False
            except requests.ConnectionError:
                messagebox.showerror("Bağlantı Hatası",
                "Ethernet Röle Kartı Bulunamadı. Lütfen IP adresinizi kontrol ediniz.")
            
    def check_ip_address():
        with open(loc, 'r') as file :
            filedata = file.read()
            splitfile = filedata.split(' , ')
        splitfile_2 =splitfile[0].split(':')
        ip = splitfile_2[0]+":"+splitfile_2[1]
        ip +=":3000"
        info_ip.config(text=ip)
        

    def check_button ():
        global is_on_1
        global is_on_2
        global is_on_3
        global is_on_4
        global is_on_5
        global is_on_6
        global is_on_7
        global is_on_8
        global is_on_9
        global is_on_10
        global is_on_11
        global is_on_12
        global is_on_13
        global is_on_14
        global is_on_15
        global is_on_16
        
        if GPIO.input(button_in_1)==0:
            is_on_1 = True
            button_1.config(image = on)
            button_1_label.config(fg="green")
        if GPIO.input(button_in_1)==1:
            button_1.config(image = off)
            button_1_label.config(fg="red")
        if GPIO.input(button_in_2)==0:
            is_on_2 = True
            button_2.config(image = on)
            button_2_label.config(fg="green")
        if GPIO.input(button_in_2)==1:
            button_2.config(image = off)
            button_2_label.config(fg="red")
        if GPIO.input(button_in_3)==0:
            is_on_3 = True
            button_3.config(image = on)
            button_3_label.config(fg="green")
        if GPIO.input(button_in_3)==1:
            button_3.config(image = off)
            button_3_label.config(fg="red")
        if GPIO.input(button_in_4)==0:
            is_on_4 = True
            button_4.config(image = on)
            button_4_label.config(fg="green")
        if GPIO.input(button_in_4)==1:
            button_4.config(image = off)
            button_4_label.config(fg="red")
        if GPIO.input(button_in_5)==0:
            is_on_5 = True
            button_5.config(image = on)
            button_5_label.config(fg="green")
        if GPIO.input(button_in_5)==1:
            button_5.config(image = off)
            button_5_label.config(fg="red")
        if GPIO.input(button_in_6)==0:
            is_on_6 = True 
            button_6.config(image = on)
            button_6_label.config(fg="green")
        if GPIO.input(button_in_6)==1:
            button_6.config(image = off)
            button_6_label.config(fg="red")
        if GPIO.input(button_in_7)==0:
            is_on_7 = True
            button_7.config(image = on)
            button_7_label.config(fg="green")
        if GPIO.input(button_in_7)==1:
            button_7.config(image = off)
            button_7_label.config(fg="red")
        if GPIO.input(button_in_8)==0:
            is_on_8 = True
            button_8.config(image = on)
            button_8_label.config(fg="green")
        if GPIO.input(button_in_8)==1:
            button_8.config(image = off)
            button_8_label.config(fg="red")
        if GPIO.input(button_in_9)==0:
            is_on_9 = True
            button_9.config(image = on)
            button_9_label.config(fg="green")
        if GPIO.input(button_in_9)==1:
            button_9.config(image = off)
            button_9_label.config(fg="red")
        if GPIO.input(button_in_10)==0:
            is_on_10 = True
            button_10.config(image = on)
            button_10_label.config(fg="green")
            
        if GPIO.input(button_in_10)==1:
            button_10.config(image = off)
            button_10_label.config(fg="red")
        if GPIO.input(button_in_11)==0:
            is_on_11 = True
            button_11.config(image = on)
            button_11_label.config(fg="green")
        if GPIO.input(button_in_11)==1:
            button_11.config(image = off)
            button_11_label.config(fg="red")
        if GPIO.input(button_in_12)==0:
            is_on_12 = True
            button_12.config(image = on)
            button_12_label.config(fg="green")
        if GPIO.input(button_in_12)==1:
            button_12.config(image = off)
            button_12_label.config(fg="red")
        if GPIO.input(button_in_13)==0:
            is_on_13 = True
            button_13.config(image = on)
            button_13_label.config(fg="green")
        if GPIO.input(button_in_13)==1:
            button_13.config(image = off)
            button_13_label.config(fg="red")
        if GPIO.input(button_in_14)==0:
            is_on_14 = True
            button_14.config(image = on)
            button_14_label.config(fg="green")
        if GPIO.input(button_in_14)==1:
            button_14.config(image = off)
            button_14_label.config(fg="red")
        if GPIO.input(button_in_15)==0:
            is_on_15 = True
            button_15.config(image = on)
            button_15_label.config(fg="green")
        if GPIO.input(button_in_15)==1:
            button_15.config(image = off)
            button_15_label.config(fg="red")
        if GPIO.input(button_in_16)==0:
            is_on_16 = True
            button_16.config(image = on)
            button_16_label.config(fg="green")
        if GPIO.input(button_in_16)==1:
            button_16.config(image = off)
            button_16_label.config(fg="red")
        

   


    heading = Label(my_frame_1, text = "KONTROL-IP'si DEĞİŞİTİRME PROGRAMI",font=("Trebucet MS",20,"bold"),bd=0,fg="black")
    heading.pack(pady=(50,0))
    heading.place(x=50,y=150)
    
    enter_txt = Entry(my_frame_1,justify="center",width=30,font=("poppins",25),bg="white",border=2)
    enter_txt.pack(pady=10)
    enter_txt.focus()
    enter_txt.place(x=30,y=215)

    button_degistir = Button(my_frame_1,text="Değiştir",font=("arial",20,"bold"),foreground="white",bg="red",command=change_ip)
    button_degistir.pack()
    button_degistir.place(x=445,y=304)

    button_default = Button(my_frame_1,text="Default",font=("arial",20,"bold"),foreground="white",bg="red",command=default_ip)
    button_default.pack()
    button_default.place(x=125,y=304)
    
    button_bc = Button(my_frame_2,text="BUTON RÖLE DURUMLARI",font=("arial",20,"bold"),foreground="white",bg="red",command=check_button)
    button_bc.pack()
    button_bc.place(x=170,y=650)

    info_ip = Label(my_frame_1,text="",font=("poppins",20),bd=0,fg="black")
    info_ip.place(x=377,y=400)

    cs = Label(my_frame_1,text="Kullanılan IP Adres : ",font=("poppins",20,"bold"),bd=0,fg="black",)
    cs.place(x=60,y=400)

    image1 = Image.open(r"./sedaelektronik_logo.png")
    logo = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(my_frame_1,image=logo)
    label1.image = logo
    label1.place(x=250, y=40)
    
    label2 = tkinter.Label(my_frame_2,image=logo)
    label2.image = logo
    label2.place(x=250, y=40)

    on = PhotoImage(file = r"./on.png")
    off = PhotoImage(file = r"./off.png")

    button_1 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(1))
    button_1.pack()
    button_1.place(x=190,y=200)
    button_1_label = Label(my_frame_2,text="-RELAY 1-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_1_label.place(x=55,y=205)

    button_2 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(2))
    button_2.pack()
    button_2.place(x=190,y=250)
    button_2_label = Label(my_frame_2,text="-RELAY 2-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_2_label.place(x=55,y=255)


    button_3 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(3))
    button_3.pack()
    button_3.place(x=190,y=300)
    button_3_label = Label(my_frame_2,text="-RELAY 3-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_3_label.place(x=55,y=305)

    button_4 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(4))
    button_4.pack()
    button_4.place(x=190,y=350)
    button_4_label = Label(my_frame_2,text="-RELAY 4-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_4_label.place(x=55,y=355)

    button_5 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(5))
    button_5.pack()
    button_5.place(x=190,y=400)
    button_5_label = Label(my_frame_2,text="-RELAY 5-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_5_label.place(x=55,y=405)

    button_6 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(6))
    button_6.pack()
    button_6.place(x=190,y=450)
    button_6_label = Label(my_frame_2,text="-RELAY 6-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_6_label.place(x=55,y=455)

    button_7 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(7))
    button_7.pack()
    button_7.place(x=190,y=500)
    button_7_label = Label(my_frame_2,text="-RELAY 7-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_7_label.place(x=55,y=505)

    button_8 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(8))
    button_8.pack()
    button_8.place(x=190,y=550)
    button_8_label = Label(my_frame_2,text="-RELAY 8-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_8_label.place(x=55,y=555)

    button_9 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(9))
    button_9.pack()
    button_9.place(x=410,y=200)
    button_9_label = Label(my_frame_2,text="-RELAY 9-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_9_label.place(x=525,y=205)

    button_10 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(10))
    button_10.pack()
    button_10.place(x=410,y=250)
    button_10_label = Label(my_frame_2,text="-RELAY 10-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_10_label.place(x=525,y=255)

    button_11 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(11))
    button_11.pack()
    button_11.place(x=410,y=300)
    button_11_label = Label(my_frame_2,text="-RELAY 11-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_11_label.place(x=525,y=305)

    button_12 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(12))
    button_12.pack()
    button_12.place(x=410,y=350)
    button_12_label = Label(my_frame_2,text="-RELAY 12-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_12_label.place(x=525,y=355)

    button_13 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(13))
    button_13.pack()
    button_13.place(x=410,y=400)
    button_13_label = Label(my_frame_2,text="-RELAY 13-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_13_label.place(x=525,y=405)


    button_14 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(14))
    button_14.pack()
    button_14.place(x=410,y=450)
    button_14_label = Label(my_frame_2,text="-RELAY 14-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_14_label.place(x=525,y=455)

    button_15 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(15))
    button_15.pack()
    button_15.place(x=410,y=500)
    button_15_label = Label(my_frame_2,text="-RELAY 15-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_15_label.place(x=525,y=505)

    button_16 = Button(my_frame_2,image = off,bd=0,command=lambda:button_click(16))
    button_16.pack()
    button_16.place(x=410,y=550)
    button_16_label = Label(my_frame_2,text="-RELAY 16-",font=("poppins",16,"bold"),bd=0,fg="red")
    button_16_label.place(x=525,y=555)
    my_frame_2.after(1,check_ip_address)
    my_frame_2.after(1,check_button)
    
    my_frame_2.mainloop()
    
except:
    tkinter.messagebox.showwarning(title="HATA MESAJI", message="LÜTFEN DOĞRU BİR IP ADRESİ GİRİNİZ")
   
                                                                                                                                                                                     		 






