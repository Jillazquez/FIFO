OK_RESULT = 'yes'
FATAL_RESULT = 'no'
PEPE = 9
CONTO = 124134134134

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

def pay_referee():

    def check_conto():
        return CONTO

    if check_conto > 10000:
        CONTO - 10000
check_if_aprove_or_not()
pay_referee()