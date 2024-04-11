letra = 's'
while letra == 's':
   t1 = str(input("Digite o nome de produto:"))
   t2 = str(input("Digite o valor do produto:"))
   t3 = str(input("Digite a descrição do produto:"))
   t4 = str(input("Digite a quantidade do produto:"))
   letra = input("Deseja continuar? [s/n]")

clear()
opcao = input('Deseja exibir os produtos [sim/nao]')
if opcao == 'sim':
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ' )
    for i in range(0, len(nome_produto)):
        print(f'{nome_produto[i]} \t\t {valor_produto[i]} \t\t\t {quantidade_produto[i]} \t\t {descricao_produto[i]}')

