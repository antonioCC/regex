import re
#patron = re.compile('a[3-5]+')# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#print( input("Introduce un texto") );
cadena = input("ingresa el texto")
print("el texto es: "+cadena)

print("ingresa un una opcion")
print("1: palabras de 7 letras o mas")
print("2: que no terminen en vocal")
print("3 que empiecen con M y la segunda no sea vocal")
print("4 que este entre comillas")
print("5 que sean ips")
print("6 que sean horas")
print("7 que sean telefonos")
print("8 que sean correos")
print("9 que sean urls")
print("10 que sean codigos postales")
numero = int(input())

if numero==1:
	#palabras de 7 letras o mas
	patron = re.compile('[a-z]{7,}')
	print (patron.findall(cadena))


if numero==2:
	#que no terminen en vocal
	patron = re.compile('[a-zA-Z0-9]+[^aeiou]\s')
	print (patron.findall(cadena))

if numero==3:
	#que empiecen con M y la segunda no sea vocal
	patron = re.compile('M[^aeiou]+')
	print (patron.findall(cadena))

if numero==4:
	#que este entre comillas
	patron = re.compile('\".+\"')
	print (patron.findall(cadena))

if numero==5:
	#que sean ips
	patron = re.compile('\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}')
	print (patron.findall(cadena))

if numero==6:
	#que sean horas
	patron = re.compile('[0-12]{0,2}\:[0-59]{0,2}\:[0-59]{0,2}')
	print (patron.findall(cadena))

if numero==7:
	#que sean telefonos
	patron = re.compile('\d\d\d\d\d\d\d\d\d')
	print (patron.findall(cadena))

if numero==8:
	#que sean correos
	patron = re.compile('[a-zA-Z]+([@gmail.com]|[@hotmail.com]|[@yahoo.com])')
	print (patron.findall(cadena))

if numero==9:
	#que sean urls
	patron = re.compile('https?:\/\/[\w\-]+\.[\w\-]+[#?]?')
	print (patron.findall(cadena))

if numero==10:
	#que sean codigo postal
	patron = re.compile('^(/d{5}$)')
	print (patron.findall(cadena))