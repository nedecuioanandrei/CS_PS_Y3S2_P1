- [] Login
	- [] angajati
		- [] nume 
		- [] username 
		- [] parola  
		- [] inregistrare comanda 
			- lista de preparate 
	- [] admin 
		- [] gestioneaza menu-ul 
			- (nume, preparet, pret, stoc)
- [] 

class 

	OldiesApp 
		- order_service 
		- user_service
		- menu_service
	
		-> LoginPage 
			- login_call [x] Done
		-> AdminPage
			- logout_call [x] Done
			- update_user_info
			- refresh_users_table []
				"""Dump all users in the table"""

			- create_user_account []
				"""Inser a new account into db"""
			- update_menu []
				"""Update a record from the menu"""
			- generate_report []
				"""Generate report given a query"""
 
		-> EmployeePage
			- logout_call [x] Done
			- update_user_info [x] Done 
			- crate_order [] 
			- update_order [] 
			- update_order_price [] 		


