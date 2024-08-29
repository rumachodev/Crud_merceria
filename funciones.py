import requests
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

# Funciones para manejar la interfaz
def agregar_producto():
    nombre = tk.simpledialog.askstring("Nombre del Producto", "Ingrese el nombre del producto:")
    precio = tk.simpledialog.askfloat("Precio", "Ingrese el precio del producto:")
    if nombre and precio is not None:
        guardar_en_notion(nombre, precio)
        tk.messagebox.showinfo("Éxito", "Producto guardado en Notion")

def consultar_productos():
    productos = obtener_productos()
    # Lógica para mostrar productos y buscar
    if productos:
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")  # Cambiado a print para consola
    else:
        tk.messagebox.showwarning("Advertencia", "No hay productos disponibles.")
    
    # Búsqueda de productos
    busqueda = tk.simpledialog.askstring("Buscar producto", "Ingrese el nombre del producto a buscar:")
    if busqueda:
        productos_filtrados = [p for p in productos if busqueda.lower() in p['nombre'].lower()]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")  # Cambiado a print para consola
        else:
            tk.messagebox.showwarning("Advertencia", "No se encontraron productos que coincidan con la búsqueda.")

def obtener_productos():
    # Lógica para obtener productos de Notion
    ...

def guardar_en_notion(nombre, precio):
    # Lógica para guardar en Notion
    ...

def modificar_producto(id_producto, nuevo_nombre, nuevo_precio):
    # Lógica para modificar un producto en Notion
    ...

def eliminar_producto(id_producto):
    # Lógica para eliminar un producto en Notion
    ...

def registrar_venta(productos):
    # Lógica para registrar una venta en Notion
    ...




