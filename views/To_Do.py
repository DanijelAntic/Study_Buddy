# ...existing code...
import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")

class ToDoView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.tasks = []
        self.task_vars = []
        self._build_ui()
        self._load_tasks()

    def _build_ui(self):
        top = tk.Frame(self)
        top.pack(fill="x", padx=8, pady=8)

        self.entry = tk.Entry(top)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(top, text="Hinzufügen", command=self.add_task)
        add_btn.pack(side="left")

        clear_btn = tk.Button(top, text="Gelöschte entfernen", command=self.remove_completed)
        clear_btn.pack(side="left", padx=(6,0))

        # scrollable area for tasks
        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=8, pady=(0,8))

        canvas = tk.Canvas(container, borderwidth=0, highlightthickness=0)
        self.tasks_frame = tk.Frame(canvas)
        vsb = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0,0), window=self.tasks_frame, anchor="nw")

        self.tasks_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.tasks.append({"text": text, "done": False})
        self.entry.delete(0, "end")
        self._refresh_tasks()
        self._save_tasks()

    def _create_task_row(self, idx, task):
        var = tk.BooleanVar(value=task.get("done", False))
        cb = tk.Checkbutton(self.tasks_frame, text=task["text"], variable=var,
                            command=lambda i=idx, v=var: self._toggle_task(i, v))
        cb.grid(row=idx, column=0, sticky="w", padx=(2,2), pady=2)

        del_btn = tk.Button(self.tasks_frame, text="Löschen",
                            command=lambda i=idx: self._delete_task(i), width=8)
        del_btn.grid(row=idx, column=1, padx=(6,2), pady=2)
        self.task_vars.append(var)

        # strike-through visual for done
        if var.get():
            cb.config(fg="gray")
        else:
            cb.config(fg="black")

    def _refresh_tasks(self):
        # clear existing widgets
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        self.task_vars = []
        for i, task in enumerate(self.tasks):
            self._create_task_row(i, task)

    def _toggle_task(self, idx, var):
        self.tasks[idx]["done"] = bool(var.get())
        self._refresh_tasks()
        self._save_tasks()

    def _delete_task(self, idx):
        if idx < 0 or idx >= len(self.tasks):
            return
        del self.tasks[idx]
        self._refresh_tasks()
        self._save_tasks()

    def remove_completed(self):
        self.tasks = [t for t in self.tasks if not t.get("done", False)]
        self._refresh_tasks()
        self._save_tasks()

    def _load_tasks(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
        except Exception as e:
            messagebox.showwarning("Laden fehlgeschlagen", f"Kann todos.json nicht laden:\n{e}")
            self.tasks = []
        self._refresh_tasks()

    def _save_tasks(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Speichern fehlgeschlagen", f"Kann todos.json nicht speichern:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do Liste")
    root.geometry("480x400")
    app = ToDoView(master=root)
    root.mainloop()
# ...existing code..