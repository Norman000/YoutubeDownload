from tkinter import *
from song import song
from video import video

root = Tk()
root.title('Youtube Downloads')
c = Canvas(root, width=300, height=190)
image=None
bg_label = Label(root, image=image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

c.grid()

v = IntVar()
v.set('0')

opçoes = {
    0: ('Música', song),
    1: ('Video', video)
}

title = Label(bg_label, text='@dreamer57_ - Youtube Downloads')
title.config(font=("",12))
title.place(x=150, y=25,anchor='center')

label = Label(bg_label, text='Nome/Link')
e = Entry(bg_label)
label.grid(row=0, pady=(50,10))
e.grid(row=0, column=1, padx=(0,20), pady=(50,10))

for opt in sorted(opçoes.keys()):
    radio = Radiobutton(bg_label, text=opçoes[opt][0], padx=10, variable=v, value=opt)
    radio.grid(row=5, column=opt, padx=20, pady=5)

download = Button(bg_label, anchor='center', text='Download', command= lambda : opçoes[v.get()][1](e))
download.grid(columnspan=2, pady=7)

root.mainloop()
