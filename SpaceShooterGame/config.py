from configparser import ConfigParser
from tkinter import *
from tkinter import ttk, messagebox

config = ConfigParser()

#config.read(file1)

def savecmd():
    try:
        file1 = "D:\python\pygamesprograms\SpaceShooterGame\config.ini"
        data = entry.get()
        config.read(file1)
        config.set("player1", "score", data)
        configure = open(file1, "w")
        config.write(configure)
        print(config.sections())
        configure.close()

    except Exception as e:
        print(e)


def loadcmd():
    try:
        file1 = "D:\python\pygamesprograms\SpaceShooterGame\config.ini"
        f = open(file1)
    except Exception as e:
        txb.delete(0.0, END)
        txb.insert(0.0, e)
    else:
        txb.delete(0.0, END)
        config.read(file1)
        data = config.sections()
        for i in data:
            if i == "player1":
                txb.insert(END, f"{i}\n")
                for j in config[i]:
                    txb.insert(END, f"{j}: {config[i][j]}\n")
    root.after(1000, loadcmd)
        

root = Tk()
root.geometry("400x400")
root.title("Configset")

frame1 = Frame(root)
frame1.pack(pady=20)

frame2 = Frame(root)
frame2.pack(pady=20)

entry = Entry(frame1)
entry.grid(pady=20)

btn = Button(frame1, text=" save ", command=savecmd, font=("d", 12))
btn.grid(row=1, pady=10, sticky=W)

extbtn = Button(frame1, text=" load ", command=loadcmd, font=("d", 12))
extbtn.grid(row=1, pady=10, sticky=E)

txb = Text(frame2, height=12, width=35)
txb.grid()

ycb = ttk.Scrollbar(frame2, orient="vertical", command=txb.yview)
ycb.grid(row=0, column=1, ipady=77)

txb.configure(yscrollcommand=ycb.set)

root.mainloop()
