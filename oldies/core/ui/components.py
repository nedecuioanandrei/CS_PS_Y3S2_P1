import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import *


class TableView(tk.Frame):
    def __init__(self, controller, header=None):
        super().__init__()
        self.header = header if header else ()

        # define ui components
        self.controller = controller
        self.scroll = tk.Scrollbar(controller)
        self.scroll.grid(row=0, column=0)
        self.table = ttk.Treeview(self.scroll, yscrollcommand=self.scroll.set, xscrollcommand=self.scroll.set)
        self.table.grid(row=1, column=0)
        self.scroll.config(command=self.table.yview)
        self.scroll.config(command=self.table.xview)

        # define table columns
        self.table["columns"] = header

        # format columns and create headings
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.heading("#0", text="", anchor=tk.CENTER)
        for col_header in header:
            self.table.column(col_header, anchor=tk.CENTER)
            self.table.heading(col_header, text=col_header, anchor=tk.CENTER)

        # create entry zone
        # define get_methods
        self.entry_frame = tk.Frame(controller)
        self.entry_frame.grid(row=2, column=0)
        for idx, entry in enumerate(header):
            self.__setattr__(f"{entry}_label", tk.Label(self.entry_frame, text=entry))
            self.__getattribute__(f"{entry}_label").grid(row=3, column=idx + 1)
            self.__setattr__(f"{entry}_entry", tk.Entry(self.entry_frame))
            self.__getattribute__(f"{entry}_entry").grid(row=1, column=idx + 1)
            self.__setattr__(f"get_{entry}", lambda *_: self.__getattribute__(f"{entry}_entry").get())

    def add_button(self, row, column, text, command):
        pass

    def update_record(self, index=None, new_record=None):
        """Update with data"""
        raise NotImplementedError()

    def refresh_content(self):
        raise NotImplementedError()

    def select_record(self):
        """Load current selected record."""
        raise NotImplementedError()
        ectmode = "day",
        #                      year=2021,
        #                      month=2,
        #                      day

    def deselect_record(self):
        """Discard current selection."""
        raise NotImplementedError()

    def get_selected_record(self):
        """Get the content of the selected record."""
        raise NotImplementedError()


class ReportFrame(tk.Frame):
    def _get_entry(self, tp):
        if tp == "cal":
            ans = Calendar(self.controller, selectmode="day", year=2021, month=2, day=3)
            ans.get = ans.get_date
            return ans
        if tp == "txt":
            return tk.Entry(self.controller)
        if tp == "frmt":
            return tk.Entry(self.controller)
        raise NotImplemented()

    def __init__(self, controller, entries=None, formats=None):
        super().__init__()
        self.entries = entries
        self.controller = controller
        self.formats = formats

        for idx, (entry, tp) in enumerate(entries):
            # create label
            self.__setattr__(f"{entry}_label", tk.Label(self.controller, text=f"{entry}"))
            self.__getattribute__(f"{entry}_label").grid(row=0, column=idx + 1)
            # create entry
            self.__setattr__(f"{entry}_entry", self._get_entry(tp))
            self.__getattribute__(f"{entry}_entry").grid(row=1, column=idx + 1)
            self.__setattr__(f"get_{entry}", lambda *_: self.__getattribute__(f"{entry}_entry").get())

    def generate_report(self, data, frmt, dst):
        raise NotImplementedError()
