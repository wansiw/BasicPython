from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปรแกรมบันทึกการปลูกผัก',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
########################
def Button2():
    text = 'เริ่มปลูกวันที่ 20/02/23'
    messagebox.showinfo('ปลูกผักวันที่',text)
def Button3():
    text = 'ใส่ปุ๋ยวันที่ 1/03/23'
    messagebox.showinfo('ใส่ปุ๋ยผักวันที่',text)
def Button4():
    text = 'เก็บเกี๋ยววันที่ 30/03/23'
    messagebox.showinfo('เก็บเกี๋ยววันที่เท่าไหร่',text)

    

FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1 , text='เริ่มปลูกวันที่เท่าไหร่',command=Button2)
B2.pack(ipadx=20,ipady=20)

FB2 = Frame(GUI)
FB2.place(x=100,y=200)
B3 = ttk.Button(FB2 , text='ใส่ปุ๋ยวันที่เท่าไหร่',command=Button3)
B3.pack(ipadx=20,ipady=20)


FB3 = Frame(GUI)
FB3.place(x=100,y=300)
B4 = ttk.Button(FB3 , text='จะเก็บเกี่ยววันไหน',command=Button4)
B4.pack(ipadx=20,ipady=20)

########################


GUI.mainloop()
