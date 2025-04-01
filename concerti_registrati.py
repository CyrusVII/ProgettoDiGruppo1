
def password():
    richiesta_pass = input("Prima di registrarti, inserisci la password: ").upper() #non permetto al cliente di scrivere in minuscolo
    
    if richiesta_pass == "GHIBLI":
        return True
    else:
        return False

# Esempio di utilizzo della funzione
if password():
    print("Accesso consentito!")
else:
    print("Password errata. Accesso negato.")
# registrazione dei concerti
def req_concerti ():
   utente = input("Vuoi procedere con la registrazione al concerto? (si/no)")
   if utente == "si":
       return True
   else:
        return False

       
   
   
   
if req_concerti ():
        print("procediamo!")
else:
        print("va bene sarà per la prossima ")
        
        
    


    



