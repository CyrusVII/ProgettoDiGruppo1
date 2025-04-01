#creiamo la registrazione utente ogni utente deve prima registrarsi con nome e password
#poi deve fare un login e per aggiungere concerti deve inserire una passowrd

#import 
import re

def registrazione_utente(userList):
    # Regex per validazione password
    regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[?!])[A-Za-z\d?!]{8,}$"

    while True:
        # Inseriamo il nome utente
        userName = input("Inserisci un nome utente: ")

        # Controllo se il nome utente è già presente
        nome_gia_esistente = False
        for sotto_lista in userList:
            for utente in sotto_lista:
                if utente[0] == userName:
                    print("Nome utente già esistente, scegline un altro.")
                    nome_gia_esistente = True
                    break
            if nome_gia_esistente:
                break

        if not nome_gia_esistente:
            break  # Se il nome utente non esiste, usciamo dal ciclo

    # Validazione della password
    while True:
        password = input("Inserisci una password valida: ")
        if re.match(regex, password):
            print("Password valida!")
            break
        else:
            print("Password non valida. Deve contenere almeno 8 caratteri, una maiuscola, un numero e un carattere speciale tra ? e !. Riprova.")

    # Salviamo l'utente nella lista
    userList.append([[userName, password]])
    print("Registrazione completata con successo!")

    
#login utente
def login_utente(userList):
    while True:
        # Inserimento del nome utente
        userName = input("Inserisci il tuo nome utente: ")
        userPassword = input("Inserisci la tua password: ")
        
        # controllo utente
        for i in userList:
          for s in userList:
            if s[0] == userName and s[1] == userPassword:
              print("Accesoo riuscito")
              return userList.index(s)
            else:
              pass
        
        
        
user = [['pippo','pluto'], ['vale','sandro']]
concerti = [['nome concerto', 10]]
login_utente(user)