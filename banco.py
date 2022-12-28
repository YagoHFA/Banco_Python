from ContaB import Conta




c = Conta()

while True:
    ops = int(input('''
[0] Para cadastar cliente
[1] Para vincular Conta Bacaria
[2] Ir para Operaçoes
[3] Para Sair \n'''))
    if ops == 0:
        
    if ops == 1:
       
    if ops == 3:
        break    
    if ops == 2:


        while True:

            op = input(
                    '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair\n'''
                    )
            if op == 'd':
                des = float(input("Deposite um valor: "))
                c.depositar(des)  
            if op == 's':
                sac = float(input("Retire um valor: "))
                c.sacar(sac)
            if op == 'e':
                print("Extrato:")
                print(c.extrato())
            if op == 'q':
                break    
            






