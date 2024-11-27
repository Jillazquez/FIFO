OK_RESULT = 'yes'
FATAL_RESULT = 'no'
import pdb

def check_if_aprove_or_not()-> str:
    result = input("Eres del barça?")

    if isinstance(result, str):
        if result.lower() == OK_RESULT:
            return 'Sabes de futbol'
        for x in range(0,15):
            r = input("Seguro?")
            pdb.set_trace()
            if isinstance(r,str):
                return "Salvado por la campana"
        return 'No sabes de futbol'
    return 'suspendido por ir de listo'

check_if_aprove_or_not()