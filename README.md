# TEMA 1 PS  

Restaurantul Oldies din Apahida are nevoie de o aplicatie pentru gestiunea comenzilor. Fiind mai retro, managerul restaurantului isi doreste in prima faza ca restaurantul sa aiba un good old desktop app, care sa permita inregistrarea comenzilor plasate de clienti in restaurant.  

Accesul la aplicație se face pe baza de login. Vor exista doua tipuri de utilizatori: angajati si administratori.  

Administratorii vor putea sa creeze conturi pentru angajati (nume, username, parola). De asemenea, administratorii vor putea sa gestioneze meniul pe care il serveste restaurantul (nume preparat, pret, stoc). Stocul reprezinta numarul de produse disponibile din acel preparat si va putea fi actualizat periodic de catre administratori.  

Angajatii vor putea dupa login sa inregistreze in sistem comenzi. Comenzile vor contine o lista de preparate si vor avea un cost total. De asemenea, comenzile vor avea un status (comanda noua, comanda in pregatire, comanda finalizata). Angajatii vor putea sa modifice statusul comenzii. Pentru fiecare comanda se va salva si data si ora la care a fost plasata. Angajatii nu vor putea adauga in comanda preparate care nu mai sunt in stoc.  

Administratorii vor putea sa vada rapoarte cu toate comenzile intre 2 date calendaristice si vor putea sa vada statistici cu cele mai comandate produse. Administratorii pot exporta aceste rapoarte intr-un fisier (in format csv sau xml). 

 

# CONSTRANGERI 

Datele vor fi salvate intr-o baza de date. 

Pentru tema 1 se va realiza o aplicatie Desktop  

Se va folosi pattern-ul arhitectural Layers pentru proiectarea si organizarea aplicatiei.  

Parolele vor fi salvate criptat in baza de date 

# CERINTE 

Documentul de analiza si design (diagrame use case + diagrama de clase) 

Implementarea si testarea aplicatiei.  

# OBSERVATIE 

Pentru tema 1 nu se va implementa generarea si exportul de rapoarte in csv/xml  

TERMEN DE PREDARE 

2 saptamani: in prima saptamana se va preda documentul de analiza si design (diagrame), in a doua saptamana se va preda implementarea (implementarea se va face doar după validarea diagramelor) 

Pentru fiecare săptămână de întârziere se va scădea 1 punct din nota finala 

Se accepta un delay de maxim 2 saptamani 

 
