def penistemp(c: float):
    """
    Convertire une température celsius en fahrenheit
    :param c: la température en celsius
    :param f: la temperature en fahrenheit
    :return:
    """
    f = c * 9 / 5 + 32
    return f


temp_c = float(input("sex c"))
temp_f = penistemp(temp_c)
print("temp", temp_f)