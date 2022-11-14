import tkinter as tk                                    # Mengimport tkinter untuk menampilkan GUI nya 
from tkinter import ttk
from turtle import bgcolor                                 # Dari library tkinter kita import tkinternya agar bisa dipanggil dan dimunculkan
from tkcalendar import Calendar                         # Dari library tkinter kita import juga tkcalendar dan memunculkan calendar 
from tkinter.scrolledtext import ScrolledText           # Dari library tkinter kita import scrolled text agar text ini bisa ada fitur scroll nya  
from time import strftime                               # Fungsinya untuk mengkonversi string ke time 
from tkinter import * 
from PIL import ImageTk, Image
todos = {}                                              # Untuk membuat dictionary todos

def detailTodo(cb = None):                              # Pengembalian fungsi jika tidak ada value 
    win = tk.Toplevel()
    win.wm_title("Detail Kegiatan")
    win.configure(bg='#4B086D')                         # Mengubah warna background menjadi ungu 
    selectedItem = treev.focus()
    selectedIndex = treev.item(selectedItem)['text']
    selectedTodo = todos[tanggal][selectedIndex]
    judul = tk.StringVar(value = selectedTodo['Judul']) 
    tk.Label(win, text = "Tanggal\t\t:",bg='#4B086D',fg= 'gold').grid(row = 0, column = 0, sticky="NW")
    tk.Label(win, text = "{} | {}".format(tanggal, selectedTodo["Waktu"]),width=25,borderwidth=2).grid(row = 0, column = 1, sticky = "W",padx=29)#Diubah menjadi 25 panjangnya agar terlihat lebih presisi. dan sticky diubah menjadi W
    tk.Label(win, text = "Judul\t\t:",bg='#4B086D',fg= 'gold').grid(row=1,column=0,sticky='NW') #mengubah beberapa warna dari judul, tanggal, dan keterangan. 
    tk.Entry(win, state = "disabled", textvariable = judul, borderwidth=2, width=29).grid(row=1, column=1, sticky="W",padx=29) # diubah panjang dari kolomnya menjadi 29 agar menyesuaikan dengan keterangan.
    tk.Label(win, text= "Keterangan\t:",bg='#4B086D',fg= 'gold').grid(row=2, column=0, sticky="NW")
    keterangan = ScrolledText(win, width = 20, height = 5) #Diubah menjadi 20 panjangnya agar terlihat lebih presisi.
    keterangan.grid(row = 2, column=1, sticky = "SW", padx=29)
    keterangan.insert(tk.INSERT, selectedTodo["Keterangan"])
    keterangan.configure(state = "disabled") 
    img = PhotoImage(file = r"C:\Users\USER\Downloads\sukuna-jujutsu-kaisen-hd-wallpaper-1920x1080-uhdpaper.com-325.1_a.png") 
    img1 = img.subsample(10, 10)
    tk.Label(win, image = img1).grid(row = 0, column = 3,columnspan = 3, rowspan = 3, padx = 5, pady = 5) #MENAMBAHKAN IMAGE KE DETAIL TODo
    Label.pack()
def LoadTodos():
    global todos 
    f = open('mytodo.dat','r')
    data = f.read()
    f.close()
    todos = eval(data)
    ListTodo()
def SaveTodos(): 
    f = open('mytodo.dat','w')
    f.write(str(todos))
    f.close()
def delTodo(): 
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus()
    todos[tanggal].pop(treev.item(selectedItem)['text'])
    ListTodo()
def ListTodo(cb = None): 
    for i in treev.get_children(): 
        treev.delete(i)
    tanggal = str(cal.selection_get())
    if tanggal in todos : 
        for i in range (len(todos[tanggal])): 
            treev.insert("","end",text = i, values = (todos[tanggal][i]['Waktu'], todos[tanggal][i]['Judul']))
def addTodo(win,key,jam,menit,judul,keterangan): 
    newTodo = {
        "Waktu":"{}:{}".format(jam.get(), menit.get()), 
        "Judul":judul.get(), 
        "Keterangan": keterangan.get("1.0", tk.END)
    }
    if key in todos: 
        todos[key].append(newTodo)
    else : 
        todos[key] = [newTodo]
    win.destroy()
    ListTodo()
def AddForm(): 
    win = tk.Toplevel()
    win.wm_title("+")
    win.configure(bg='#4B086D') #nyamain warna
    jam = tk.IntVar(value = 10)
    menit = tk.IntVar(value = 30)
    judul = tk.StringVar(value="")
    tk.Label(win, text="Waktu\t\t: ",bg='#4B086D',fg= 'gold').grid(row=0, column = 0) #Ngubah warna di waktu 
    tk.Spinbox(win, from_= 0, to = 23, textvariable = jam, width = 3).grid(row = 0, column = 1, sticky = "W",padx=35) #nambahin sticky
    tk.Spinbox(win, from_= 0, to = 59, textvariable = menit, width = 3).grid(row = 0, column = 2, sticky = "W",padx=15) #nambahin sticky
    tk.Label(win, text = "Judul\t\t:",bg='#4B086D',fg= 'gold').grid(row = 1, column = 0)#ngubah warna di judul 
    tk.Entry(win, textvariable = judul).grid(row = 1, column = 1, columnspan = 1)
    tk.Label(win, text = "Keterangan\t:",bg='#4B086D',fg= 'gold').grid(row = 2, column = 0) #ngasih "" di keterangan dan ngubah warnanya 
    keterangan = ScrolledText(win, width = 20, height = 5)
    keterangan.grid(row = 2, column = 1, columnspan = 2, rowspan = 4, sticky = "SW")
    tanggal = str(cal.selection_get())
    tk.Button(win, text = "Tambah", command = lambda: addTodo(win, tanggal, jam, menit, judul, keterangan),bg='skyblue1', fg='black').grid(row = 6, columnspan = 3)
    #ngubah warna di bagian button tambah menjadi skyblue
def title():
    waktu = strftime("%H:%M")
    tanggal = str(cal.selection_get())
    root.title(tanggal + " | " + waktu + " | LIST TO DO" )  ## Menambah Judul
    root.after(1000, title)    
root = tk.Tk()
root.configure(bg='#02c1cf')
root.iconbitmap(r"C:\Users\USER\OprecMBCBD4\Tugas3_MBC\icon.ico")  ## Mengubah logo menjadi sesuai dengan apliakasi yaitu to do list
img = PhotoImage(file = r"C:\Users\USER\Downloads\albert-einstein-quotes-jpg.png") #Menambah gambar agar terlihar lebih fresh lebih lagi gambar untuk kita bisa motivasi
img1 = img.subsample(5, 7)
tk.Label(root, image = img1).grid(row = 0, column = 4,columnspan = 3, rowspan = 3, padx = 5, pady = 10) #Label dari image Albert Einstein 
cal = Calendar(root, font = "Times", weight = "Bold", selectmode = 'day', locale = 'id_ID', cursor = 'hand1')
cal.grid(row = 1, column = 0, sticky = 'N', rowspan = 7)
cal.bind("<<CalendarSelected>>", ListTodo)
tanggal = str(cal.selection_get())
treev = ttk.Treeview(root)
treev.grid(row = 0, column = 1, sticky = 'WNE', rowspan = 4, columnspan = 2)
scrollBar = tk.Scrollbar(root, orient = "vertical", command = treev.yview)
scrollBar.grid(row = 0, column = 3, sticky = 'ENS', rowspan = 4)
treev.configure(yscrollcommand = scrollBar.set)
treev.bind("<Double-1>", detailTodo)
treev["columns"] = ('1', '2') 
treev["show"] = 'headings'
treev.column("1", width = 100)
treev.heading("1", text = "JAM")
treev.heading("2", text = "JUDUL")
btnAdd = tk.Button (root, text='Tambah', width=20, bg='skyblue1', fg='black', command=AddForm) ## mengbah warna tombol tambah
btnAdd.grid(row = 4, column = 1, sticky = 'N')
btnDel = tk.Button (root, text='Hapus', width=20, bg='skyblue1', fg='black', command=delTodo) ## mengbah warna tombol hapus
btnDel.grid(row = 4, column = 2, sticky = 'N')
btnLoad = tk.Button (root, text='Load', width=20, bg='skyblue1', fg='black', command=LoadTodos) ## mengbah warna tombol load
btnLoad.grid(row = 5, column = 1, sticky = 'S')
btnSave = tk.Button (root, text='Save', width=20, bg='skyblue1', fg='black', command=SaveTodos) ## ## mengbah warna tombol save
btnSave.grid(row = 5, column = 2, sticky = 'S')
title()
root.mainloop()