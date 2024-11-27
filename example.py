OK_RESULT = 'yes'
FATAL_RESULT = 'no'
PEPE = 9
PLAYERS = []

def check_if_aprove_or_not()-> str:
    result = input("Eres del barça?")

    if isinstance(result, str):
        if result.lower() == OK_RESULT:
            return 'Sabes de futbol'
        for x in range(0,15):
            r = input("Seguro?")
            if isinstance(r,str):
                return "Salvado por la campana"
        return 'No sabes de futbol'
    return 'suspendido por ir de listo'

def add_players_to_list():
    while PLAYERS.__len__() < 11:

        r = input("Dime un jugador del barça")
        if isinstance(r,str):
            PLAYERS.append(r)


check_if_aprove_or_not()