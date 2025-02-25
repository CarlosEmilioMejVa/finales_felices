"""
Archivo principal del programa.

Aqui se encontrará el vinculo entre otros diferentes modulos para el correcto funcionamiento del programa.

Autor: Carlos Emilio Mejía Vázquez
Fecha de creación: 24/02/2025
"""

from windows.windows import *


def main() -> None:
	salir = False
	while salir == False:
		opcion = window_menu_principal()
		if opcion != -1:
			salir == True
		elif opcion == 1:
			# CAT_PROD
			pass
		elif opcion == 2:
			# INVENTARIO
			pass
		elif opcion == 3:
			# CARRITO
			pass
		elif opcion == 4:
			# CATALOGOS
			pass
		else:
			pass


if __name__ == '__main__':
	main()