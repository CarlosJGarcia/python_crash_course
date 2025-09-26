# Uso de 'continue' dentro de un bucle para terminar la iteración actual y saltar al inicio del bucle
# A diferencia de 'break' no sale del bucle, solo sale de la iteración actual, ignorando el resto y saltando al if/for/while

n = 0
while n < 10:
    n += 1

    if n % 2 != 0:
        continue

    print(n)
