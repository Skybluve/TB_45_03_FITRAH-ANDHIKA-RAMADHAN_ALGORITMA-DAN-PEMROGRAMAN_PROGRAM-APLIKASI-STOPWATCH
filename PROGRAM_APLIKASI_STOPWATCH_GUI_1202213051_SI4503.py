from tkinter import *
import time

class StopWatch(Frame):
    
   
    def print_Teks(self):
        self.teks = Label(self, textvariable=self.waktu_String,font="Times 19 bold", bg='light green', fg='blue')
        self.aturWaktu(self.waktu_terkini)
        self.teks.grid(row=0, column=0)

    def update(self):
        self.waktu_terkini = time.time() - self._start
        self.aturWaktu(self.waktu_terkini)
        self._timer = self.after(50, self.update)

    def aturWaktu(self, waktu):
        menit = int(waktu / 60)
        detik = int(waktu - menit * 60.0)
        jam = int((waktu - menit * 60.0 - detik) * 100)
        self.waktu_String.set('%02d:%02d:%02d' % (menit, detik, jam))

    def Start(self):
        if not self.waktu_Berjalan and self.textStart.get() == 'Start' :
            self.textStart.set('Print')
            self._start = time.time() - self.waktu_terkini
            self.update()
            self.waktu_Berjalan = True
        elif self.waktu_Berjalan and self.textStart.get() == 'Print' :
            self.setKolom(str(self.posisi)+ ". " + self.waktu_String.get()+"\n")
            self.posisi+=1

    def pause(self):
        if self.waktu_Berjalan:
            self.textStart.set('Start')
            self.after_cancel(self._timer)
            self.waktu_terkini = time.time() - self._start
            self.aturWaktu(self.waktu_terkini)
            self.waktu_Berjalan = False

    def Reset(self):
        self._start = time.time()
        self.waktu_terkini = 0.0
        self.aturWaktu(self.waktu_terkini)
        self.kolom.config(state=NORMAL)
        self.kolom.delete('1.0',END)
        self.kolom.configure(state=DISABLED)

    def print_Kolom(self):
        self.kolom = Text(height=12, width=30, bg='yellow', fg='black')
        self.scrollBar()
        self.kolom.grid(row=1,column=0,columnspan=4,pady=4)
        self.kolom.configure(state=DISABLED)

    def setKolom(self, nilai):
        self.kolom.config(state = NORMAL)
        self.kolom.insert(END,nilai)
        self.kolom.configure(state = DISABLED)

    def scrollBar(self):
        scroll = Scrollbar()
        scroll.grid(row=1, column=5, rowspan=1, sticky=N+S+W)
        scroll.config(command=self.kolom.yview)
        self.kolom.config(yscrollcommand=scroll.set)

    def print_Tombol(self):
        Button(textvariable=self.textStart,bg = 'light green',command=self.Start).grid(row=2, column=0)
        Button(text='Pause',bg ='orange',command = self.pause).grid(row=2, column=1)
        Button(text='Reset',bg = 'yellow',command = self.Reset).grid(row=2, column=2)
        Button(text='Quit',bg = 'red', command =self.quit).grid(row=2, column=3)
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._start = 0.0
        self.waktu_terkini = 0.0
        self.waktu_Berjalan = False
        self.waktu_String = StringVar()
        self.textStart= StringVar()
        self.textStart.set('Start')
        parent.configure(background='blue')
        parent.title('Program Aplikasi Stopwatch')
        self.print_Teks()
        self.print_Kolom()
        self.print_Tombol()
        self.posisi=1
            

def main():
    root = Tk()
    sw = StopWatch(root)
    sw.grid(row=0,column=0, columnspan=4)
    root.mainloop()

if __name__ == '__main__':
    main()