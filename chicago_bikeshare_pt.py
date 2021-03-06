# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

print("\n")

for i in range(20):
	print("Amostra " + str(i+1) + ": ")
	print(data_list[i+1])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

print("\n")

for i in range(20):
	print("Gênero da Amostra " + str(i+1) + ": ")
	print(data_list[i][-2])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data, index):
	# def column_to_list(data: list, index: int) -> list:
	"""
	Função para obter uma coluna de uma lista obtida a partir de um csv.
	Argumentos:
	  data: A lista obtida a partir de um arquivo csv.
	  index: O índice da coluna desejada.
	Retorna:
	  Uma lista contendo os valores da coluna selecionada.

	"""
	column_list = []
	# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
	for i in range(len(data)):
		column_list.append(data[i][index])
	
	return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print("\n")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for i in range(len(data_list)):
	gender = data_list[i][-2];

	if(gender == 'Male'):
		male += 1;
	elif(gender == 'Female'):
		female += 1;

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
	# def count_gender(data_list: list) -> list:
	"""
	Função para obter a contagem de gêneros do arquivo chicago.csv
	Argumentos:
	  data_list: A lista de dados obtida a partir do arquivo chicago.csv.
	Retorna:
	  Uma lista [count_male, count_female] contendo as contagens de "Male" e "Female" no arquivo.

	"""
	male = 0
	female = 0
	
	for i in range(len(data_list)):
		gender = data_list[i][-2];

		if(gender == 'Male'):
			male += 1;
		elif(gender == 'Female'):
			female += 1;
	
	return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
	# def most_popular_gender(data_list: list) -> str:
	"""
	Função para obter o gênero mais popular do arquivo chicago.csv.
	Argumentos:
	  data_list: A lista de dados obtida a partir de chicago.csv.
	Retorna:
	  Uma string sinalizando o gênero mais popular.

	"""
	[count_male, count_female] = count_gender(data_list);

	if(count_male > count_female):
		return "Masculino"
	elif(count_male < count_female):
		return "Feminino"
	else:
		return "Igual"

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Genero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Genero')
plt.show(block=True)

# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_types(data_list):
	# def count_user_types(data_list: list) -> list:
	"""
	Função para obter a contagem de tipos de usuário do arquivo chicago.csv
	Argumentos:
	  data_list: A lista de dados obtida a partir do arquivo chicago.csv.
	Retorna:
	  Uma lista [count_customer, count_subscriber, count_dependent] contendo as contagens.


	"""
	customer = 0
	subscriber = 0
	dependent = 0
	
	for i in range(len(data_list)):
		user_type = data_list[i][-3];

		if(user_type == 'Customer'):
			customer += 1;
		elif(user_type == 'Subscriber'):
			subscriber += 1;
		elif(user_type == 'Dependent'):
			dependent += 1;
	
	return [customer, subscriber, dependent]

user_types_list = column_to_list(data_list, -3)
#para verificar os valores possíveis de user_types
print(set(user_types_list))

types = ["Customer", "Subscriber", "Dependent"]
quantity = count_user_types(data_list)
print(quantity)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuario')
plt.show(block=True)

# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque há linhas em que o campo correspondente a gênero está vazio."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# converter para float
trip_duration_list = [float(i) for i in trip_duration_list]

for i in range(len(trip_duration_list)):
	d = trip_duration_list[i]
	if(d is None):
		print("!!!")

	if(i == 0 or d < min_trip):
		min_trip = d
	
	if(i == 0 or d > max_trip):
		max_trip = d
	
	mean_trip += d

mean_trip /= len(trip_duration_list)

# checar se posso usar sort...
trip_duration_list.sort()
median_trip = trip_duration_list[int(len(trip_duration_list)//2)]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3)) # não deveria ser user_types, mas start_stations...

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
  param1: O primeiro parâmetro.
  param2: O segundo parâmetro.
Retorna:
  Uma lista de valores x.

"""

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
