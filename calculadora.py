def calcular_imc(pes, alt):
    return int(pes) / float(alt) ** 2

def mens_sit(imc):
    if imc < 20:
        return 'Abaixo do Peso'
    elif imc < 25:
        return 'Normal'
    elif imc < 30:
        return 'Excesso de Peso'
    elif imc < 35:
        return 'Obesidade'
    else:
        return 'Obesidade Mórbida'