# Exercises from unit 6.6 

# Exercise 1

name_user = input("Digite su nombre de usuario: ")
amount = len(name_user)

if not name_user.isalnum():
    print ("El nombre de usuario puede contener solo letras y números.")
    
if amount < 6:
    print ("El nombre de usuario debe contener al menos 6 caracteres.")
elif amount > 12:
    print ("El nombre de usuario no puede contener más de 12 caracteres.")

# Exercise 2 

password = input("Digite su contraseña: ")
amount = len(password)
    
if amount < 8:
    print ("El nombre de usuario debe contener al menos 8 caracteres.")

number = False 
space = False 
lower = False
upper = False 
alpha = False 
not_alpha = False

keywords = list(password)
for k in keywords:
    if k.isspace():
        print ("La contraseña no puede tener espacios en blanco.")
        break
    if not k.isalnum():
        not_alpha = True
    if k.isdigit():
        number = True 
    if k.isupper():
        upper = True 
    if k.islower():
        lower = True
    if k.isalpha():
        alpha = True

if number and upper and lower and alpha and not_alpha:
    print ("Tu contraseña se ha registrado correctamente.")
else: 
    print ("Tu contraseña es invalida recuerda que debe tener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico. ")
    
        
    
