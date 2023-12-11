#O final da lista equivale ao topo da pilha
pilhaUrlAcesso = ["URL 1", "URL 2", "URL 3", "URL 4", "URL 5"] 

print("\nOBS: O final da lista equivale ao topo da pilha\n")

print("Pilha inicial".center(50,"-"))
print(pilhaUrlAcesso)

#Adicionando itens ao topo da pilha
pilhaUrlAcesso.append("URL 6")
pilhaUrlAcesso.append("URL 7")
pilhaUrlAcesso.append("URL 8")
pilhaUrlAcesso.append("URL 9")

print("\n","Pilha após push de 4 itens".center(50,"-"))
print(pilhaUrlAcesso)


#Removendo itens do topo da pilha
pilhaUrlAcesso.pop()
pilhaUrlAcesso.pop()
pilhaUrlAcesso.pop()
pilhaUrlAcesso.pop()
pilhaUrlAcesso.pop()

print("\n","Pilha após pop de 5 itens".center(50,"-"))
print(pilhaUrlAcesso)

