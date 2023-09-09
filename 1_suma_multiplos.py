# Suma de todos los múltiplos de 3 o 5 menores que N* 
# Dado un número entero N, calcula la suma de todos los números menores que N que son múltiplos de 3 o 5

def sum_multiplos (n):
    return sum (x for x in range(n)if x % 3 == 0 or x % 5 == 0 )




if __name__ == '__main__':
    N = int (input(" Enter a number N : "))
    print (f"sum of all multiples of 3 or 5 less than {N} is : {sum_multiplos(N)}")