listaLivros = ["Livro 1", "Livro 2", "Livro 3", "Livro 4", "Livro 5"]

print("\n","Lista inicial".center(50,"-"))
print(listaLivros)

#Utilizando o método pop recebendo parâmetro 'vazio' para remover item
itemRemovido = listaLivros.pop()

print("\n","Lista método POP vazio".center(50,"-"))
print(listaLivros)
print("\nItem removido: {}".format(itemRemovido))

#Utilizando o método pop recebendo como parâmetro o índice 1 para remover item
itemRemovido = listaLivros.pop(1)

print("\n","Lista método POP índice 1".center(50,"-"))
print(listaLivros)
print("\nItem removido: {}".format(itemRemovido))

#Utilizando o método remove recebendo como parâmetro o item 'Livro 3'
listaLivros.remove("Livro 3")

print("\n","Lista método remove item 'Livro 3'".center(50,"-"))
print(listaLivros)
