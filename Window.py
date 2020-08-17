import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Combobox

import yaml

import Scraper


class Window:

    def __init__(self):
        self.scraper = Scraper.Scraper()
        self.get_specs = self.get_specs(self.get_config(0))
        self.get_info = self.scraper.get_info(self.get_specs)
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


        choices = [x for x in (enumerate(self.read_yml()))]
        variable = StringVar(self.master)

        w = OptionMenu(self.master, variable, *choices)
        w.pack()

        self.app_ui_buttons()
        self.app_ui_table(self.get_info)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.container.pack(side="left", fill="both", expand=True)

        self.scrollbar.pack(side="right", fill="y")
        self.master.title("InfoCreeper")
        self.master.iconbitmap("icon.ico")
        self.master.mainloop()

    def app_ui_buttons(self):
        fr_buttons = tk.Frame(self.scrollable_frame, relief=tk.RAISED, bd=3)
        btn_load = tk.Button(fr_buttons, text="Load", command=self.load_info)
        # btn_open = tk.Button(fr_buttons, text="Open", command=self.open_file)
        # btn_save = tk.Button(fr_buttons, text="Save As...", command=self.save_file)

        btn_load.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        # btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        # btn_save.grid(row=2, column=0, sticky="ew", padx=5)
        fr_buttons.grid(row=0, column=0, sticky="ns")

    def app_ui_table(self, data):
        setattr(self, 'fr_prices', tk.Frame(self.scrollable_frame, relief=tk.RAISED, bd=3))
        number = 0
        for i, j in data.items():
            s = StringVar()
            Label(self.fr_prices, text=f"{i}: ").grid(row=number, column=1, sticky="w")
            Entry(self.fr_prices, width=30, state='readonly', textvariable=s).grid(row=number, column=2)
            s.set(j)
            number += 1
        self.fr_prices.grid(row=0, column=1, sticky="ns")

    def read_yml(self):
        with open('config.yml', 'r') as f:
            return yaml.safe_load(f)

    def get_config(self, num):
        specs = [x for x in (enumerate(self.read_yml()))]
        choices = [specs[x][1] for x in range(len(specs))]

        return choices[num]

    def get_specs(self, config):
        return config

    def load_info(self):
        self.fr_prices.destroy()
        self.load_other()
        pass

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    def load_other(self):
        three = Scraper.Scraper().get_info(self.get_config(1))
        return self.app_ui_table(three)
