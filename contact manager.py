from tkinter import *
from tkinter import messagebox
#========GUI========
win = Tk()
win.geometry('400x400')
win.configure(bg = '#FFCC66')
win.title('Contct Management')

#========Def========
def insert():
    fname= ent_fname.get()
    lname=ent_lname.get()
    city=ent_city.get()
    tel=ent_tel.get()
        
    lstbox.insert(END,fname + ','+lname+','+city+','+tel)    
        
def exit_():
    result = messagebox.askyesno('EXIT','Are you sure \nyou want leave.')
    if result == True:
        win.destroy()

def fetch():
    clean()
    index = lstbox.curselection()
    data = lstbox.get(index)
    ldata = data.split(',')
    ent_fname.insert(0,ldata[0])
    ent_lname.insert(0,ldata[1])
    ent_city.insert(0,ldata[2])
    ent_tel.insert(0,ldata[3])
 

def clean():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
 
def delete():
    index = lstbox.curselection()
    res = lstbox.delete(index)
    ent_fname.insert(index,res[0])
    ent_lname.insert(index,res[1])
    ent_city.insert(index,res[2])
    ent_tel.insert(index,res[3])


#========LABELS========
lbl_fname = Label(text= 'Fname:',font='arial 11',bg= '#FFCC66')
lbl_fname.place(x=15,y=15)

lbl_lname = Label(text= 'Lname:',font='arial 11',bg= '#FFCC66')
lbl_lname.place(x=200,y=15)

lbl_city = Label(text= 'City:',font='arial 11',bg= '#FFCC66')
lbl_city.place(x=35,y=70)

lbl_Tel = Label(text= 'Tel:',font='arial 11',bg= '#FFCC66')
lbl_Tel.place(x=225,y=70)

#========ENTRY========
ent_fname= Entry(width='15')
ent_fname.place(y=15,x=70)

ent_lname= Entry(width='15')
ent_lname.place(y=15,x=255)

ent_city= Entry(width='15')
ent_city.place(y=70,x=70)

ent_tel= Entry(width='15')
ent_tel.place(y=70,x=255)

#========List Box========
lstbox = Listbox(width= 30,height= 15)
lstbox.place(y= 130, x = 50)

#========Button========
btn_insert= Button(text='Insert',command=insert)
btn_insert.place(x=300,y=130)

btn_delete= Button(text='Delete',command=delete)
btn_delete.place(x=300,y=170)

btn_clean= Button(text='Clean',command=clean)
btn_clean.place(x=300,y=210)

btn_Fetch= Button(text='Fetch',command=fetch)
btn_Fetch.place(x=300,y=250)

btn_exit= Button(text='Exit',command=exit_)
btn_exit.place(x=300,y=290)

 













win.mainloop()