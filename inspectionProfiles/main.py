# Pedimos para o usuário inserir um número
num = int(input("Insira um número inteiro: "))

# Definimos os dois primeiros valores da sequência
fib1 = 0
fib2 = 1

# Se o número for igual a um dos primeiros valores, ele pertence à sequência
if num == fib1 or num == fib2:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    # Calculamos a sequência de Fibonacci até encontrar um número maior ou igual ao que foi informado pelo usuário
    while fib2 < num:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum

        # Se encontrarmos o número na sequência, imprimimos a mensagem e encerramos o loop
        if fib2 == num:
            print(f"O número {num} pertence à sequência de Fibonacci!")
            break
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
