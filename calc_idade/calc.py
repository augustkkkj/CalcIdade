#sistema de calcular idade junto com calculadora

while True:
    print('\n====Sistema de idade com calculadora====')
    print('1- Adivinhar Idade')
    print('2- Calculadora')
    print('3- sair')

    opcao = input('digite qual atividade deseja: ')
    
    if opcao == '3':
        print('obrigado por usar')
        break


    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = num1 - num2
        print(f'sua idade é: {resultado} anos')

    elif opcao == '2':
        print("\nCalculadora Simples:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        if calc == '5':
            print('falou')
            break

        calc = int(input('escolha uma operação: '))
    
    elif calc == '1':
         resultado = num1 + num2
         print("Resultado:", resultado)

        




