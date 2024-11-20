OK_RESULT = 'yes'
FATAL_RESULT = 'no'

def check_if_aprove_or_not()-> str:
    result = input("Eres del barça?")

    if isinstance(result, str):
        if result.lower() == OK_RESULT:
            return 'Sabes de futbol'
        return 'No sabes de futbol'
    return 'suspendido por ir de listo'