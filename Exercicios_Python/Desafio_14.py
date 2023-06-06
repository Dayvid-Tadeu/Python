# Escreva um programa que converta a temperatura CELSIUS para FAHRENHEIT.
print('='*40)

cel = float(input('Qual a temperatura em graus °C? '))
fa = 32 + (cel * 9/5)

print('='*40)

print('A Temperatura de {}°C é equivalente a {}°F'.format(cel, fa))