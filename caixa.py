print('----Caixa eletrônico----')

saldo = 1000

print('Bem-vindo!')
print('"1"- Saque')
print('"2"- Deposito')
print('"0"- Encerrar seção')

while True:
    operacao = int(input('Qual operação deseja realizar: '))

    if operacao == 1:
        print('Saque')
        saque = int(input('Quanto você deseja sacar? '))
        saldo -= saque

        if saque > saldo:
            print('Saldo insuficiente, tente novamente.')
            break

        else:
            print('Saque realizado com sucesso.')
        print(f'Novo saldo: {saldo}')
        print()
        
    elif operacao == 2:
        print('Deposito')
        deposito = int(input('Qual o valor do deposito? '))
        saldo += deposito
        print(f'Novo saldo: {saldo}')
        continue
    
    elif operacao == 0:
        print('Obrigado.')
        break

    else:
        print('Por favor, digite 1, 2 ou 0.')
        continue    
