import sqlite3

conn = sqlite3.connect("livros.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo TEXT,
       autor TEXT,
       ano INTEGER
    )                                       
''')

# loop principal
while True:
    print("=== CADASTRO DE LIVROS ===")
    print("1 - cadastrar novo Livro")
    print("2 - listar Livros")
    print("3 - Sair")

    opcao = input("Escolha uma opção...")

    if opcao == "1":
        titulo = input("Titulo do livro:")
        autor = input("Autor:")
        ano = int(input("Ano de publicacao: "))
        
        cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        (titulo, autor, ano))
        
        conn.commit() # confirmar inserção de dados 
        print(f'Livro {titulo} criado com sucesso!')
    elif opcao == "2":
        print("Livros cadastrados")
        for linha in cursor.execute("SELECT * FROM livros"):
            print(f'ID: {linha[0]}) | titulo {linha[1]} | autor {linha[2]} | Ano {linha[3]}')

    elif opcao == "3":
        print("Encerdando o programa..")
        break
        
    else:
        print("Opcao invalida, tente novamente...")