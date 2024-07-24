def es_real(lexema):
    Q0 = 0
    Q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    F = [5, 6]

    estado_actual = Q0
    indice = 0

    SIGMA = {
        "MENOS": 0,
        "MAS": 1,
        "DIGITO": 2,
        "PUNTO": 3,
        "e": 4,
        "E": 5,
        "OTRO": 6
    }

    DELTA = [
        [1, 1, 2, 7, 8, 8, 8], # transiciones de Q0
        [8, 8, 2, 7, 8, 8, 8], # transiciones de Q1
        [8, 8, 2, 5, 4, 4, 8], # transiciones de Q2
        [8, 8, 6, 8, 8, 8, 8], # transiciones de Q3
        [3, 3, 6, 8, 8, 8, 8], # transiciones de Q4
        [8, 8, 5, 8, 4, 4, 8], # transiciones de Q5
        [8, 8, 6, 8, 8, 8, 8], # transiciones de Q6
        [8, 8, 5, 8, 8, 8, 8],  # transiciones de Q7
        [8, 8, 8, 8, 8, 8, 8] # transiciones de Q8
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
