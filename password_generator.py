import secrets
import string
# import random

def generate_password(
    length: int = 19,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
)-> str: 
    
    #per la lenght data come parametro, chiamare una delle funzioni e pushare il valore dentro la variabile password
    password = ""
        
    # funzioni separate per generare lettere maiuscole, minuscole, numeri e simboli
    def gen_upper(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.ascii_uppercase)
        return stringa

    def gen_lower(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.ascii_lowercase)
        return stringa

    def gen_digits(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.digits)
        return str(stringa)

    def gen_symbols(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.punctuation)
        return str(stringa)




    #per ogni carattere pushare il risultato di una delle funzioni, in modo da avere una password che contenga tutti i tipi di caratteri, e che sia lunga quanto la lenght data come parametro.
    array_passw = []
    funzioni = [gen_upper, gen_lower, gen_digits, gen_symbols]

    if use_upper == False:
        funzioni.remove(gen_upper)
    if use_lower == False:
        funzioni.remove(gen_lower)
    if use_digits == False:
        funzioni.remove(gen_digits)
    if use_symbols == False:
        funzioni.remove(gen_symbols)



    while len(array_passw) < length:
        array_passw.append(secrets.choice(funzioni)())

    # return print(gen_upper(1) + gen_lower(1) + gen_digits(1) + gen_symbols(1))
    # print(secrets.token_urlsafe(length)) # torna una stringa casuale di lunghezza lenght, composta da lettere, numeri e simboli.
    # print(secrets.choice(string.ascii_letters + string.digits))
    return print (array_passw)


generate_password()



print("Generating password...")