#%%
# nome_arquivo = "minha_historia.txt"

#usando with ele fecha automaticamente sem a necessidade do .close()
#essas duas linhas, resumem as duas abaixo de forma mais eficaz 

with open(nome_arquivo) as open_file :
    conteudo  = open_file.read()
#ao sair do escopo o arquivo fecha sozinho, o print deve estar fora da identação
print(conteudo)


#abre o arquivo
open_file = open(nome_arquivo)

#processa o arquivo
conteudo = open_file.read()
print(conteudo)

#fecha o arquivo 
open_file.close()

#%%