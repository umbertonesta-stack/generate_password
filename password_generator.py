import secrets
import string


def generate_password(
    length: int = 19,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
)-> str: 
    
    password = ""



    # funzioni separate per generare lettere maiuscole, minuscole, numeri e simboli
    def gen_upper(n) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.ascii_uppercase)
        return stringa

    def gen_lower(n) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.ascii_lowercase)
        return stringa

    def gen_digits(n) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.digits)
        return str(stringa)

    def gen_symbols(n) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.punctuation)
        return str(stringa)








    return print(gen_upper(1) + gen_lower(1) + gen_digits(1) + gen_symbols(1))


    # print(secrets.token_urlsafe(length)) # torna una stringa casuale di lunghezza lenght, composta da lettere, numeri e simboli.

    # print(secrets.choice(string.ascii_letters + string.digits))
    # return password


generate_password()



print("Generating password...")