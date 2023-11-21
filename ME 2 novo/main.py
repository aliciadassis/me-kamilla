import pandas as pd

def ler_dataframe(nome_arquivo, colunas):
    try:
        return pd.read_csv(nome_arquivo)
    except FileNotFoundError:
        return pd.DataFrame(columns=colunas)

def escrever_dataframe(nome_arquivo, dataframe):
    dataframe.to_csv(nome_arquivo, index=False)

def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    cpf = input('Digite o CPF do funcionário: ')
    data_nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')

    return {'Nome': nome, 'CPF': cpf, 'Data de Nascimento': data_nascimento}

def cadastrar_veiculo():
    placa = input("Digite a placa do veículo: ")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")

    return {'Placa': placa, 'Marca': marca, 'Modelo': modelo, 'Ano': ano}

def registrar_lavagem(funcionarios_df, veiculos_df, lavagens_df):
    placa = input("Digite a placa do veículo: ")
    cpf = input('Digite o CPF do funcionário: ')
    data_lavagem = input('Digite a data da lavagem (DD/MM/AAAA): ')
    hora_lavagem = input('Digite a hora da lavagem (HH:MM): ')
    tipo_lavagem = input('Tipo da lavagem (simples ou completa): ').lower()

    while tipo_lavagem not in ['simples', 'completa']:
        tipo_lavagem = input('Escolha uma opção de lavagem válida: (simples ou completa) ')

    valor = 50.00 if tipo_lavagem == 'simples' else 100.00

    nova_lavagem = {'Placa do Veículo': placa, 'CPF do Funcionário': cpf, 'Data da Lavagem': data_lavagem,
                    'Hora da Lavagem': hora_lavagem, 'Tipo de Lavagem': tipo_lavagem, 'Valor Cobrado': valor}

    lavagens_df = pd.concat([lavagens_df, pd.DataFrame([nova_lavagem])], ignore_index=True)

    return lavagens_df

def relatorio_lavagens(lavagens_df, veiculos_df, funcionarios_df):
    relatorio_df = lavagens_df.merge(veiculos_df, left_on='Placa do Veículo', right_on='Placa')
    relatorio_df = relatorio_df.merge(funcionarios_df, left_on='CPF do Funcionário', right_on='CPF')

    relatorio_df = relatorio_df[['Data da Lavagem', 'Hora da Lavagem', 'Placa', 'Modelo', 'Nome', 'Tipo de Lavagem', 'Valor Cobrado']]

    print("\nRelatório de Lavagens:")
    print(relatorio_df)

def main():
    funcionarios_df = ler_dataframe('funcionarios.csv', ['Nome', 'CPF', 'Data de Nascimento'])
    veiculos_df = ler_dataframe('veiculos.csv', ['Placa', 'Marca', 'Modelo', 'Ano'])
    lavagens_df = ler_dataframe('lavagens.csv', ['Placa do Veículo', 'CPF do Funcionário', 'Data da Lavagem', 'Hora da Lavagem', 'Tipo de Lavagem', 'Valor Cobrado'])

    while True:
        print("\nMenu:")
        print("1. Cadastrar Funcionário")
        print("2. Cadastrar Veículo")
        print("3. Registrar Lavagem")
        print("4. Relatório de Lavagens")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcionarios_df = pd.concat([funcionarios_df, pd.DataFrame([cadastrar_funcionario()])], ignore_index=True)
        elif opcao == '2':
            veiculos_df = pd.concat([veiculos_df, pd.DataFrame([cadastrar_veiculo()])], ignore_index=True)
        elif opcao == '3':
            lavagens_df = registrar_lavagem(funcionarios_df, veiculos_df, lavagens_df)
        elif opcao == '4':
            relatorio_lavagens(lavagens_df, veiculos_df, funcionarios_df)
        elif opcao == '0':
            escrever_dataframe('funcionarios.csv', funcionarios_df)
            escrever_dataframe('veiculos.csv', veiculos_df)
            escrever_dataframe('lavagens.csv', lavagens_df)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
