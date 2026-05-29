while True:
    try:
        valor_da_conta = float(input(f'Qual o valor da conta '))
    except ValueError:
        print('\n---Desculpe, digite apenas numeros---\n')
        continue
    taxa_de_gorjeta = valor_da_conta * 0.10
    print(f'Deseja pagar o valor de {taxa_de_gorjeta:.2f} como taxa de serviço ?')
    resposta_do_usuario = input(f'Digite: s ou n ')
    if resposta_do_usuario == ('s'):
            print(f'Valor total da conta é: {valor_da_conta + taxa_de_gorjeta:.2f}')
            break
    elif resposta_do_usuario == ('n'):
            print(f'Valor da conta é: {valor_da_conta:.2f}')
            break
    else:
            print('\n---Resposta errada, vamos recomeçar---\n')
