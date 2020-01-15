dict = {
    'unidades': ('uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'),
    'decenas': ('diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta',
                'ochenta', 'noventa'),
    'centesimas': ('cien', 'ciento', 'doscientos', 'tresciento', 'cuatrocientos', 'quinientos',
                   'seisientos', 'sietesientos', 'ochocientos', 'novecientos'),
    'millares': ('mil',)
}


def number_to_words(num):
    answer = ''

    converted = [int(c) for c in str(num)]

    if num > 1000:
        answer = "!! ERROR: El numero ingresado es mayor a 1000. "
    else:
        print("Numero: ", converted)
        if len(converted) == 4:
            answer = dict['millares'][0]
        elif len(converted) == 3:
            answer += centesimas(converted)
        elif len(converted) == 2:
            answer = decenas(converted)
    '''
    if converted > 1:
        answer = '!! ERROR: El numero ingresado es mayor a 1000. '
    if converted == 1:
        answer = dict['millares'][0]

    print("mil: ", num/1000)
    print("cien: ", num/100)
    print("diez: ", num/10)
    print("uno: ", num/1)
    print([int(d) for d in str(num)])
    print(answer)
    '''
    return answer


def centesimas(converted):
    answer = ""
    if converted[0] == 1 and converted[1] == 0 and converted[2] == 0:
        answer = dict['centesimas'][0]
    else:
        if converted[0] == 1:
            answer += dict['centesimas'][1]
        elif converted[0] == 2:
            answer += dict['centesimas'][2]
        elif converted[0] == 3:
            answer += dict['centesimas'][3]
        elif converted[0] == 4:
            answer += dict['centesimas'][4]
        elif converted[0] == 5:
            answer += dict['centesimas'][5]
        elif converted[0] == 6:
            answer += dict['centesimas'][6]
        elif converted[0] == 7:
            answer += dict['centesimas'][7]
        elif converted[0] == 8:
            answer += dict['centesimas'][8]
        elif converted[0] == 9:
            answer += dict['centesimas'][9]

        answer += " "
        answer += decenas(converted[1:3])
    return answer


def decenas(converted):
    answer = ""
    if converted[0] == 0 and converted[1] == 0:
        return ""
    elif converted[0] == 1:
        answer += dict['decenas'][0]
    elif converted[0] == 2:
        answer += dict['decenas'][1]
    elif converted[0] == 3:
        answer += dict['decenas'][2]
    elif converted[0] == 4:
        answer += dict['decenas'][3]
    elif converted[0] == 5:
        answer += dict['decenas'][4]
    elif converted[0] == 6:
        answer += dict['decenas'][5]
    elif converted[0] == 7:
        answer += dict['decenas'][6]
    elif converted[0] == 8:
        answer += dict['decenas'][7]
    elif converted[0] == 9:
        answer += dict['decenas'][8]
    answer += unidades(converted[1])
    return answer


def unidades(unidad):
    answer = " y "
    if unidad == 1:
        answer += dict['unidades'][0]
    elif unidad == 2:
        answer += dict['unidades'][1]
    elif unidad == 3:
        answer += dict['unidades'][2]
    elif unidad == 4:
        answer += dict['unidades'][3]
    elif unidad == 5:
        answer += dict['unidades'][4]
    elif unidad == 6:
        answer += dict['unidades'][5]
    elif unidad == 7:
        answer += dict['unidades'][6]
    elif unidad == 8:
        answer += dict['unidades'][7]
    elif unidad == 9:
        answer += dict['unidades'][8]

    return answer


print(number_to_words(783))
