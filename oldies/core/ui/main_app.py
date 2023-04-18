import json
import traceback
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from oldies.core.bll.order_service import OrderService
from oldies.core.bll.menu_service import MenuService
from oldies.core.bll.user_service import UserService

from oldies.core.persistance.repos.repo_factory import RepoFactory
from oldies.core.entities.user import (Role, User)

from oldies.core.ui.components import (UsersTable, MenuTable, OrderTable, OrderReportFrame)

LARGEFONT = ("Verdana", 35)


def load_context(path):
    try:
        with open(path, "r") as f:
            context = json.load(f)
        return context
    except:
        print(f"Failed when loading the context {traceback.format_exc()}")
        raise


class OldiesApp(tk.Tk):

    def _init_services(self) -> None:
        self.repo_factory = RepoFactory(self.context)
        self.order_service = OrderService(order_repo=self.repo_factory.get_order_repo())
        self.menu_service = MenuService(menu_repo=self.repo_factory.get_dish_repo())
        self.user_service = UserService(user_repo=self.repo_factory.get_user_repo())

    def __init__(self, *args, app_context=None, **kwargs):
        self.context = app_context
        self._init_services()

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames[LoginPage] = LoginPage(container, self, self.show_current_frame,
                                           self.user_service)
        self.frames[LoginPage].grid(row=0, column=0, sticky="nsew")

        self.frames[AdminPage] = AdminPage(container, self, self.show_login_page, self.user_service, self.menu_service,
                                           self.order_service)
        self.frames[AdminPage].grid(row=0, column=0, sticky="nsew")

        self.frames[EmployeePage] = EmployeePage(container, self, self.user_service, self.menu_service,
                                                 self.order_service)
        self.frames[EmployeePage].grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_current_frame(self):
        if self.frames[LoginPage].get_user_current_role() == Role.ADMIN:
            self.frames[AdminPage].user = self.frames[LoginPage].get_user()
            self.show_admin_page()
        if self.frames[LoginPage].get_user_current_role() == Role.ADMIN:
            self.frames[EmployeePage].user = self.frames[LoginPage].get_user()
            self.show_employee_page()
        self.show_login_page()

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
    def __init__(self, parent, controller, login_callback, user_service):
        self.user = None
        self.login_callback = login_callback
        self.controller = controller
        self.user_service = user_service

        tk.Frame.__init__(self, parent)

        # title label
        label = ttk.Label(self, text="Welcome to Oldies-Apahida", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        # username/password entries
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

        # remember me logic
        self.remember_me = tk.BooleanVar()
        self.remember_me.set(False)
        self.remember_me_checkbox = tk.Checkbutton(self, text='Remember me', variable=self.remember_me,
                                                   command=lambda *_: self.remember_me.get)
        self.remember_me_checkbox.grid(row=3, column=2)

    def login_call(self):
        self.user = self.user_service.login(self.username_entry.get(), self.password_entry.get())

        if self.user is None:
            messagebox.showerror(title="Login Error", message="Wrong username/password")
            self.user = None
            return

        if self.user.role == Role.EMPLOYEE:
            self.controller.show_employee_page()
        else:
            self.controller.show_admin_page()

        if not self.remember_me.get():
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

        self.login_callback()

    def get_user(self):
        return self.user

    def get_user_current_role(self):
        return self.user.role


class AdminPage(tk.Frame):

    def _init_user_management_frame(self, controller):
        self.users_table = UsersTable(controller, self.create_user_account, self.delete_user_account)

    def _init_my_account_frame(self, controller):
        self.account_info = tk.Text(controller, bg="light yellow")
        self.account_info.grid(row=0, column=0)
        self.logout_button = ttk.Button(controller, text="Logout", command=self.logout_call)
        self.logout_button.grid(row=1, column=0)

    def _init_menu_management_frame(self, controller):
        self.menu_table = MenuTable(controller)

    def _init_report_frame(self, controller):
        self.report_frame = OrderReportFrame(controller)

    def __init__(self, parent, controller, logout_call, user_service, menu_service, order_service):
        tk.Frame.__init__(self, parent)
        self.user = None
        self.controller = controller
        self.logout_call = logout_call
        self.user_service = user_service
        self.menu_service = menu_service
        self.order_service = order_service

        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)

        my_account_frame = ttk.Frame(notebook, width=720, height=400)
        create_account_frame = ttk.Frame(notebook, width=720, height=400)
        menu_manager_frame = ttk.Frame(notebook, width=720, height=400)
        report_frame = ttk.Frame(notebook, width=720, height=400)

        # User management
        self._init_user_management_frame(create_account_frame)

        # Menu management
        self._init_menu_management_frame(menu_manager_frame)

        # Report management
        self._init_report_frame(report_frame)

        # My account
        self._init_my_account_frame(my_account_frame)

        notebook.add(create_account_frame, text='Manage accounts')
        notebook.add(menu_manager_frame, text='Manage Menu')
        notebook.add(report_frame, text='Report section')
        notebook.add(my_account_frame, text='My_account')

        self.refresh_users_table()
        self.refresh_menu()

    def update_user_info(self):
        self.account_info.delete(1.0, tk.END)
        self.account_info.insert(tk.END, str(self.user))

    def refresh_users_table(self):
        self.users_table.delete_all()
        users = self.user_service.list()
        for user in users:
            self.users_table.insert(user)

    def create_user_account(self):
        record = self.users_table.get_selected_record()
        new_user = User(
            name=record["Name"],
            first_name=record["First_name"],
            username=record["Username"],
            role=record["Role"],
            password=record["Password"],
        )
        self.user_service.create_user(new_user)
        self.refresh_users_table()

    def delete_user_account(self):
        record = self.users_table.get_selected_record()
        user = User(
            name=record["Name"],
            first_name=record["First_name"],
            username=record["Username"],
            role=record["Role"],
            password=record["Password"],
        )
        self.user_service.delete_user(user)
        self.refresh_users_table()

    def refresh_menu(self):
        self.menu_table.delete_all()
        dishes = self.menu_service.list()
        for dish in dishes:
            self.menu_table.insert(dish)

    def generate_report(self):
        self.report_frame.generate_report()


class EmployeePage(tk.Frame):
    def _init_order_management_frame(self, controller):
        self.order_table = OrderTable(controller)

    def _init_my_account_frame(self, controller):
        self.account_info = tk.Text(controller, bg="light yellow")
        self.account_info.grid(row=0, column=0)
        self.logout_button = ttk.Button(controller, text="Logout", command=self.logout_call)
        self.logout_button.grid(row=1, column=0)

    def __init__(self, parent, controller, user_service, menu_service, order_service):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user_service = user_service
        self.menu_service = menu_service
        self.order_service = order_service

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
