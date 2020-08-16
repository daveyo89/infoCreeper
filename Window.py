import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import Scraper


class Window:

    def __init__(self):
        self.get_info = self.get_info()
        self.master = tk.Tk()
        self.container = ttk.Frame(self.master)
        self.canvas = tk.Canvas(self.container, width=400,height=400)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.scrollable_frame.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # self.txt_edit = tk.Text(self.master)

        self.app_ui_buttons()
        self.app_ui_table()

        self.canvas.pack(side="left", fill="both", expand=True)
        self.container.pack(side="left", fill="both", expand=True)

        self.scrollbar.pack(side="right", fill="y")
        self.master.title("InfoCreeper")
        self.master.iconbitmap("icon.ico")
        self.master.mainloop()

    def app_ui_buttons(self):
        fr_buttons = tk.Frame(self.scrollable_frame, relief=tk.RAISED, bd=3)
        btn_load = tk.Button(fr_buttons, text="Load", command=self.load_info)
        btn_open = tk.Button(fr_buttons, text="Open", command=self.open_file)
        btn_save = tk.Button(fr_buttons, text="Save As...", command=self.save_file)

        btn_load.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=2, column=0, sticky="ew", padx=5)
        fr_buttons.grid(row=0, column=0, sticky="ns")

    def app_ui_table(self):
        fr_prices = tk.Frame(self.scrollable_frame, relief=tk.RAISED, bd=3)

        number = 0
        for i, j in self.get_info.items():
            s = StringVar()
            Label(fr_prices, text=f"{i}: ").grid(row=number, column=1, sticky="w")
            Entry(fr_prices, width=30, state='readonly', textvariable=s).grid(row=number, column=2)
            s.set(j)
            number += 1
        fr_prices.grid(row=0, column=1, sticky="ns")

    @classmethod
    def get_info(cls):
        return Scraper.Scraper().get_info()

    def load_info(self):
        # self.txt_edit.insert(tk.END, self.get_info)
        pass

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        # self.txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            # self.txt_edit.insert(tk.END, text)
        self.master.title(f"Simple Text Editor - {filepath}")

    def save_file(self):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        # with open(filepath, "w") as output_file:
        #     text = self.txt_edit.get(1.0, tk.END)
        #     output_file.write(text)
        self.master.title(f"Simple Text Editor - {filepath}")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()
