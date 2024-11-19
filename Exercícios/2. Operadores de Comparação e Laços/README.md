# Operadores de Comparação e Laços


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