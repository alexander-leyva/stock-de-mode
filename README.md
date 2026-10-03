# Stock de Mode

Sistema de inventario para marcas de moda, enfocado en el control de piezas, materiales, costos de produccion y stock disponible. Pensado para marcas que trabajan con piezas unicas o de produccion limitada, donde cada prenda tiene su propio desglose de materiales y costos.

## Problema que resuelve

Muchas marcas de moda independientes no cuentan con una herramienta sencilla para llevar el control de cuantas piezas tienen en stock, cual es el costo real de produccion de cada una, y cuales estan por agotarse. Este proyecto propone una solucion ligera, visual y facil de usar para ese problema.

## Funcionalidades

- Visualizacion de metricas generales: piezas distintas, unidades totales en stock, y valor total del inventario.
- Filtro de piezas por categoria (vestidos, chaquetas, faldas, etc).
- Tabla de piezas con bajo stock para identificar reabastecimiento urgente.
- Carga de logo de marca personalizado, que se aplica como marca de agua en la interfaz.
- Diseno minimalista pensado para una experiencia de marca premium.

## Tecnologias utilizadas

- Python para la generacion y procesamiento de datos.
- SQLite para el almacenamiento estructurado de prendas e inventario.
- Pandas para la manipulacion de datos.
- Streamlit para la interfaz web interactiva.

## Estructura del proyecto

inventario-moda/
    data/               Datos generados en formato csv
    database/           Base de datos SQLite
    src/                Scripts de generacion de datos y creacion de base de datos
    app/                Aplicacion Streamlit
    .streamlit/         Configuracion de tema visual

## Como ejecutarlo

1. Crear y activar un entorno virtual de Python.
2. Instalar dependencias: pip install pandas streamlit
3. Generar los datos: python src/generar_datos.py
4. Crear la base de datos: python src/crear_base_datos.py
5. Ejecutar la aplicacion: streamlit run app/streamlit_app.py

## Autor

Desarrollado por Alexander Leyva. Proyecto desarrollado como parte de portafolio en Ciencia de Datos, combinando experiencia previa en diseno de modas con analisis y visualizacion de datos.