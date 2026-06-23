#%%
txt = "Meu nome arquivo!"

nome_arquivo = "historia_2.txt"



with open(nome_arquivo, mode='w') as open_file:
    open_file.write(txt)

# %%
