import sqlte3

conn = slite3.connect('alunos.db')
cursor = conn.cursor()

#Crie uma tabela se não existir
cursor.execute('''
  CREATE TABLE IF NOT EXISTS Alunos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,   
      nome TXT,
      nota REAL       
)

''')

# inserir dados 
cursor.execute("INSERT INTO ALUNOS (nome, nota) VALUES (?, ?)", ('Aneli', 8.0)):
conn.commit() #executar 

# consultar dados
for row in cursor.execute("SELECT * FROM alunos"):
    print(row)

conn.close()