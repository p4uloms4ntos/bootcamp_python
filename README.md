# Exercícios Python 

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



