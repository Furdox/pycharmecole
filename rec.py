def tamaman(a: float, b: float, c: float):
    """
    Vérifie si un triangle est rectangle.
    :param a:
    :param b:
    :param c:
    :return: True or False
    """

    if a ** 2 + b ** 2 == c ** 2:
        print("Miaou :3")
        return True
    else:
        print(";w;")
        return False


input_a = float(input("Entrez la valeur a: "))
input_b = float(input("Entrez la valeur b: "))
input_c = float(input("Entrez la valeur c: "))
tamaman(input_a, input_b, input_c)