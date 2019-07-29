from tkinter import * 
from tkinter import ttk
import random

# funtion
lists = []
kids = []
pick = []
sav = {}
count = 0

def Produce101():
    global pick

    pick.insert(0, random.choice(lists))
    lists.remove(pick[0])
    lists.append(pick[0])

def Gacha():
    global lists
    global kids
    global pick
    global count

    if not lists:
        label1.config(text="Go Edit")

    else:
        kids = []
        st = int(len(lists) / 2)
        amount = int(10000 / len(lists))

        amount_pick = int(amount*0.05)
        amount_sel = int(amount*0.02)
        amount_div = int(amount_pick / len(lists))

        amount_total = amount + amount_div + int((amount_sel*(count-1))/len(lists))
        st_total = amount + amount_div + int((amount_sel*st)/len(lists))

        excep_pick = int(amount*0.07)
        excep_sel = int(amount*0.03)
        excep_div = int(excep_pick /len(lists))

        excep_amount_total = amount + excep_div + int((excep_sel*(count-1))/len(lists))
        excep_st_total = amount + excep_div + int((excep_sel*st)/len(lists))

        Produce101()

        if count == 0:
            for i in range(len(lists)):
                for j in range(amount):
                    kids.append(lists[i])
            print('a ', len(kids))

        if count == 1:
            for i in range(len(lists)-1):
                for j in range(amount+amount_div):
                    kids.append(lists[i])

            for i in range(amount-amount_pick):
                kids.append(lists[len(lists)-1])

            while len(kids) < 10000:
                kids.append(random.choice(lists))
                if len(kids) == 10000:
                    break
            print('b ', len(kids))

        if count > 1 and count < st:
            if pick[0] == lists[len(lists)-1]:
                for i in range(len(lists)-count):
                    for j in range(excep_amount_total):
                        kids.append(lists[i])

                for i in range(amount-excep_pick):
                    kids.append(lists[len(lists)-1])

                for i in range(len(lists)-count, len(lists)-1):
                    for j in range(amount-excep_sel):
                        kids.append(lists[i]) 

            else:
                for i in range(len(lists)-count):
                    for j in range(amount_total):
                        kids.append(lists[i])

                for i in range(amount-amount_pick):
                    kids.append(lists[len(lists)-1])

                for i in range(len(lists)-count, len(lists)-1):
                    for j in range(amount-amount_sel):
                        kids.append(lists[i])

            while len(kids) < 10000:
                kids.append(random.choice(lists))
                if len(kids) == 10000:
                    break

            print('c ', len(kids))


        if count >= st:
            if pick[0] == lists[len(lists)-1]:
                for i in range(st):
                    for j in range(excep_st_total):
                        kids.append(lists[i])

                for i in range(amount-excep_pick):
                    kids.append(lists[len(lists)-1])

                for i in range(st, len(lists)-1):
                    for j in range(amount-excep_sel):
                        kids.append(lists[i])

            else:
                for i in range(st):
                    for j in range(st_total):
                        kids.append(lists[i])

                for i in range(amount-amount_pick):
                    kids.append(lists[len(lists)-1])

                for i in range(st, len(lists)-1):
                    for j in range(amount-amount_sel):
                        kids.append(lists[i])  

            while len(kids) < 10000:
                kids.append(random.choice(lists))
                if len(kids) == 10000:
                    break
            print('d ', len(kids))



        print(len(kids), lists)

        print('pick: ', lists[len(lists)-1], 'pickList: ', pick, 'count: ', count)
        count += 1
        print('1: ', kids.count(lists[0]))
        print('2: ', kids.count(lists[1]))
        print('3: ', kids.count(lists[2]))
        print('4: ', kids.count(lists[3]))

        sav = open("C:/Users/yh/Desktop/Eatcha.txt", "a")
        for i in lists:
            data = "name: " + i + "\n"
            sav.write(data)
        sav.close()

        label1.config(text=str(lists[len(lists)-1]))

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
    del lists[index]
    listbox.delete(selection[0], selection[0])

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

def resetList():
    global count
    global pick

    count = 0
    del pick[0:]
    
    label1.config(text=str('RESET'))

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

buttonRe = Button(frame1, width=20, height=1, text="Reset",font=('arial', 7), overrelief="solid", command=resetList)
buttonRe.pack()

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
label3 = Label(frame3, text="test_page")
label3.pack()

# Main
root.mainloop()
