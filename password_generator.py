import secrets
import string
# import random

def generate_password(
    length: int = 8,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
)-> str: 
        
    gen_upper_check = False
    gen_lower_check = False
    gen_digits_check = False
    gen_symbols_check = False    

    # se tutti i flag dei set sono False, o se length è minore del numero di set abilitati, solleva ValueError con un messaggio parlante
    if not (use_upper or use_lower or use_digits or use_symbols):
        raise ValueError("Almeno uno dei set di caratteri deve essere abilitato.")


    # funzioni separate per generare lettere maiuscole, minuscole, numeri e simboli
    def gen_upper(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.ascii_uppercase)
        nonlocal gen_upper_check
        gen_upper_check = True
        return stringa

    def gen_lower(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.ascii_lowercase)
        nonlocal gen_lower_check
        gen_lower_check = True
        return stringa

    def gen_digits(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.digits)
        nonlocal gen_digits_check
        gen_digits_check = True
        return str(stringa)

    def gen_symbols(n: int = 1) -> str:
        stringa = ""
        for i in range(n):
            stringa += secrets.choice(string.punctuation)
        nonlocal gen_symbols_check  
        gen_symbols_check = True
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

   
    if ((gen_upper_check == False and use_upper == True) or (gen_lower_check == False and use_lower == True) or (gen_digits_check == False and use_digits == True) or (gen_symbols_check == False and use_symbols == True)):
        if length > len(funzioni):
            
            generate_password()
            # raise ValueError("la password non è stata generata correttamente... riprova.")

    password = ''.join(array_passw)
    return print (password)


print("Generating password...")
generate_password()






# return print(gen_upper(1) + gen_lower(1) + gen_digits(1) + gen_symbols(1))
# print(secrets.token_urlsafe(length)) # torna una stringa casuale di lunghezza lenght, composta da lettere, numeri e simboli.
# print(secrets.choice(string.ascii_letters + string.digits))


