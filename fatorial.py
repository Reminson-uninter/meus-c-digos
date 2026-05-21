def fatorial(n):
    if n <= 0:
        return None
    elif n == 0 or n == 1:
        print(f"Retornando 1 para n={n}")
        return 1
    else:
        print(f"Calculando {n} * fatorial({n-1})")
        return n * fatorial(n - 1)

print(f'Resultado: {fatorial(4)}')
