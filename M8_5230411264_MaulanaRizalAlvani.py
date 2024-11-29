# Import pustaka
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RentalMotorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RENTAL MOTOR BERKELAZZ")
        self.root.geometry("1500x1000")
        self.root.resizable(False, False)

        # Warna tema
        self.bg_color = "#ffffff" 
        self.primary_color = "#4a4a4a" 
        self.accent_color = "#1a73e8" 
        self.secondary_color = "#f1f1f1" 

        # Atur latar belakang
        self.root.configure(bg=self.bg_color)

        # Harga motor per hari
        self.motor_prices = {
            "Motor Matic": 50000,
            "Motor Bebek": 40000,
            "Motor Sport": 100000
        }

        # Daftar Riwayat Pesanan
        self.history = []

        # Label Judul
        header_label = tk.Label(
            root, text="RENTAL MOTOR BERKELAZZ", font=("Helvetica", 25, "bold"),
            bg=self.bg_color, fg=self.primary_color, pady=10
        )
        header_label.pack()

        # Pilihan Motor
        motor_frame = tk.Frame(root, bg=self.bg_color)
        motor_frame.pack(pady=10)
        tk.Label(motor_frame, text="Pilih Jenis Motor:", font=("Helvetica", 14), bg=self.bg_color, fg=self.primary_color).pack(anchor="w")

        self.motor_var = tk.StringVar(value="Motor Matic")
        for motor in self.motor_prices.keys():
            tk.Radiobutton(
                motor_frame, text=motor, variable=self.motor_var, value=motor, font=("Helvetica", 12),
                bg=self.bg_color, fg=self.primary_color, anchor="w", selectcolor=self.secondary_color
            ).pack(anchor="w")

        # Input Lama Sewa
        days_frame = tk.Frame(root, bg=self.bg_color)
        days_frame.pack(pady=10)
        tk.Label(days_frame, text="Lama Sewa (Hari):", font=("Helvetica", 14), bg=self.bg_color, fg=self.primary_color).pack(anchor="w")

        self.days_entry = tk.Entry(days_frame, font=("Helvetica", 12), width=10)
        self.days_entry.pack(anchor="w", pady=5)

        # Tombol Hitung dan Reset
        self.button_frame = tk.Frame(root, bg=self.bg_color)
        self.button_frame.pack(pady=10)

        self.calculate_button = tk.Button(
            self.button_frame, text="Hitung Biaya", font=("Helvetica", 12, "bold"),
            bg=self.accent_color, fg="white", command=self.calculate_cost, relief="flat", padx=10, pady=5
        )
        self.calculate_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(
            self.button_frame, text="Reset", font=("Helvetica", 12, "bold"),
            bg=self.secondary_color, fg=self.primary_color, command=self.reset, relief="flat", padx=10, pady=5
        )
        self.reset_button.grid(row=0, column=1, padx=10)

        # Label Hasil
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), fg=self.accent_color, bg=self.bg_color)
        self.result_label.pack(pady=10)

        # Tabel Riwayat Pesanan
        tk.Label(root, text="Riwayat Pesanan:", font=("Helvetica", 14), bg=self.bg_color, fg=self.primary_color).pack(pady=5)

        self.history_frame = tk.Frame(root, bg=self.bg_color)
        self.history_frame.pack()

        self.tree = ttk.Treeview(self.history_frame, columns=("Motor", "Hari", "Total"), show="headings", height=7)
        self.tree.pack()

        # Konfigurasi kolom
        self.tree.heading("Motor", text="Jenis Motor")
        self.tree.heading("Hari", text="Lama Sewa (Hari)")
        self.tree.heading("Total", text="Total Biaya (Rp)")
        self.tree.column("Motor", anchor="center", width=150)
        self.tree.column("Hari", anchor="center", width=100)
        self.tree.column("Total", anchor="center", width=150)

        # Style Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview", background=self.secondary_color, foreground=self.primary_color, rowheight=25,
            fieldbackground=self.secondary_color, font=("Helvetica", 11)
        )
        style.map("Treeview", background=[("selected", self.accent_color)], foreground=[("selected", "white")])

    def calculate_cost(self):
        try:
            days = int(self.days_entry.get())
            if days <= 0:
                raise ValueError
            motor = self.motor_var.get()
            cost_per_day = self.motor_prices[motor]
            total_cost = cost_per_day * days
            self.result_label.config(text=f"Total Biaya: Rp {total_cost:,}")

            # Tambahkan ke riwayat
            self.history.append((motor, days, total_cost))
            self.tree.insert("", "end", values=(motor, days, f"Rp {total_cost:,}"))

        except ValueError:
            messagebox.showerror("Input Tidak Valid", "Masukkan jumlah hari yang valid (angka positif).")

    def reset(self):
        self.motor_var.set("Motor Matic")
        self.days_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalMotorApp(root)
    root.mainloop()






