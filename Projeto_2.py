import json
import csv
from functools import reduce

def salvar_json(lista):
    with open("vinhos.json", "w") as arquivo:
        json.dump(lista, arquivo)

def carregar_json():
    with open("vinhos.json", "r") as arquivo:
        return json.load(arquivo)

def adicionar_vinho():
    try:
        lista_json = carregar_json()
        lista_python = json.loads(lista_json)

        nome = input("Digite o nome do vinho: ")
        origem = input("Digite a origem do vinho: ")
        tipo = input("Digite o tipo do vinho: ")
        safra = int(input("Digite a safra do vinho: "))
        preco = float(input("Digite o preço do vinho: "))

        novo_vinho = {"nome": nome, "origem": origem, "tipo": tipo, "safra": safra, "preco": preco}
        lista_python.append(novo_vinho)

        lista_json = json.dumps(lista_python)
        salvar_json(lista_json)

        print("Vinho adicionado com sucesso!")
    except ValueError:
        print("Erro: Entrada inválida para a safra ou preço do vinho.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def listar_vinhos():
    try:
        lista_json = carregar_json()
        lista_python = json.loads(lista_json)

        for vinho in lista_python:
            print("Nome:", vinho["nome"])
            print("Origem:", vinho["origem"])
            print("Tipo:", vinho["tipo"])
            print("Safra:", vinho["safra"])
            print("Preço:", vinho["preco"])
            print("------------------------")
          
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def ler_vinho():
    try:
        lista_json = carregar_json()
        lista_python = json.loads(lista_json)

        nome = input("Digite o nome do vinho que você quer ler: ")
        for vinho in lista_python:
            if vinho["nome"] == nome:
                print()
                print("-----------------------")
                print("Nome:", vinho["nome"])
                print("Origem:", vinho["origem"])
                print("Tipo:", vinho["tipo"])
                print("Safra:", vinho["safra"])
                print("-----------------------")
                print()
                break
        else:
            print("Vinho não encontrado!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def dados_estatisticos_precos():
    try:
        lista_json = carregar_json()
        lista_python = json.loads(lista_json)

        precos = list(map(lambda vinho: vinho["preco"], lista_python))

        media_precos = sum(precos) / len(precos)
        mediana_precos = sorted(precos)[len(precos) // 2] if len(precos) % 2 != 0 else (sorted(precos)[len(precos) // 2 - 1] + sorted(precos)[len(precos) // 2]) / 2
        moda_precos = list(filter(lambda x: precos.count(x) == max(map(lambda x: precos.count(x), precos)), set(precos)))
        desvio_padrao_precos = (reduce(lambda x, y: x + y, map(lambda x: (x - media_precos) ** 2, precos)) / len(precos)) ** 0.5

        print("Dados estatísticos dos preços dos vinhos:")
        print(f"Média: {media_precos}")
        print(f"Mediana: {mediana_precos}")
        print(f"Moda: {', '.join(map(str, moda_precos))}")
        print(f"Desvio padrão: {desvio_padrao_precos}")

        with open('dados_estatisticos_precos.csv', mode='w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Estatísticas', 'Valor'])
            writer.writerow(['Média', media_precos])
            writer.writerow(['Mediana', mediana_precos])
            writer.writerow(['Moda', ', '.join(map(str, moda_precos))])
            writer.writerow(['Desvio Padrão', desvio_padrao_precos])

        print("Dados estatísticos salvos em 'dados_estatisticos_precos.csv'!")

    except Exception as e:
        print(f"Ocorreu um erro ao calcular ou salvar os dados estatísticos: {e}")

def atualizar_vinho():
    try:
        lista_json = carregar_json()
        lista_python = json.loads(lista_json)

        nome = input("Digite o nome do vinho que você quer atualizar: ")
        for vinho in lista_python:
            if vinho["nome"] == nome:
                origem = input("Digite a nova origem do vinho: ")
                tipo = input("Digite o novo tipo do vinho: ")
                safra = int(input("Digite a nova safra do vinho: "))
                preco = float(input("Digite o novo preço do vinho: "))

                vinho["origem"] = origem
                vinho["tipo"] = tipo
                vinho["safra"] = safra
                vinho["preco"] = preco

                lista_json = json.dumps(lista_python)
                salvar_json(lista_json)

                print("Vinho atualizado com sucesso!")
                break
        else:
            print("Vinho não encontrado!")
    except ValueError:
        print("Erro: Entrada inválida para a safra do vinho.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def deletar_vinho():
    try:
        lista_json = carregar_json()
        lista_python = json.loads(lista_json)

        nome = input("Digite o nome do vinho que você quer deletar: ")
        for vinho in lista_python:
            if vinho["nome"] == nome:
                lista_python.remove(vinho)
                lista_json = json.dumps(lista_python)
                salvar_json(lista_json)

                print("Vinho deletado com sucesso!")
                break
        else:
            print("Vinho não encontrado!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")  

def mostrar_menu():
    print("Escolha uma opção:")
    print("1 - Adicionar um novo vinho")
    print("2 - Listar todos os vinhos")
    print("3 - Ler um vinho específico")
    print("4 - Atualizar um vinho")
    print("5 - Deletar um vinho")
    print("6 - Mostrar Dados Estatísticos do preços")
    print("7 - Sair do programa")

continuar = True

while continuar:
    mostrar_menu()
    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionar_vinho()
        elif opcao == 2:
            listar_vinhos()
        elif opcao == 3:
            ler_vinho()
        elif opcao == 4:
            atualizar_vinho()
        elif opcao == 5:
            deletar_vinho()
        elif opcao == 6:
            dados_estatisticos_precos()
        elif opcao == 7:
            continuar = False
            print("Obrigado por usar o programa!")
        else:
            print("Opção inválida!")
    except ValueError:
        print("Erro: Insira um número correspondente à opção desejada.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
