#O começo e o final da lista equivalem ao começo e ao final da fila respectivamente
fila = ["Usuário 1", "Usuário 2", "Usuário 3", "Usuário 4"]  

print("\nOBS: O começo e o final da lista equivalem ao começo e ao final da fila respectivamente\n")

print("Fila inicial".center(50,"-"))
print(fila)


#Adicionando usuários ao final da fila
fila.append("Usuário 5")
fila.append("Usuário 6")
fila.append("Usuário 7")
fila.append("Usuário 8")

print("\n","Fila após enqueue de 4 usuários".center(50,"-"))
print(fila)

#Removendo usuários do começo da fila
fila.pop(0)
fila.pop(0)
fila.pop(0)
fila.pop(0)
fila.pop(0)

print("\n","Fila após dequeue de 5 usuários".center(50,"-"))
print(fila)
