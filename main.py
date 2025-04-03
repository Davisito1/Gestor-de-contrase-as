import random as r, string as s

chars = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation
password = ""
lenght = int(input("Introduce la longitud de la contraseña: "))

for i in range(lenght):
    password += r.choice(chars)

print(f"Tu contraseña ha sido generada: {password}")