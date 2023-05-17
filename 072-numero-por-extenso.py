numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
opcao = 'sim'
while True:
    if opcao == 'sim' or opcao == 's' or opcao == 'Sim' or opcao == 'S':
        num = int(input("Digite um número de 0 a 20: "))
        if num >= 0 and num <= 20:
            print(f"Você digitou o número {numeros[num]}.") #a posição do número é igual ao número pedido
            opcao = input("Deseja continuar? ")
        else:
            print("Tente novamente. ", end='')
            opcao = input("Deseja continuar? ")
