# calculadora.py

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def menu():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Digite a opção (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Saindo...")
            break
        
        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida, tente novamente.")
            continue
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado é: {soma(num1, num2)}")
        elif escolha == '2':
            print(f"O resultado é: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"O resultado é: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"O resultado é: {divisao(num1, num2)}")

# Executa a calculadora
calculadora()
