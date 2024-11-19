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





