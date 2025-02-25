"""
Archivo de ventanas.

Aqui se encontraran la logica de las ventanas (windows) del programa. Para situaciones relacionadas a las estructuras de las ventanas del programa, dirigirse al archivo windows/layouts/layouts.py.

Autor: Carlos Emilio Mejía Vázquez
Fecha de creación: 24/02/2025
"""

from windows.layouts.layouts import *


def window_menu_principal()->int:
	window = sg.Window(
		title = "Finales Felices • Menú principal",
		layout = layout_menu_principal()
	)
	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			return -1
		if event == "-CAT_PROD-":
			return 1
		if event == "-INVENTARIO-":
			return 2
		if event == "-CARRITO-":
			return 3
		if event == "-CATALOGOS-":
			return 4
