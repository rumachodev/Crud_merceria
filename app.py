import streamlit as st
from funciones import *
from ventas import Carrito

# Configuración de la página
st.set_page_config(page_title="Mercería by Silvia", layout="wide")

def modificar_producto_ui():
    # Lógica para modificar productos
    ...

def eliminar_producto_ui():
    # Lógica para eliminar productos
    ...

def registrar_venta_ui():
    carrito = Carrito()


def crear_menu():
    ventana = tk.Tk()
    ventana.title("Mercería by Silvia")
    
    # Crear botones para el menú
    btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
    btn_agregar.pack(pady=10)

    btn_consultar = tk.Button(ventana, text="Consultar Productos", command=consultar_productos)
    btn_consultar.pack(pady=10)

    btn_modificar = tk.Button(ventana, text="Modificar Producto", command=modificar_producto_ui)
    btn_modificar.pack(pady=10)

    btn_eliminar = tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto_ui)
    btn_eliminar.pack(pady=10)

    btn_registrar = tk.Button(ventana, text="Registrar Venta", command=registrar_venta_ui)
    btn_registrar.pack(pady=10)

    ventana.mainloop()

# Menú de navegación
opcion = st.sidebar.selectbox("Selecciona una opción", ["Agregar Producto", "Consultar Productos", "Modificar Producto", "Eliminar Producto", "Registrar Venta"])

if opcion == "Agregar Producto":
    agregar_producto()
elif opcion == "Consultar Productos":
    consultar_productos()
elif opcion == "Modificar Producto":
    modificar_producto_ui()
elif opcion == "Eliminar Producto":
    eliminar_producto_ui()
elif opcion == "Registrar Venta":
    registrar_venta_ui()

# Iniciar el bucle principal
crear_menu()