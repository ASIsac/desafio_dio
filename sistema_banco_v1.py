menu = '''
\n========== MENU ==========
 --->  [1] DEPÓSITO  <---
 --->  [2] SAQUE     <---
 --->  [3] EXTRATO   <---
 --->  [4] SAIR      <---
==========================
--> '''

deposito = 0
extrato = ''
saque = 0
saldo = 0
limite = 500
quantidade_saques = 1
quantidade_deposito = 0

while True:
    opcao = input(menu)
    
    if opcao == '1': # depósito na conta corrente
        deposito = float(input('\nValor a depositar: R$ '))
        
        if deposito > 0:
            saldo += deposito
            quantidade_deposito += 1
            extrato += f'Deposito {quantidade_deposito}: R$ {deposito:.2f}\n'
            print(f'\nSaldo: ---> R$ {saldo:.2f} <---\n')
        else:
            print('Valor inválido !')
    
    elif opcao == '2': # saque da conta corrente
        
        print(f'Saldo disponível: R$ {saldo:.2f}')
        saque = float(input('Digite o valor que você deseja sacar: R$ '))
        
        if saldo == 0:
            print('Sem saldo!')

        elif saque > saldo:
            print('\nErro na operação de saque')
        
        elif saque > limite:
            print('\nErro na operação de saque. Valor excede o limite')
        
        elif quantidade_saques > 3:
            print('\nLimite de saques diários atingidos')
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque {quantidade_saques}: R$ {saque:.2f}\n"
            quantidade_saques += 1
        else:
            print('Erro na operação')
                
    elif opcao == '3': # extrato da conta corrente

        print('============ EXTRATO ==============')

        if not extrato:
            print('NÃO FORAM REALIZADAS MOVIMENTAÇÕES')
        
        elif saldo > 0:
            print(extrato)
            print(f'\nSaldo Atual: R$ {saldo:.2f}')
            
        else:
            print('\nNão foram realizadas movimentações!')
        print('===================================\n')
    
    elif opcao == '4': # sair do sistema
        break
    else: # caso o usuáriop digite algo fora
        print('\n Operação inválida!')
        print ('Digite novamente a operação desejada.\n')

print('\n= = = = = = = = = = = = = = = = = = = ')
print('| Obrigado por usar o nosso sistema |')
print('|           Até a próxima!          |')
print('= = = = = = = = = = = = = = = = = = = \n')
