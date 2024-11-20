# Estruturas de Controle de Fluxo

### Exercício 1: Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.
```python
quantidade = 10  # Exemplo de valor, substitua com input do usuário se necessário
preço = 20  # Exemplo de valor, substitua com input do usuário se necessário

if quantidade > 0 and preço > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")
```

### Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
* Temperatura < 18°C é 'Baixa'
* Temperatura >= 18°C e <= 26°C é 'Normal'
* Temperatura > 26°C é 'Alta'
```python
temperatura = float(input())

if temperatura < 18:
    print("Baixa")
elif 18 <= temperatura <= 26:
    print("Normal")
else:
    print("Alta")
```

### Exercício 3: Filtragem de Logs por Severidade
Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
```python
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
```

### Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
```python
idade = 25  # Exemplo de valor, substitua com input do usuário se necessário
email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email:
    print("Email inválido")
else:
    print("Dados de usuário válidos")
```

### Exercício 5: Detecção de Anomalias em Dados de Transações
Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.
```python
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")
```

## Exercícios com FOR

### 6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

```python
texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)
```
### 7. Normalização de Dados
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
```python
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)
```
### 8. Filtragem de Dados Faltantes
Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
```python
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)
```
### 9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
```python
numeros = range(1, 11)
pares = [x for x in numeros if x % 2 == 0]

print(pares)
```

### 10. Agregação de Dados por Categoria
Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
```python
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)
```

## Exercícios com WHILE

### 11. Leitura de Dados até Flag
Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
```python
dados = []
entrada = ""
while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
```
### 12. Validação de Entrada
Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
```python
numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")
```

### 13. Consumo de API Simulado
Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
```python
pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")
```

### 14. Tentativas de Conexão
Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
```python
tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if True:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")
```

### 15. Processamento de Dados com Condição de Parada
Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.
```python
itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1
```
# Desafio 

 Integre no desafio anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas.

```python
# Inicializa as variáveis para o controle do loop
nome_valido = False
salario_valido = False
bonus_valido = False

# Loop para verificar o nome
while not nome_valido: # (while nome_valido is not True:)0
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Loop para verificar o salário
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Loop para verificar o bônus
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de cálculo de bônus

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
```


## Extras

### Exercício 1

Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
A mensagem "Reprovado", se a média for menor do que 7;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

```python
print("Informe a primeira nota do aluno:")
n1 = float(input())
print("Informe a primeira nota do aluno:")
n2 = float(input())
media = (n1 + n2) / 2

print("========================")
print("A média das notas é: {}".format(media))

if media == 10:
    print("Aprovado com distinção!")
elif media >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")
```
### Exercício 2
Escreva um script que leia três números e mostre o maior e o menor deles.
```python
list_nums = []
for i in range(3):
    print("Informe o {}º número:".format(i+1))
    list_nums.append(int(input()))
    
list_nums.sort()
print("========================")
print("Maior número: {}".format(list_nums[-1]))
print("Menor número: {}".format(list_nums[0]))
```

### Exercício 3
Nome na vertical em escada.
```python
print("Informe o nome:")
nome = input()
print("========================")
for i in range(len(nome) + 1):
    print(nome[:i])
```

### Exercício 4
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro, é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).
```python
print("Qual o tamanho da sequência de Fibonancci você deseja ver?")
n = int(input())

v0 = 0
v1 = 1
v = 1
print("========================")
print(1)
for i in range(n):
    print(v)
    v0 = v1
    v1 = v
    v = v1 + v0
```

### Exercício 5
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
```python
print("Informe o nome:")
nome = input()
while len(nome) <= 3:
    print("O nome deve conter mais de 3 caracteres")
    nome = input()

print("Insira a sua idade")
idade = int(input())
while idade < 0 or idade > 150:
    print("Insira um valor entre 0 e 150")
    idade = int(input())

print("Insira seu salário")
salario = int(input())
while salario <= 0:
    print("Insira um valor maior do que zero")
    salario = int(input())

print("Insira o sexo")
sexo = input()
while sexo not in ['m','n']:
    print("Insira um m para masculino ou f para feminino")
    sexo = input()

print("Insira seu estado civil")
estado_civil = input()
while estado_civil not in ['s','c','v','d']:
    print("Insira um valor valido")
    estado_civil = input()

```

### Exercício 6
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.
```python
print("Informe um número")
n = int(input())

check = 0

for i in range(2, n):
    if n % i == 0:
        check = 1
        break

print("========================")
if check == 0:
    print("É primo!")
else:
    print("Não é primo!")
```

