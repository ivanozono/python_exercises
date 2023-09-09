'''
el siguiente juego con reglas muy particulares.
 el juego recibe una lista , que obtendra la suma de sus numeros, 
 hay ciertas condiciones si en la lista se encuentra la letra D se duplicada  la entrada anterior , 
 si encuentra la letra S sumara la dos entradas anterior y la agregara, si encuentra la letra R , 
 tornara a  0 la entrada anterior y la actual. al final dara la suma de la lista.
'''
def juego_con_reglas(lista):
    # Creamos una lista auxiliar para almacenar los resultados intermedios
    resultados = []

    for item in lista:
        if item == 'D':
            if resultados:  # Verificamos si hay elementos anteriores en la lista
                resultados.append(resultados[-1] * 2)
            else:
                resultados.append(0)  # Si no hay elementos anteriores, añadimos 0
        elif item == 'S':
            if len(resultados) >= 2:
                resultados.append(resultados[-1] + resultados[-2])
            elif len(resultados) == 1:  # Si solo hay un elemento, simplemente lo duplicamos
                resultados.append(resultados[-1] * 2)
            else:
                resultados.append(0)  # Si no hay elementos anteriores, añadimos 0
        elif item == 'R':
            if resultados:
                resultados[-1] = 0  # Convertimos el último elemento en 0
                resultados.append(0)  # Añadimos un 0 adicional según las reglas
            else:
                resultados.append(0)  # Si no hay elementos anteriores, añadimos 0
        else:
            resultados.append(item)  # Si es un número, simplemente lo añadimos a la lista

    return sum(resultados)

# Ejemplo de uso
lista = [5, 3, 'D', 4, 'S', 'R', 2]
resultado = juego_con_reglas(lista)
print(f"Resultado final: {resultado}")
