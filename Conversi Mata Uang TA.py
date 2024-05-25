# Modul 1 (Tipe Data) dan Modul 8 (GUI)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Modul 5 (OOP 1, Class) dan Modul 4 (Method)
class MataUang:
    def __init__(self, nilai, negara):
        self.nilai = nilai
        self.negara = negara

# Modul 6 (OOP 2, Encapsulation), Modul 4 (Method) Modul 1 (Tipe Data Dan Variabel)
class Konverter:
    nilai_tukar = {
        'Indonesia': {'Amerika Serikat': 0.000063, 'Arab Saudi': 0.000235, 'Jepang': 0.009816, 'Korea Selatan': 0.08541, 'Euro': 0.000058, 'Ponsterling': 0.000049},
        'Amerika Serikat': {'Indonesia': 15000, 'Arab Saudi': 3.75, 'Jepang': 114, 'Korea Selatan': 1200, 'Euro': 0.91, 'Ponsterling': 0.78},
        'Arab Saudi': {'Indonesia': 3850, 'Amerika Serikat': 0.27, 'Jepang': 30.4, 'Korea Selatan': 320, 'Euro': 0.24, 'Ponsterling': 0.21},
        'Jepang': {'Indonesia': 127, 'Amerika Serikat': 0.0088, 'Arab Saudi': 0.033, 'Korea Selatan': 10.5, 'Euro': 0.0079, 'Ponsterling': 0.0068},
        'Korea Selatan': {'Indonesia': 12.1, 'Amerika Serikat': 0.00083, 'Arab Saudi': 0.0031, 'Jepang': 0.095, 'Euro': 0.00075, 'Ponsterling': 0.00065},
        'Euro': {'Indonesia': 16000, 'Amerika Serikat': 1.1, 'Arab Saudi': 4.1, 'Jepang': 126, 'Korea Selatan': 1330, 'Ponsterling': 0.86},
        'Ponsterling': {'Indonesia': 18600, 'Amerika Serikat': 1.28, 'Arab Saudi': 4.77, 'Jepang': 147, 'Korea Selatan': 1550, 'Euro': 1.16}
    }
    
    def konversi(self, dari, ke, jumlah):
        return jumlah * self.nilai_tukar[dari][ke]
    
# Modul 8 (GUI) dan Modul 4 (Method)
class App:
    def __init__(self, root):
        self.konverter = Konverter()
        self.root = root
        self.root.title("Konverter Mata Uang")
        self.root.geometry("300x200")

        self.frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.dari_var = tk.StringVar()
        self.ke_var = tk.StringVar()
        self.jumlah_var = tk.DoubleVar()
        self.hasil_var = tk.StringVar()

        ttk.Label(self.frame, text="Dari:").grid(column=1, row=1, sticky=tk.W)
        self.dari_combobox = ttk.Combobox(self.frame, textvariable=self.dari_var, values=list(self.konverter.nilai_tukar.keys()))
        self.dari_combobox.grid(column=2, row=1)
        ttk.Label(self.frame, text="Ke:").grid(column=1, row=2, sticky=tk.W)
        self.ke_combobox = ttk.Combobox(self.frame, textvariable=self.ke_var, values=list(self.konverter.nilai_tukar.keys()))
        self.ke_combobox.grid(column=2, row=2)
        ttk.Label(self.frame, text="Jumlah:").grid(column=1, row=3, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.jumlah_var).grid(column=2, row=3)
        ttk.Button(self.frame, text="Konversi", command=self.konversi).grid(column=2, row=4)
        ttk.Label(self.frame, text="Hasil:").grid(column=1, row=5, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.hasil_var, state='readonly').grid(column=2, row=5)
        
    # Modul 4 (Method) dan Modul 1 (Tipe Data Dan Variabel)
    def konversi(self):
        while True :
            dari = self.dari_var.get()
            ke = self.ke_var.get()
            jumlah = self.jumlah_var.get()
            hasil = self.konverter.konversi(dari, ke, jumlah)
            simbol = {
                'Indonesia': 'Rp',
                'Amerika Serikat': '$',
                'Arab Saudi': 'SR',
                'Jepang': '¥',
                'Korea Selatan': '₩',
                'Euro': '€',
                'Ponsterling': '£'
            }
            self.hasil_var.set(f"{simbol[ke]} {hasil:.2f}")

            # Modul 2 (Pengkondisian)
            lagi = messagebox.askyesno("Konversi Lagi", "Apakah ingin mengkonversi mata uang lagi?")
            if lagi:
                self.reset_fields()
            else:
                self.root.quit()
            break
    
    def reset_fields(self):
            self.dari_var.set('')
            self.ke_var.set('')
            self.jumlah_var.set(0)
            self.hasil_var.set('')

# Modul 2 (Pengkondisian)
if __name__ == "__main__":

    # Modul 8 (GUI)
    root = tk.Tk()
    app = App(root)
    root.mainloop()
