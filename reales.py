def es_real(lexema):
    Q0 = 0
    Q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    F = [6, 7]

    estado_actual = Q0
    indice = 0

    SIGMA = {
        "DIGITO": 0,
        "MAS": 1,
        "MENOS": 2,
        "PUNTO": 3,
        "e": 4,
        "E": 5,
        "OTRO": 6
    }

    DELTA = [
        [2, 1, 1, 3, 8, 8, 8], # transiciones de Q0
        [2, 8, 8, 3, 8, 8, 8], # transiciones de Q1
        [2, 8, 8, 6, 8, 8, 8], # transiciones de Q2
        [6, 8, 8, 8, 8, 8, 8], # transiciones de Q3
        [7, 8, 8, 8, 8, 8, 8], # transiciones de Q4
        [7, 4, 4, 8, 8, 8, 8], # transiciones de Q5
        [6, 8, 8, 8, 5, 5, 8], # transiciones de Q6
        [7, 8, 8, 8, 8, 8, 8], # transiciones de Q7
        [8, 8, 8, 8, 8, 8, 8]  # transiciones de Q8 (estado de rechazo)
    ]

    def simbolo(caracter):
        if caracter >= '0' and caracter <= '9':
            return SIGMA["DIGITO"]
        
        elif caracter == '+':
            return SIGMA["MAS"]
        
        elif caracter == '-':
            return SIGMA["MENOS"]
        
        elif caracter == '.':
            return SIGMA["PUNTO"]
        
        elif caracter == 'e':
            return SIGMA["e"]
        
        elif caracter == 'E':
            return SIGMA["E"]
        
        else:
            return SIGMA["OTRO"]

    while indice < len(lexema) and estado_actual != 8:
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]

        indice += 1

    return estado_actual in F
