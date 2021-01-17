from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
import time
from ctypes import *
#-----------------------------------------------
import csv
import sys
import os
from os import path
#------------------------------------------------
from tkinter import *
import tkinter 
from tkinter import messagebox
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import ttk
#-----------------------------------------------
webobject = webdriver.Chrome()
csvpath=path("C:\Users\Dell\Documents\AdBot") # <<<<Need Write to create CSV Here My document

#getpassword=StringVar()
#getusername=StringVar()
username = ""
password = ""
goforward=False
#----------------------------------------------------------------------------------
#---------------------------------UI-----------------------------------------------
botui= Tk()
botui.title("Ads Click Bot - AdBot V1.01")
botui.geometry('240x70')
botui.eval('tk::PlaceWindow %s center' % botui.winfo_toplevel())
#-----------------------------------------------------------------------------------
#----------Arrangemets------------------------
usernameLabel = Label(botui, text="  User Name       ").grid(row=0, column=0)
getusername  = StringVar()
usernameEntry = Entry(botui,textvariable = getusername ).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(botui,text="   Password       ").grid(row=1, column=0)  
getpassword = StringVar()
passwordEntry = Entry(botui, textvariable=getpassword, show='*').grid(row=1, column=1)
#----------------------------------------------------------------------------------

#------------------------------------------------------------------------------------

def contine():
    with open("Data.csv") as file:
            #messagebox.showinfo('AdBot 1.01', 'csv is availble')
            reader=list(csv.reader(file))
            userdata= str(reader[2])
            password= userdata.split(',', 1)[1]
            username= userdata.split(',',1)[0]
            password= password[2:]
            passlen=len(password)
            password=password[:passlen-2]
            username=username[2:]
            userlen=len(username)
            username=username[:userlen-1]
    webobject.get("https://www.star-clicks.com/default")
    signinlink=webobject.find_element_by_link_text("SIGN IN")
    signinlink.click()
    emaillogging = webobject.find_element_by_id("Email")
    time.sleep(3)
    emaillogging.clear()
    time.sleep(1)
    #messagebox.showinfo('AdBot 1.01', username)
    emaillogging.send_keys(username)
    Passwordadd = webobject.find_element_by_id("Password")
    time.sleep(1)
    Passwordadd.clear()
    time.sleep(1)
    #messagebox.showinfo('AdBot 1.01', password)
    Passwordadd.send_keys(password)
    time.sleep(1)
    #print(password)
    submitbutoon = webobject.find_element_by_id("Button1")
    submitbutoon.click()
    time.sleep(15)
    ppcclick()
#-----------------------------------------------------------------------------------
def run():
    if not os.path.isfile('./Data.csv') == True:
        messagebox.showinfo('AdBot 1.01', 'Please Enter User Details')
    else:
        #messagebox.showinfo('AdBot 1.01', username)
        #messagebox.showinfo('AdBot 1.01', password)
        contine()
        #username,password =reader[1]
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
def clicked():
    with open("Data.csv","w") as file:
        #messagebox.showinfo('AdBot 1.01', 'csv not availble')
        writer=csv.writer(file)
        writer.writerow(["LogingEmail:", "Password"])
        username = str(getusername.get())
        password = str(getpassword.get())
        writer.writerow([username,password])
        
        webobject.get("https://www.star-clicks.com/default")
        signinlink=webobject.find_element_by_link_text("SIGN IN")
        signinlink.click()
        emaillogging = webobject.find_element_by_id("Email")
        time.sleep(3)
        emaillogging.clear()
        time.sleep(1)
        #messagebox.showinfo('AdBot 1.01', username)
        emaillogging.send_keys(username)
        Passwordadd = webobject.find_element_by_id("Password")
        time.sleep(1)
        Passwordadd.clear()
        time.sleep(1)
        #messagebox.showinfo('AdBot 1.01', password)
        Passwordadd.send_keys(password)
        time.sleep(1)
        #print(password)
        submitbutoon = webobject.find_element_by_id("Button1")
        submitbutoon.click()
        time.sleep(15)
        ppcclick()
        
def exitit():
    webobject.close()
    botui.destroy()
    sys.exit("All Works Done !")
    
#------------------------------------------------------------------

#------------------------------------------------------------------
def clickallads(turn):
    for count in range(1,int(turn)):
        if len(webobject.find_elements_by_id("BasicModulem9_11"))>0:
            adclick = webobject.find_element_by_id("BasicModulem9_11")
            adclick.click()
            webobject.switch_to.window(webobject.window_handles[1])
            time.sleep(5)
            webobject.close()
            webobject.switch_to.window(webobject.window_handles[0])
            time.sleep(5)
        else :
            signoutt = webobject.find_element_by_link_text("Sign out") 
            signoutt.click()
            time.sleep(5)
            exitit()
            #webobject.close()
            
            
def ppcclick():
    if webobject.current_url == "https://www.star-clicks.com/portal/manage":
        ppcads = webobject.find_element_by_link_text("PPC Ads")
        ppcads.click()
        time.sleep(5)
        clickallads(25)
    else:
        #webobject.close()
        messagebox.showinfo('AdBot 1.01', 'User Details Incorrect, Change > .csv')
    
        
#-------------------------------------------------------------------------------
#----------Menus------------------
menu = Menu(botui)

new_item = Menu(menu)

    
    

new_item.add_command(label='Save', command=clicked)

new_item.add_command(label='Exit',command = exitit)

menu.add_cascade(label='File', menu=new_item)
botui.config(menu=menu)

#----------Arrangemets------------------------
usernameLabel = Label(botui, text="  User Name       ").grid(row=0, column=0)
getusername  = StringVar()
usernameEntry = Entry(botui,textvariable = getusername ).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(botui,text="   Password       ").grid(row=1, column=0)  
getpassword = StringVar()
passwordEntry = Entry(botui, textvariable = getpassword, show='*').grid(row=1, column=1)
#----------------------------------------------------------------------------------
botui.protocol("WM_DELETE_WINDOW", exitit)
run()
botui.mainloop()