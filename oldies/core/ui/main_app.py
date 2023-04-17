import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import *

from oldies.core.bll.order_service import OrderService
from oldies.core.bll.menu_service import MenuService
from oldies.core.bll.user_service import UserService

from oldies.core.persistance.repos.repo_factory import RepoFactory
from oldies.core.entities.user import (Role, User)

from oldies.core.ui.components import (TableView, ReportFrame)

LARGEFONT = ("Verdana", 35)
context = {
    "database_uri": "mongodb://root:hello@localhost:27017/",
    "db": "mongo",
}


class OldiesApp(tk.Tk):

    def _init_service(self):
        self.user = None
        self.repo_factory = RepoFactory(context)
        self.order_service = OrderService(order_repo=self.repo_factory.get_order_repo())
        self.menu_service = MenuService(menu_repo=self.repo_factory.get_dish_repo())
        self.user_service = UserService(user_repo=self.repo_factory.get_user_repo())

    def __init__(self, *args, **kwargs):
        self._init_service()
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, AdminPage, EmployeePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)

    def login(self, username, password):
        print(f"{username=} {password=}")
        self.user = self.user_service.login(username, password)

    def show_admin_page(self):
        self.frames[AdminPage].update_user_info()
        self.show_frame(AdminPage)

    def show_employee_page(self):
        self.frames[EmployeePage].update_user_info()
        self.show_frame(EmployeePage)

    def show_login_page(self):
        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Welcome to Oldies-Apahida", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        username_label = ttk.Label(self, text="username", font=LARGEFONT)
        username_label.grid(row=1, column=1)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=2)

        passwd_label = ttk.Label(self, text="password", font=LARGEFONT)
        passwd_label.grid(row=2, column=1)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=2)

        login_button = ttk.Button(self, text="Login", command=self.login_call)
        login_button.grid(row=3, column=3, padx=10, pady=10)

        self.remember_me = tk.BooleanVar()
        self.remember_me.set(False)
        self.remember_me.trace('w', lambda *_: print("The value was changed"))
        self.remember_me_checkbox = tk.Checkbutton(self, text='Remember me', variable=self.remember_me,
                                                   command=lambda *_: self.remember_me.get)
        self.remember_me_checkbox.grid(row=3, column=2)

    def login_call(self):
        print(
            f"Vreau sa ma logez ca \nusername:{self.username_entry.get()}\npassword:{self.password_entry.get()}\nremember_me:{self.remember_me.get()}")
        self.controller.login(self.username_entry.get(), self.password_entry.get())

        if self.controller.user is None:
            messagebox.showerror(title="Login Error", message="Wrong username/password")
            return

        if self.controller.user.role == Role.EMPLOYEE:
            self.controller.show_employee_page()
        else:
            self.controller.show_admin_page()

        if not self.remember_me.get():
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)


# second window frame page1
class AdminPage(tk.Frame):

    def _init_user_management_frame(self, controller):
        TableView(controller, ("Name", "First_name", "Username", "Role", "Password"))
        # def update_table_content():
        #     users = self.controller.user_service.list()
        #     iid = 1
        #     for user in users:
        #         table.insert(parent="", index="end", iid=iid, text="",
        #                      values=(user.name, user.first_name, user.username, user.role))
        #         iid += 1
        #
        # update_table_content()
        #
        # def select_record():
        #     # clear entry boxes
        #     name_entry.delete(0, tk.END)
        #     first_name_entry.delete(0, tk.END)
        #     username_entry.delete(0, tk.END)
        #     role_entry.delete(0, tk.END)
        #     password_entry.delete(0, tk.END)
        #
        #     # grab record
        #     selected = table.focus()
        #     # grab record values
        #     values = table.item(selected, 'values')
        #     # temp_label.config(text=selected
        #
        #     # user service call
        #
        #     # output to entry boxes
        #     name_entry.insert(0, values[0])
        #     first_name_entry.insert(0, values[1])
        #     username_entry.insert(0, values[2])
        #     role_entry.insert(0, values[3])
        #
        # def deselect_record():
        #     for item in table.get_children():
        #         table.selection_remove(item)
        #     name_entry.delete(0, tk.END)
        #     first_name_entry.delete(0, tk.END)
        #     username_entry.delete(0, tk.END)
        #     role_entry.delete(0, tk.END)
        #     password_entry.delete(0, tk.END)
        #
        # def update_record():
        #     selected = table.focus()
        #     table.item(selected, text="",
        #                values=(name_entry.get(), first_name_entry.get(), username_entry.get(), role_entry.get(),
        #                        password_entry.get()))
        #     name_entry.delete(0, tk.END)
        #     first_name_entry.delete(0, tk.END)
        #     username_entry.delete(0, tk.END)
        #     role_entry.delete(0, tk.END)
        #     password_entry.delete(0, tk.END)


    def _init_my_account_frame(self, controller):
        self.account_info = tk.Text(controller, bg="light yellow")
        self.account_info.grid(row=0, column=0)
        self.logout_button = ttk.Button(controller, text="Logout", command=self.logout_call)
        self.logout_button.grid(row=1, column=0)

    def _init_menu_managemen_frame(self, controller):
        pass

    def _init_report_frame(self, controller):
        self.report_frame = ReportFrame(controller, [
            ("begin", "cal"),
            ("end", "cal"),
            ("format", "frmt"),
        ], ("xml", "csv"))


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)

        my_account_frame = ttk.Frame(notebook, width=720, height=400)
        create_account_frame = ttk.Frame(notebook, width=720, height=400)
        menu_manager_frame = ttk.Frame(notebook, width=720, height=400)
        report_frame = ttk.Frame(notebook, width=720, height=400)

        # User management
        self._init_user_management_frame(create_account_frame)

        # Menu management
        self._init_menu_managemen_frame(menu_manager_frame)

        # Report management
        self._init_report_frame(report_frame)

        # My account
        self._init_my_account_frame(my_account_frame)

        notebook.add(create_account_frame, text='Manage accounts')
        notebook.add(menu_manager_frame, text='Manage Menu')
        notebook.add(report_frame, text='Report section')
        notebook.add(my_account_frame, text='My_account')

    def logout_call(self):
        self.controller.show_login_page()

    def update_user_info(self):
        self.account_info.delete(1.0, tk.END)
        self.account_info.insert(tk.END, str(self.controller.user))

    def create_user_account(self):
        pass

    def update_menu(self):
        pass

    def generate_report(self):
        pass


class EmployeePage(tk.Frame):
    def _init_order_management_frame(self, controller):
        pass

    def _init_my_account_frame(self, controller):
        self.account_info = tk.Text(controller, bg="light yellow")
        self.account_info.grid(row=0, column=0)
        self.logout_button = ttk.Button(controller, text="Logout", command=self.logout_call)
        self.logout_button.grid(row=1, column=0)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)

        my_account_frame = ttk.Frame(notebook, width=720, height=400)
        order_management_frame = ttk.Frame(notebook, width=720, height=400)

        self._init_order_management_frame(order_management_frame)
        self._init_my_account_frame(my_account_frame)

        notebook.add(order_management_frame, text='Manage orders')
        notebook.add(my_account_frame, text='My_account')

    def logout_call(self):
        self.controller.show_login_page()

    def update_user_info(self):
        self.account_info.delete(1.0, tk.END)
        self.account_info.insert(tk.END, str(self.controller.user))

    def create_order(self):
        pass

    def update_order(self):
        pass

    def update_order_price(self):
        pass
