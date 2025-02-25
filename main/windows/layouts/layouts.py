"""
Archivo de estructuras.

Aqui se encontraran las estructuras (layouts) del programa. Para situaciones relacionadas a las ventanas del programa, dirigirse al archivo windows/windows.py.

Autor: Carlos Emilio Mejía Vázquez
Fecha de creación: 24/02/2025
"""

import PySimpleGUI as sg

def layout_menu_principal()->list[..., list]:
	"""Layout para el menú principal del programa."""
	layout = [
			[sg.P(), sg.B("Catalogo de productos", k='-CAT_PROD-'), sg.P()],
			[sg.P(), sg.B("Inventario", k='-INVENTARIO-'), sg.P()],
			[sg.P(), sg.B("Carrito", k='-CARRITO-'), sg.P()],
			[sg.P(), sg.B("Catalogo", k='-CATALOGOS-'), sg.P()]
		]
	return layout