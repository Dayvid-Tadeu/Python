# Digite algo no teclado e mostre e mostre as informações dele.
a = input('Digite algo ')
print('O Tipo primitivo desse valor é ',type(a))
print('Só tem espaços? ',a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Está em Maiusculas',a.isupper())
print('Esta em Minusculas? ',a.islower())
print('Está Capitalizada? ',a.istitle()) #Tem letra com tamanhos diferentes
