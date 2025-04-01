# Funzione per prenotazione
def prenotazioni(lista_concerti, lista_utenti, id):
    
    # Stampa della lista concerti
    print('Lista concerti: ')
    for concerti in lista_concerti:
        print([concerti])
     
        # Scelta concerto
        prenota = int(input('Per quanti concerto vuoi prenotarti? (max 3)'))
        
        if prenota == 1:
            # Scelta concerto da aggiungere
            concerti_scelti = input('Per quale concerto vuoi prenotarti? ')
            if concerti_scelti.lower() in lista_concerti:
                #Aggiunge concerto alla lista di concerti scelti
                lista_utenti[id].append(concerti_scelti)
                # Scala numero posti disponibili
                posti_scelti = int(input(f'Quanti posti vuoi prenotare? {lista_concerti[1]}'))
                lista_concerti[1] - posti_scelti
            
        elif prenota == 2:
            # Ciclo per interrompere al secondo concerto scelto
            contatore = 0
            while contatore < 3:
                concerti_scelti = input('Per quale concerto vuoi prenotarti? ')
                if concerti_scelti.lower() in lista_concerti:
                    #Aggiunge concerto alla lista di concerti scelti
                    lista_utenti[id].append(concerti_scelti)
                    # Scala numero posti disponibili dopo scelta
                    posti_scelti = int(input(f'Quanti posti vuoi prenotare? {lista_concerti[1]}'))
                    lista_concerti[1] - posti_scelti
                    contatore += 1 
                
        elif prenota == 3:
            # Ciclo per interrompere al secondo concerto scelto
            contatore = 0
            while contatore < 4:
                concerti_scelti = input('Per quale concerto vuoi prenotarti? ')
                if concerti_scelti.lower() in lista_concerti:
                    #Aggiunge concerto alla lista di concerti scelti
                    lista_utenti[id].append(concerti_scelti)
                    # Scala numero posti disponibili dopo scelta
                    posti_scelti = int(input(f'Quanti posti vuoi prenotare? {lista_concerti[1]}'))
                    lista_concerti[1] - posti_scelti
                    contatore += 1 

                        