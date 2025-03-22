def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b
def potenciação(a, b):
    return a ** b

def calculadora():
    print("Bem-vindo à Calculadora em Python!")
    while True:
        print("\nEscolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - potenciação")
        print("6 - Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '6':
            print("Encerrando a calculadora...")
            break

        if escolha not in ['1', '2', '3', '4','5']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida! Digite apenas números.")
            continue

        if escolha == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")
        elif escolha == '5':
            print(f"Resultado: {potenciação (num1, num2)}")

if __name__ == "__main__":
    calculadora()