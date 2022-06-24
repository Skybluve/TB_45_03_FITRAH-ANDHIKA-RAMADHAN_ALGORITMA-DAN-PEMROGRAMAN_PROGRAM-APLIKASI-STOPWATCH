# mengimpor modul tkinter
from tkinter import * 
# mengimpor modul time
import time 

# menggunakan class StopWatch dan menginheritence dari class Frame
class StopWatch(Frame):
    
   # metode ‘print_Teks’
    def print_Teks(self):
        #membuat label dengan settingan dan ukuran yang sudah saya tentukan. Ini untuk menampilkan angka angka stopwatch
        self.teks = Label(self, textvariable=self.waktu_String,font="Times 19 bold", bg='light green', fg='blue')
        
        # menjalankan metode ‘aturWaktu’ dengan memasukkan nilai variabel ‘waktu_terkini’ sebagai parameter
        self.aturWaktu(self.waktu_terkini)
        #memasukkan teks angka stopwatch kedalam window
        self.teks.grid(row=0, column=0)
        
    # metode ‘update’ untuk memperbarui waktu stopwatch
    def update(self):
        #  mendapatkan waktu terkini
        self.waktu_terkini = time.time() - self._start 
        # menjalankan metode ‘aturWaktu’ dengan memasukkan nilai variabel ‘waktuSekarang’ sebagai parameter
        self.aturWaktu(self.waktu_terkini)
        # memanggil metode ‘after’ dengan memasukkan nilai variabel ‘delay’ sebagai parameter
        self._timer = self.after(50, self.update)

    # menggunakan metode ‘aturWaktu’ untuk mengatur waktu stopwatch
    def aturWaktu(self, waktu):
        # medapatkan waktu dalam menit, detik, dan milidetik
        menit = int(waktu / 60)
        detik = int(waktu - menit * 60.0)
        jam = int((waktu - menit * 60.0 - detik) * 100)
        # menggabungkan angka menit, detik, dan milidetik dan dimasukkan ke variabel ‘waktu_String’
        self.waktu_String.set('%02d:%02d:%02d' % (menit, detik, jam))

    # menggunakan metode start untuk menjalankan stopwatch
    def Start(self):
        # memastikan stopwatch tidak berjalan dan teks tombolnya adalah ‘Start’ atau ‘Resume’
        if not self.waktu_Berjalan and self.textStart.get() == 'Start' :
            # mengubah teks tombolnya menjadi ‘Pause’
            self.textStart.set('Print')
            # mendapatkan nilai waktu sekarang
            self._start = time.time() - self.waktu_terkini
            # menjalankan metode ‘update’
            self.update()
            # mengubah nilai variabel ‘waktu_Berjalan’ menjadi True yang menandakan stopwatch berjalan
            self.waktu_Berjalan = True
        # memastikan stopwatch berjalan dan teks tombolnya adalah ‘Pause’
        elif self.waktu_Berjalan and self.textStart.get() == 'Print' :
            # memasukkan nilai stopwatch ke layar
            self.setKolom(str(self.posisi)+ ". " + self.waktu_String.get()+"\n")
            # menambahkan nilai posisi sesuai urutan yang dicetak ke layar
            self.posisi+=1
    # menggunakan metode ‘pause’ untuk menghentikan stopwatch
    def pause(self):
        # memastikan stopwatch berjalan bernilai True
        if self.waktu_Berjalan:
            self.textStart.set('Start')
            # menjalankan metode ‘after_cancel’ untuk pause timer stopwatch
            self.after_cancel(self._timer)
            # mendapatkan nilai waktu sekarang
            self.waktu_terkini = time.time() - self._start
            # menjalankan metode ‘aturWaktu’ dengan memasukkan nilai variabel ‘waktuSekarang’ sebagai parameter
            self.aturWaktu(self.waktu_terkini)
            # mengubah nilai variabel ‘waktu_Berjalan’ menjadi False yang menandakan stopwatch tidak berjalan
            self.waktu_Berjalan = False
    # menggunakan metode ‘reset’ untuk mereset stopwatch
    def Reset(self):
        # mendapatkan waktu stopwatch
        self._start = time.time()
        # mereset nilai variabel ‘waktu_terkini’
        self.waktu_terkini = 0.0
        # menjalankan metode ‘aturWaktu’ dengan memasukkan nilai variabel ‘waktuSekarang’ sebagai parameter
        self.aturWaktu(self.waktu_terkini)
        # membuat layar agar bisa di modifikasi
        self.kolom.config(state=NORMAL)
        # menghapus isi dari layar
        self.kolom.delete('1.0',END)
        # membuat layar agar tidak bisa di modifikasi
        self.kolom.configure(state=DISABLED)
        
    # menggunakan metode ‘setKolom’ untuk menampilkan isi dari variabel ‘kolom’ ke layar
    def print_Kolom(self):
        # membuat kolom teks untuk layar  dengan settingan yang sudah saya tentukan
        self.kolom = Text(height=12, width=30, bg='yellow', fg='black')
        # menjalankan metode scrollbar untuk menampilkan scrollbar pada layar
        self.scrollBar()
        # memasukkan layar ke dalam window
        self.kolom.grid(row=1,column=0,columnspan=4,pady=4)
        # membuat layar agar tidak bisa di modifikasi
        self.kolom.configure(state=DISABLED)
        
    # menggunakan metode setKolom untuk menampilkan nilai ke layar
    def setKolom(self, nilai):
        # membuat layar agar bisa di modifikasi
        self.kolom.config(state = NORMAL)
        # memasukkan nilai ke dalam layar
        self.kolom.insert(END,nilai)
        # membuat layar agar tidak bisa di modifikasi
        self.kolom.configure(state = DISABLED)

    # menggunakan metode scrollbar untuk menampilkan scrollbar pada layar
    def scrollBar(self):
        # membuat scrollbar
        scroll = Scrollbar()
        # memasukkan scrollbar ke dalam window
        scroll.grid(row=1, column=5, rowspan=1, sticky=N+S+W)
        # menghubungkan scrollbar dengan kolom teks ke dalam window
        scroll.config(command=self.kolom.yview)
        # mengaktifkan perintah scrollbar ke layar
        self.kolom.config(yscrollcommand=scroll.set)
        
    # menggunakan metode tombol untuk menampilkan tombol pada layar
    def print_Tombol(self):
        # Membuat tombol start,pause,reset, dan quit
        Button(textvariable=self.textStart,bg = 'light green',command=self.Start).grid(row=2, column=0)
        Button(text='Pause',bg ='orange',command = self.pause).grid(row=2, column=1)
        Button(text='Reset',bg = 'yellow',command = self.Reset).grid(row=2, column=2)
        Button(text='Quit',bg = 'red', command =self.quit).grid(row=2, column=3)
    
    # membuat konstruktor untuk class Stopwatch 
    def __init__(self, parent):
        # menjalankan konstruktor dari class Frame
        Frame.__init__(self, parent)
        # membuat variabel untuk menampung waktu
        self._start = 0.0
        # membuat variabel untuk menampung waktu sekarang
        self.waktu_terkini = 0.0
        # menginisialisasi variabel waktu_Berjalan dengan False
        self.waktu_Berjalan = False
        # menginisialisasi class stopwatch untuk memperbarui waktu
        self.waktu_String = StringVar()
        # menginisialisasi variabel dan class StringVar untuk teks tombol start,pause,reset, dan quit
        self.textStart= StringVar()
        # mengubah isi dari variabel textStart menjadi Start
        self.textStart.set('Start')
        # mengubah warna menjadi  biru
        parent.configure(background='blue')
        # mengubah judul window  menjadi Program Aplikasi  Stopwatch
        parent.title('Program Aplikasi Stopwatch')
        # menjalankan metode print_teks untuk menampilkan isi dari variabel kolom ke layar
        self.print_Teks()
        # menjalankan metode print_Kolom untuk menampilkan isi dari variabel kolom ke layar
        self.print_Kolom()
        # menjalankan metode print_Tombol untuk menampilkan isi dari variabel tombol ke layar
        self.print_Tombol()
        # menginisialisasi posisi  urutan  percetkan waktu
        self.posisi=1
            
# membuat fungsi untuk menjalankan program dengan metode main
def main():
    # menjalankan window tkinter 
    root = Tk()
    # membuat object dari class Stopwatch
    sw = StopWatch(root)
    # memasukkan frame class Stopwatch ke dalam window
    sw.grid(row=0,column=0, columnspan=4)
    # membuat fungsi agar program tidak langsung di tutup
    root.mainloop()
# menjalankan program dengan metode main
if __name__ == '__main__':
    main()