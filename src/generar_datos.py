import pandas as pd
import numpy as np

np.random.seed(42)

categorias = ["Vestido", "Chaqueta", "Falda", "Pantalon", "Blusa", "Abrigo"]
colores = ["Negro", "Blanco", "Beige", "Rojo", "Azul marino", "Verde olivo"]
materiales_lista = ["Seda", "Algodon", "Lino", "Encaje", "Lana", "Cuero sintetico"]

n_prendas = 40

nombres_base = ["Aurora", "Eclipse", "Nova", "Luna", "Zafiro", "Ambar", "Ceniza", "Bruma"]

prendas = []
for i in range(1, n_prendas + 1):
    categoria = np.random.choice(categorias)
    nombre = f"{categoria} {np.random.choice(nombres_base)}"
    costo_produccion = round(np.random.uniform(15, 120), 2)
    margen = np.random.uniform(1.8, 3.2)
    precio_venta = round(costo_produccion * margen, 2)
    prendas.append({
        "id_prenda": i,
        "nombre": nombre,
        "categoria": categoria,
        "talla": np.random.choice(["XS", "S", "M", "L", "XL"]),
        "color": np.random.choice(colores),
        "material_principal": np.random.choice(materiales_lista),
        "costo_produccion": costo_produccion,
        "precio_venta": precio_venta,
    })

df_prendas = pd.DataFrame(prendas)
df_prendas.to_csv("data/prendas.csv", index=False)
print("Datos generados correctamente")
print(df_prendas.head())