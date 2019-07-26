from tkinter import * 
from tkinter import ttk
import random

# funtion
lists = []
results = []
kids = []
pick = []
sav = {}

count = 0

def makeResults(pick):
    global lists
    global results
    global count
    
    results = []
    for i in lists:
        results.append(i)
    if pick:
        for i in pick:
            if i in results:
                results.remove(i)

    print(results)

def Produce101():
    global count
    global pick
    global kids
    global sav

    pick.append(random.choice(kids))
    
    print('count: ', count, 'pick: ', pick[count])
    
    count += 1

    print(len(kids), pick)

def Gacha():
    global lists
    global results
    global kids
    global count

    if not lists:
        label1.config(text="Go Edit")

    else:
        kids = []
        stock = int(10000/len(lists))
        penalty = int(stock*0.05)
        chance = int(stock*0.01)

        makeResults(pick)

        if count == 0:
            for i in lists:
                for j in range(stock):
                    kids.append(i)
            
        elif count == 1:
            kids = []

            pick_cal = stock - penalty
            results_cal = int((10000-pick_cal)/len(results))

            for i in range(pick_cal):
                kids.append(pick[count-1])

            for i in results:
                for j in range(results_cal):
                    kids.append(i)

        else:
            kids = []

            double_cal = stock - penalty - chance
            chance_cal = stock - chance
            results_cal = int((10000-double_cal)/len(lists))

            print(len(lists), len(results), double_cal, chance_cal, results_cal)

            for i in pick:
                for j in range(chance_cal):
                    kids.append(i)
                print('append pick: ', len(kids)) 

            for i in results:
                for j in range(int(results_cal/len(results))):
                    kids.append(i)
                print('append results: ', len(kids)) 

            if pick[count-1] == pick[count-2]:
                for j in range(double_cal):
                    kids.append(pick[count-1])
                print('append other: ', len(kids))

        Produce101()

        sav = open("C:/Users/yh/Desktop/Eatcha.txt", "a")
        for i in lists:
            data = "name: " + i + "\n"
            sav.write(data)
        sav.close()

        label1.config(text=str(pick[count-1]))

def addList():
    global lists
    lists.append(entry.get())
    if not entry.get():
        return lists.pop()
    listbox.insert(END, entry.get())
    entry.delete(0, "end")

def delList():
    global lists
    selection = listbox.curselection()
    if(len(selection)==0):
        return
    value = listbox.get(selection[0])
    index = lists.index(value)
    length = len(selection)
    del lists[index:]
    listbox.delete(selection[0], (length+1))

def savList():
    global lists
    if not lists:
        return buttonSav.config(text="No List")
    sav = open("C:/Users/yh/Desktop/Eatcha.txt", "a")
    for i in lists:
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
for i in range(len(lists)):
    listbox.insert(END, lists[i]),
    listbox.insert(len(listbox), lists[i])
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
