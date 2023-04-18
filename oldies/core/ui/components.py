import tkinter as tk
from tkinter import ttk
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
            self.__setattr__(f"get_{entry}", self.__getattribute__(f"{entry}_entry").get)
        self.add_button("select", 4, 2, "select", self.select_record)
        self.add_button("deselect", 4, 3, "deselect", self.deselect_record)

    def add_button(self, tag, row, column, text, command):
        """Add a new button."""
        self.__setattr__(f"{tag}_button", tk.Button(self.entry_frame, command=command, text=text))
        self.__getattribute__(f"{tag}_button").grid(row=row, column=column)

    def update_record(self, index=None, new_record=None):
        """Update with data"""
        self.table.item(index, text="", values=new_record)

    def select_record(self):
        """Load current selected record."""
        for idx, entry in enumerate(self.header):
            self.__getattribute__(f"{entry}_entry").delete(0, tk.END)

        selected = self.table.focus()
        values = self.table.item(selected, 'values')

        for idx, entry in enumerate(self.header):
            self.__getattribute__(f"{entry}_entry").insert(0, values[idx])

    def deselect_record(self):
        """Discard current selection."""
        for idx, entry in enumerate(self.header):
            self.__getattribute__(f"{entry}_entry").delete(0, tk.END)
        if len(self.table.selection()) > 0:
            self.table.selection_remove(self.table.selection()[0])

    def get_selected_record(self) -> dict:
        """Get the content of the selected record."""
        ans = {}
        for h in self.header:
            ans[h] = self.__getattribute__(f"get_{h}")()
        return ans

    def delete_all(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def insert(self, item):
        self.table.insert("", 'end', iid=None,
                          values=item.as_tuple())


class UsersTable(TableView):
    def __init__(self, controller, create_user_callback, delete_user_callback):
        super().__init__(controller, ("Name", "First_name", "Username", "Role", "Password"))
        super().add_button("create", 4, 1, "create", create_user_callback)
        super().add_button("delete", 4, 4, "delete", delete_user_callback)


class MenuTable(TableView):
    def __init__(self, controller):
        super().__init__(controller, ("Name", "Price", "Stock"))


class OrderTable(TableView):
    def __init__(self, controller):
        super().__init__(controller, ("Dish_list", "Timestamp", "Status"))


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

        self.format_label = tk.Label(self.controller, text="Format")
        self.selected_format = tk.StringVar()
        self.selected_format.set(formats[0])
        self.format_entry = ttk.OptionMenu(self.controller, self.selected_format, *self.formats)
        self.format_entry.grid(row=2, column=3)

        for idx, (entry, tp) in enumerate(entries):
            # create label
            self.__setattr__(f"{entry}_label", tk.Label(self.controller, text=f"{entry}"))
            self.__getattribute__(f"{entry}_label").grid(row=0, column=idx + 1)

            # create entry
            self.__setattr__(f"{entry}_entry", self._get_entry(tp))
            self.__getattribute__(f"{entry}_entry").grid(row=1, column=idx + 1)
            self.__setattr__(f"get_{entry}", lambda *_: self.__getattribute__(f"{entry}_entry").get())

        self.generate_button = ttk.Button(self.controller, text="Generate", command=self.generate_report)
        self.generate_button.grid(row=2, column=2)

    def get_data(self):
        raise NotImplementedError()

    def generate_report(self):
        raise NotImplementedError()


class OrderReportFrame(ReportFrame):
    def __init__(self, controller):
        super().__init__(controller, [
            ("begin", "cal"),
            ("end", "cal"),
            ("format", "frmt"),
        ], ("xml", "csv"))

    def generate_report(self):
        print("Ana are mere")
