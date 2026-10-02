import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect("database/inventario.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prendas (
    id_prenda INTEGER PRIMARY KEY,
    nombre TEXT,
    categoria TEXT,
    talla TEXT,
    color TEXT,
    material_principal TEXT,
    costo_produccion REAL,
    precio_venta REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventario (
    id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
    id_prenda INTEGER,
    cantidad_disponible INTEGER,
    ubicacion_almacen TEXT,
    FOREIGN KEY (id_prenda) REFERENCES prendas (id_prenda)
)
""")

df_prendas = pd.read_csv("data/prendas.csv")
df_prendas.to_sql("prendas", conn, if_exists="replace", index=False)

np.random.seed(1)
almacenes = ["Almacen Central", "Tienda Norte", "Tienda Sur"]
inventario_data = []
for id_prenda in df_prendas["id_prenda"]:
    inventario_data.append({
        "id_prenda": id_prenda,
        "cantidad_disponible": np.random.randint(0, 50),
        "ubicacion_almacen": np.random.choice(almacenes)
    })

df_inventario = pd.DataFrame(inventario_data)
df_inventario.to_sql("inventario", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Base de datos creada correctamente con prendas e inventario")