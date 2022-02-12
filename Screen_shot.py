#pip install pyautogui
import pyautogui


def Screeenshot():
    try:
        a = TI1.get()
        b = file.get()
        pyautogui.screenshot(a+'.'+b)
        t = 'ใส่ชื่อไฟล์'
        v2_result.set(t)
    except:
        t = 'โปรดใส่ชื่อไฟล์ให้ถูกต้อง'
        v2_result.set(t)


#GUI#
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('230x160')
GUI.title('Screenshot')
FONT1 = ('Tahoma' ,20,'bold')
FONT2 = ('Tahoma' ,15)
FONT3 = ('' ,15)
FONT4 = ('' ,10)

v2_result = StringVar()
v2_result.set('ใส่ชื่อไฟล์')
R2 = ttk.Label(textvariable = v2_result,font = FONT3)
R2.pack()

filelist = ['png', 'pdf', 'jpeg', 'gif']
file = ttk.Combobox(GUI, values = filelist,width = 4 ,font = FONT4, state = 'readonly')
file.current(0)
file.pack(ipadx=5,ipady=1)
L5 = ttk.Label(GUI,text ='',font = ('',2))
L5.pack()

TI1 = ttk.Entry(GUI)
TI1.pack(ipadx=25,ipady=4)
L5 = ttk.Label(GUI,text ='',font = ('',2))
L5.pack()

B2 = ttk.Button(GUI,text='Screenshot!',command= Screeenshot)
B2.pack(ipadx=50,ipady=5)

GUI.mainloop()