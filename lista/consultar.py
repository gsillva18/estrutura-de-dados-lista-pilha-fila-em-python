listaCompras = ["cuscuz", "carne", "café", "batata", "melancia"]

print("\n","Lista inicial".center(50,"-"))
print(listaCompras)

#Consultando item da lista com indice 2

item = listaCompras[2]
print("\nItem do índice 2: {} ".format(item))

#Consultando indice da lista com valor "batata"

indice = listaCompras.index("batata")
print("\nÍndice do item 'batata': {} \n".format(indice))

#Consultando todos os itens da lista e seus respectivos índices
for indice, item in enumerate(listaCompras):
    print("\nÍndice: {} | Item: {}".format(indice, item))
