def is_prim(number):
    '''
    Verifică dacă un număr este prim\n
    :param number: Număr natural
    :return: True -> numărul este prim sau False -> numărul nu este prim
    '''
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for divizor in range(3, number // 2, 2):
        if number % divizor == 0:
            return False

    return True
    pass


def get_longest_all_not_prime(lista: list[int]):
    '''
    Verifică dacă toate numerele sunt neprime
    :param lista: Lista
    :return: True -> dacă toate numerele sunt neprime sau False -> dacă există numere prime
    '''
    for items in lista:
        if is_prim(items):
            return False
    return True
    pass


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([4, 6, 12, 18]) is True
    assert get_longest_all_not_prime([4, 2, 9, 12]) is False
    assert get_longest_all_not_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) is False



def Problema_1(lista):
    '''
    Calculeaza subsecventa car
    :param lista:
    :return:
    '''
    subsecventa_finala = []
    subsecventa_temporala = []
    for inceput in range(0, len(lista)):
        for sfarsit in range(inceput + 1, len(lista)):
            if get_longest_all_not_prime(lista[inceput:sfarsit]) is True:
                subsecventa_temporala = lista[inceput:sfarsit]
                if len(subsecventa_finala) < len(subsecventa_temporala):
                    subsecventa_finala = subsecventa_temporala[:]
                    subsecventa_temporala = []
                pass
            else:
                break
    return subsecventa_finala
    pass


def verificare_cifre_prime(numar):
    str_nr = str(numar)
    for cifre in range(0, len(str_nr)):
        cifra_verificare = int(str_nr[cifre])
        if not is_prim(cifra_verificare):
            return False
    return True
    pass


def test_verificare_cifre_prime():
    assert verificare_cifre_prime(23257) is True
    assert verificare_cifre_prime(232457) is False
    assert verificare_cifre_prime(2223) is True
    assert verificare_cifre_prime(123) is False


def subsecventa_verificare_sir(lista: list):
    for el in lista:
        if not verificare_cifre_prime(el):
            return False

    return True
    pass


def get_longest_prime_digits(lista: list):
    subsecventa_finala = []
    subsecventa_temp = []
    for inceput in range(0, len(lista)):
        for sfarsit in range(inceput + 1, len(lista) + 1):
            if subsecventa_verificare_sir(lista[inceput:sfarsit]) is True:
                subsecventa_temporala = lista[inceput:sfarsit]
                if len(subsecventa_finala) < len(subsecventa_temporala):
                    subsecventa_finala = subsecventa_temporala[:]
                    subsecventa_temporala = []
                pass
            else:
                break
    return subsecventa_finala
    pass


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2, 3, 2, 3, 2, 1, 2, 3, 2, 1, 5]) == [2, 3, 2, 3, 2]
    assert get_longest_prime_digits([1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 3, 3, 3, 5, 5, 5, 7, 1]) == [3, 3, 3, 5, 5, 5, 7]




def citire_lista():
    lista = [int(e) for e in input('Introduceti elementele separate prin spatiu: ').split(' ')]
    return lista




def meniu():
    test_get_longest_all_not_prime()
    test_get_longest_prime_digits()
    test_verificare_cifre_prime()

    sa_vedem = []

    while True:
        print('''
        1. Citire lista
        2.Toate numerele sunt neprime.
        3.Toate numerele sunt formate din cifre prime.
        4.Iesire''')
        cmd = input('Command: ')

        if cmd == '1':
            pass
            sa_vedem = citire_lista()
        elif cmd == '2':
            print(Problema_1(sa_vedem))
        elif cmd == '3':
            print(get_longest_prime_digits(sa_vedem))
        elif cmd == '4':
            break

    pass

meniu()