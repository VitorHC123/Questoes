def fibonacci(num):
    def quad(x):
        s = int(x ** 0.5)
        return s * s == x

    return quad(5 * num * num + 4) or quad(5 * num * num - 4)

numero = 21

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")