def Prime(number):
    """
    Verifică dacă un număr este prim\n
    :param number: Număr natural
    :return: True -> numărul este prim sau False -> numărul nu este prim
    """
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


def verifica_numere_care_nu_sunt_prime(lista: list[int]):
    """
    Verifică dacă numerele din lista nu sunt prime
    :param lista: Lista cu numerele
    :return: True -> dacă toate numerele sunt neprime sau False -> dacă există numere prime
    """
    for items in lista:
        if Prime(items):
            return False
    return True
    pass


def verificare_cifre_prime(numar):
    """
    Verifica daca cifrele unui numar sunt prime
    :param numar:
    :return:
    """
    string_transform = str(numar)
    for digits in range(0, len(string_transform)):
        digits_verify = int(string_transform[digits])
        if not Prime(digits_verify):
            return False
    return True


def subsecventa_verificare_sir(lista: list):
    for elements in lista:
        if not verificare_cifre_prime(elements):
            return False
    return True


def list_read_function():
    list_read = [int(numbers) for numbers in input('Insert elements: ').split(' ')]
    return list_read


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2, 3, 22, 55, 2552, 1, 11, 12, 98]) == [2, 3, 22, 55, 2552]
    assert get_longest_prime_digits([1, 3, 11, 55, 25, 76]) == [55, 25]
    assert get_longest_prime_digits([98, 55, 66, 45, 3, 2, 3, 54, 56]) == [3, 2, 3]


def test_get_longest_all_not_prime():
    assert verifica_numere_care_nu_sunt_prime([25, 36, 713, 388]) is True
    assert verifica_numere_care_nu_sunt_prime([45, 11, 67, 512]) is False
    assert verifica_numere_care_nu_sunt_prime([12, 13, 14, 15]) is False


def test_verificare_cifre_prime():
    assert verificare_cifre_prime(757372) is True
    assert verificare_cifre_prime(23715773257) is False
    assert verificare_cifre_prime(2735772223) is True
    assert verificare_cifre_prime(9876543234567123) is False


# Prima problema
def get_longest_all_not_prime(the_list):
    """
    Calculeaza subsecventa de siruri care nu sunt prime
    :param lista: O lista cu numere
    :return:Returneaza cea mai lunga subsecventa de siruri
    """
    final_list = []
    temp_list = []
    for left in range(0, len(the_list)):
        for right in range(left + 1, len(the_list)):
            if verifica_numere_care_nu_sunt_prime(the_list[left:right]) is True:
                temp_list = the_list[left:right]
                if len(final_list) < len(temp_list):
                    final_list = temp_list[:]
                    temp_list = []
                pass
            else:
                break
    return final_list


# A doua problema
def get_longest_prime_digits(the_list: list):
    '''
    Calculeaza subsecventa de siruri in care numarul este format din cifre prime
    :param the_list:
    :return: Returneaza cea mai lunga subsecventa de siruri
    '''
    final_list = []
    temp_list = []
    for left in range(0, len(the_list)):
        for right in range(left + 1, len(the_list) + 1):
            if subsecventa_verificare_sir(the_list[left:right]) is True:
                temp_list = the_list[left:right]
                if len(final_list) < len(temp_list):
                    final_list = temp_list[:]
                    temp_list = []
                pass
            else:
                break
    return final_list


# A treia problema
def get_longest_sorted_asc(the_list: list):
    '''
    Functia verifica daca elementele sunt sortate in ordine crescatoare
    :param the_list:
    :return: True daca sunt False daca nu sunt
    '''
    minim = -1
    for element in the_list:
        if element > minim:
            minim = element
        else:
            return False
    return True
    pass


def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 2, 3, 4, 5, 6, 7, 100]) is True
    assert get_longest_sorted_asc([3, 2, 1, 5, 3, 4, 5, 6]) is False
    assert get_longest_sorted_asc([10, 100, 1000, 10000, 1000000]) is True
    assert get_longest_sorted_asc([1000, 100, 10, 1]) is False


def test_func():
    test_get_longest_all_not_prime()
    test_get_longest_prime_digits()
    test_verificare_cifre_prime()
    test_get_longest_sorted_asc()


def print_menu():
    print('''
1. Read the list.
2. Get longest all not prime.
3. Get longest prime digits.
4. Get longest sorted asc
5. Exit
''')


def menu():
    the_list = []
    test_func()
    while True:
        print_menu()
        command = input('Select one option: ')

        if command == '1':
            the_list = list_read_function()
        elif command == '2':
            print(get_longest_all_not_prime(the_list))
        elif command == '3':
            print(get_longest_prime_digits(the_list))
        elif command == '4':
            if get_longest_sorted_asc(the_list):
                print('Numerele sunt ordonate crescator')
            else:
                print('Numerele nu sunt ordonate crescator')
        elif command == '5':
            break


menu()
