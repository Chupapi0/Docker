import web
import sqlite3

urls = (
    '/', 'Index',
    '/insertar', 'Insertar'
)

app = web.application(urls, globals())
render = web.template.render('.')

def get_db():
    conn = sqlite3.connect("agenda.db")
    conn.row_factory = sqlite3.Row
    return conn

# Crear tabla si no existe
conn = get_db()
conn.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
conn.commit()
conn.close()

class Index:
    def GET(self):
        conn = get_db()
        cursor = conn.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        return render.index(usuarios)

class Insertar:
    def GET(self):
        return render.insertar()

    def POST(self):
        data = web.input()
        nombre = data.get('nombre')
        email = data.get('email')
        conn = get_db()
        conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        conn.close()
        print("Redirigiendo...")
        raise web.seeother('/')

if __name__ == "__main__":
    app.run()