CREATE TABLE IF NOT EXISTS producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    categoria TEXT,
    precio REAL,
    stock INTEGER
);

CREATE TABLE IF NOT EXISTS proveedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT
);

CREATE TABLE IF NOT EXISTS movimiento_stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER,
    tipo TEXT,
    cantidad INTEGER,
    -- CREATE A DATETIME FIELD USINT THE CURRENT DATE AND TIME IN SQLITE FORMAT IN AN STRING
    fecha TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (producto_id) REFERENCES producto (id)
);


CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);
