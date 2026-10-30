# Classe pour gerer exception avec mauvaise creation d 'utilisateurs

class PasswordException(Exception):
    def __init__(self, msg ="Mot de passe incorrect",*args):
        super().__init__(msg,*args)
        if len(msg)<6 :
            return      