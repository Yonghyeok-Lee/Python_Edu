from tkinter import * 
from tkinter import ttk
import random

# funtion
results = []

def Gacha():
    global results
    if not results:
        label1.config(text="Go Edit")
    else:
        label1.config(text=str(random.choice(results)))

def addList():
    global results
    results.append(entry.get())
    if not entry.get():
        return results.pop()
    listbox.insert(END, entry.get())
    entry.delete(0, "end")

def delList():
    global results
    selection = listbox.curselection()
    if(len(selection)==0):
        return
    value = listbox.get(selection[0])
    index = results.index(value)
    length = len(selection)
    del results[index:]
    listbox.delete(selection[0], (length+1))
    print(results)

def savList():
    global results
    if not results:
        return buttonSav.config(text="No List")
    sav = open("C:/Users/yh/Desktop/Eatcha.txt", "a")
    for i in results:
        data = "name: " + i + "\n"
        sav.write(data)
    sav.close()
    buttonSav.config(text="Complete")
    print(sav)

# default setting
root = Tk()

root.title("eatcha~")
root.geometry("400x300+100+100")
root.resizable(False, False)

# make frame
notebook = ttk.Notebook(root, width=350, height=250)
notebook.pack()

# frame No.1
frame1 = Frame(root)
notebook.add(frame1, text="Gacha")
label1 = Label(frame1, text="GOGOGOGOGOGOGO", height=5, padx=2, pady=2, font=('arial', 17, 'normal'))
label1.pack()

buttonPick = Button(frame1, width=12, height=3, text="Eatcha!!!", font=('arial', 12, 'bold'), overrelief="solid", command=Gacha)
buttonPick.pack()

# frame No.2
frame2 = Frame(root)
notebook.add(frame2, text="Edit")
label2 = Label(frame2, text="Setting List", font=('arial', 12, 'normal'), padx=7)
label2.grid(row=0, column=0, sticky='N') 

listbox = Listbox(frame2, selectmode="extended")
for i in range(len(results)):
    listbox.insert(END, results[i]),
    listbox.insert(len(listbox), results[i])
listbox.grid(row=0, column=2, sticky='N') 

buttonAdd = Button(frame2, width=5, padx=2, text="Add", overrelief="solid", command=addList)
buttonAdd.grid(row=2, column=3, sticky='w') 

buttonDel = Button(frame2, width=5, padx=2, text="Delete", overrelief="solid", command=delList)
buttonDel.grid(row=2, column=4, sticky='E')

entry = Entry(frame2)
entry.grid(row=2, column=2, sticky='w', padx=5)

buttonSav = Button(frame2, width=19, padx=2, text="Save", overrelief="solid", command=savList)
buttonSav.grid(row=5, column=2, sticky='S')

# frame No.3
frame3 = Frame(root)
notebook.add(frame3, text="result")
label3 = Label(frame3, text="test_page_3")
label3.pack()

# Main
root.mainloop()
