# Exercícios Python - Estrutura de Dados

### Exercício 1

Utilizando o built-in method input(), crie um programa que receba a altura e o peso de uma pessoa e imprima na tela o IMC da mesma.

```python
import time # Funcão para manipulação de tempo 

print("Bem vindo a calculadora de IMC.")
print("Por favor, informe sua altura:")
altura = float(input())
print("Por favor, informe seu peso:")
peso = float(input())

print("Calculando...")
print("=============")
time.sleep(1) # dar uma pausa de 1 s
print("Seu IMC é: {:.2f}".format(peso / altura ** 2))
```

### Exercício 2

Escreva um programa que pergunte o nome completo do usuário e cumprimente o mesmo pelo primeiro nome.

```python
print("Qual é seu nome completo?")
nome = input()
primeiro_nome = nome.split()[0]
print("\n")
print("Olá, {}!".format(primeiro_nome))
```

### Exercício 3

Escreva um código que extraia o domínio de um e-mail informado.

```python
print("Informe um e-mail")
email = input()
dominio = email.split("@")[-1]
print("\n")
print("O domínio do e-mail é: {}".format(dominio))
```

### Exercício 4 

Faça um programa para uma loja de tintas. A pessoa informa a área em m2 que deseja pintar, e o script calculará a quantidade de latas de tinta que a pessoa deve comprar e o valor. Considere que cada litro de tinta pinta 3m2, que cada lata contém 18L e que custa R$ 80.

```python
print("Bem vindo à loja de tintas.")
print("Informe a área que você deseja pintar em m2:")
area = float(input())

volume_necessario = area / 3
latas = int(volume_necessario / 18)
custo = latas * 80
print("Você precisará de {} latas e elas custarão {} reais.".format(latas, custo))
```

### Exercício 5

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao IR.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

```python
print("Calculadora de salário.")
print("Informe sua remuneração por horas:")
valor_por_hora = float(input())
print("Informe quantas horas trabalhou por mês.")
horas_trabalhadas = float(input())

salario = valor_por_hora * horas_trabalhadas
ir = salario * 0.11
inss = (salario - ir) * 0.08
sindicato = (salario - ir - inss) * 0.05

print("========================")
print("1. Salário bruto: R$ {:.2f}".format(salario))
print("2. Valor pago de IR: R$ {:.2f}".format(ir))
print("3. Valor pago de INSS: R$ {:.2f}".format(inss))
print("4. Valo pago ao sindicato: R$ {:.2f}".format(sindicato))
print("5. Salário líquido: R$ {:.2f}".format(salario - ir - inss - sindicato ))
```

#
#### Inteiros (`int`)

1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#### Números de Ponto Flutuante (`float`)

6. Escreva um programa que receba dois números flutuantes e realize sua adição.
7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#### Strings (`str`)

11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#### Booleanos (`bool`)

16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

### Exercícios Resolução

### Exercício 1: Soma de Dois Números Inteiros

```python
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 8  # Exemplo de entrada
num2 = 12  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)
```

### Exercício 2: Resto da Divisão por 5

```python
# num = int(input("Digite um número: "))
num = 18  # Exemplo de entrada
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)
```

### Exercício 3: Multiplicação de Dois Números

```python
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
num1 = 5  # Exemplo de entrada
num2 = 7  # Exemplo de entrada
resultado_multiplicacao = num1 * num2
print("O resultado da multiplicação é:", resultado_multiplicacao)
```

### Exercício 4: Divisão Inteira do Primeiro pelo Segundo Número

```python
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 20  # Exemplo de entrada
num2 = 3  # Exemplo de entrada
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é:", resultado_divisao_inteira)
```

### Exercício 5: Quadrado de um Número

```python
# num = int(input("Digite um número: "))
num = 6  # Exemplo de entrada
resultado_quadrado = num ** 2
print("O quadrado do número é:", resultado_quadrado)
```

### Exercício 6: Adição de Dois Números Flutuantes

```python
# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 2.5  # Exemplo de entrada
num2 = 4.5  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)
```

### Exercício 7: Média de Dois Números Flutuantes

```python
# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 3.5  # Exemplo de entrada
num2 = 7.5  # Exemplo de entrada
media = (num1 + num2) / 2
print("A média é:", media)
```

### Exercício 8: Potência de um Número

```python
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
base = 2.0  # Exemplo de entrada
expoente = 3.0  # Exemplo de entrada
potencia = base ** expoente
print("O resultado da potência é:", potencia)
```

### Exercício 9: Conversão de Celsius para Fahrenheit

```python
# celsius = float(input("Digite a temperatura em Celsius: "))
celsius = 30.0  # Exemplo de entrada
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")
```

### Exercício 10: Área de um Círculo

```python
# raio = float(input("Digite o raio do círculo: "))
raio = 5.0  # Exemplo de entrada
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)
```

### Exercício 11: Converter String para Maiúsculas

```python
# texto = input("Digite um texto: ")
texto = "Olá, mundo!"  # Exemplo de entrada
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)
```

### Exercício 12: Imprimir Nome Completo em Minúsculas

```python
# nome_completo = input("Digite seu nome completo: ")
nome_completo = "Fulano de Tal"  # Exemplo de entrada
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)
```

### Exercício 13: Remover Espaços em Branco de uma Frase

```python
# frase = input("Digite uma frase: ")
frase = "  Olá, mundo!  "  # Exemplo de entrada
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)
```

### Exercício 14: Separar Dia, Mês e Ano de uma Data

```python
# data = input("Digite uma data no formato dd/mm/aaaa: ")
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
```

### Exercício 15: Concatenar Duas Strings

```python
# parte1 = input("Digite a primeira parte do texto: ")
# parte2 = input("Digite a segunda parte do texto: ")
parte1 = "Olá,"  # Exemplo de entrada
parte2 = " mundo!"  # Exemplo de entrada
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)
```

#### Exercício 16. Operador `and` (E lógico)

```python
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
```

#### Exercício 17. Operador `or` (OU lógico)

```python
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)
```

#### Exercício  18. Operador `not` (NÃO lógico)

```python
# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)
```

#### Exercício 19. Operador `==` (Igualdade)

```python
# Exemplo de entrada
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)
```

#### Exercício 20. Operador `!=` (Diferença)

```python
# Exemplo de entrada
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)
```




