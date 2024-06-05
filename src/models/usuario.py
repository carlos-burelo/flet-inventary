"""
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

"""

class Usuario:
    def __init__(self, id: int, nombre: str, email: str, password: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.email} - {self.password}"
