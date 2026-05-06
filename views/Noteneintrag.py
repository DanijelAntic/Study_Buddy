import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os

# Einfaches Noten-Eingabeformular: pro Fach eine Zeile, 4 Noten-Spalten, Durchschnitt pro Fach
# Buttons: Berechnen (aktualisiert Durchschnitte), Clear (löscht alle Eingaben), Speichern (CSV)

NUM_ROWS = 8
NUM_GRADES = 4

class NotenTabelle(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(padx=10, pady=10)
        self._build_ui()

    def _build_ui(self):
        headers = ["Fach"] + [f"Note {i+1}" for i in range(NUM_GRADES)] + ["Durchschnitt"]
        for c, h in enumerate(headers):
            tk.Label(self, text=h, font=("Arial", 10, "bold")).grid(row=0, column=c, padx=5, pady=5)

        self.fach_vars = []
        self.grade_vars = []
        self.avg_labels = []

        for r in range(1, NUM_ROWS + 1):
            fach = tk.Entry(self, width=20)
            fach.grid(row=r, column=0, padx=3, pady=3)
            self.fach_vars.append(fach)

            grades_row = []
            for c in range(NUM_GRADES):
                e = tk.Entry(self, width=8)
                e.grid(row=r, column=1 + c, padx=3, pady=3)
                grades_row.append(e)
            self.grade_vars.append(grades_row)

            avg = tk.Label(self, text="", width=10, anchor="e")
            avg.grid(row=r, column=1 + NUM_GRADES, padx=3, pady=3)
            self.avg_labels.append(avg)

        # Gesamt-Durchschnitt unten
        tk.Label(self, text="Gesamt-Durchschnitt:", font=("Arial", 10, "bold")).grid(row=NUM_ROWS + 1, column=0, columnspan=2, sticky="w", pady=(10,0))
        self.overall_avg_label = tk.Label(self, text="", font=("Arial", 10, "bold"))
        self.overall_avg_label.grid(row=NUM_ROWS + 1, column=2, columnspan=2, sticky="w", pady=(10,0))

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.grid(row=NUM_ROWS + 2, column=0, columnspan=NUM_GRADES + 2, pady=(10,0))

        btn_calc = tk.Button(btn_frame, text="Berechnen / Aktualisieren", command=self.berechnen)
        btn_calc.pack(side="left", padx=5)

        btn_clear = tk.Button(btn_frame, text="Clear", command=self.clear_all)
        btn_clear.pack(side="left", padx=5)

        btn_save = tk.Button(btn_frame, text="Speichern", command=self.save_csv)
        btn_save.pack(side="left", padx=5)

    def berechnen(self):
        overall_sum = 0.0
        overall_count = 0
        for i in range(NUM_ROWS):
            grades = []
            for e in self.grade_vars[i]:
                val = e.get().strip().replace(",", ".")
                if val == "":
                    continue
                try:
                    g = float(val)
                    grades.append(g)
                except ValueError:
                    # ungültiger Wert -> Markieren und ignorieren
                    e.delete(0, tk.END)
                    e.insert(0, "")
            if grades:
                avg = sum(grades) / len(grades)
                self.avg_labels[i].config(text=f"{avg:.2f}")
                overall_sum += sum(grades)
                overall_count += len(grades)
            else:
                self.avg_labels[i].config(text="")
        if overall_count:
            overall = overall_sum / overall_count
            self.overall_avg_label.config(text=f"{overall:.2f}")
        else:
            self.overall_avg_label.config(text="")

    def clear_all(self):
        if not messagebox.askyesno("Löschen bestätigen", "Alle Einträge wirklich löschen?"):
            return
        for e in self.fach_vars:
            e.delete(0, tk.END)
        for row in self.grade_vars:
            for e in row:
                e.delete(0, tk.END)
        for lbl in self.avg_labels:
            lbl.config(text="")
        self.overall_avg_label.config(text="")

    def save_csv(self):
        self.berechnen()  # sicherstellen, dass Durchschnitte aktuell sind
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                                                 initialfile="noten.csv")
        if not file_path:
            return
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                header = ["Fach"] + [f"Note{i+1}" for i in range(NUM_GRADES)] + ["Durchschnitt"]
                writer.writerow(header)
                for i in range(NUM_ROWS):
                    fach = self.fach_vars[i].get().strip()
                    grades = [e.get().strip() for e in self.grade_vars[i]]
                    avg = self.avg_labels[i].cget("text")
                    if fach == "" and all(g == "" for g in grades) and avg == "":
                        continue
                    writer.writerow([fach] + grades + [avg])
            messagebox.showinfo("Gespeichert", f"Datei gespeichert: {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Speichern fehlgeschlagen:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Noteneintrag")
    app = NotenTabelle(master=root)
    root.mainloop()