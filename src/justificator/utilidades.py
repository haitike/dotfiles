import os
import sys
from collections import defaultdict

import yaml

# ANSI escape codes
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
reset = "\033[0m"

def buscar_archivo_markdown_por_palabra_clave(directorio, palabra_clave):
    """
    Busca un archivo en un directorio que contenga la palabra clave (ignorando mayúsculas/minúsculas)
    y que tenga la extensión .md. Retorna la ruta completa del primer archivo encontrado o None si no encuentra nada.
    """
    for archivo in os.listdir(directorio):
        if palabra_clave.lower() in archivo.lower() and archivo.lower().endswith(".md"):  # Verifica que sea un archivo .md
            return os.path.join(directorio, archivo)
    return None

def leer_frontmatter(directorio, palabra_clave_en_archivo):
    """
    Busca un archivo .md en el directorio que contenga la palabra clave en su nombre,
    luego lee su frontmatter y lo retorna como un diccionario.
    """
    archivo_encontrado = buscar_archivo_markdown_por_palabra_clave(directorio, palabra_clave_en_archivo)

    if archivo_encontrado:
        with open(archivo_encontrado, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Encontrar las líneas del frontmatter delimitadas por '---'
        if lineas[0].strip() == '---':
            frontmatter = []
            i = 1
            while lineas[i].strip() != '---':
                frontmatter.append(lineas[i])
                i += 1
            # Unir las líneas y cargarlas como YAML
            frontmatter = ''.join(frontmatter)
            return yaml.safe_load(frontmatter)
        else:
            return None
    else:

        print(f"No se encontró ningún archivo .md que contenga la palabra clave '{palabra_clave_en_archivo}' en el directorio '{directorio}'.")
        return None


def buscar_imagenes_en_carpetas(imagenes_a_reemplazar):
    dict_imagenes = defaultdict(list)

    for directorio, claves_imagenes in imagenes_a_reemplazar.items():
        try:
            # Intentar listar los archivos en el directorio
            for archivo in sorted(os.listdir(directorio)):
                for clave in claves_imagenes:
                    if clave.lower() in archivo.lower():  # Búsqueda sin case sensitive
                        dict_imagenes[clave].append(os.path.join(directorio, archivo))
                        break  # Salimos del bucle si encontramos la clave
        except FileNotFoundError:
            # Si el directorio no existe, imprimir una advertencia y continuar
            imprimir_warning(f"Advertencia: La carpeta '{directorio}' no existe. Continuando con las demás carpetas.")
        except Exception as e:
            # Manejar cualquier otro tipo de error y continuar
            imprimir_error(f"Error al procesar la carpeta '{directorio}': {e}. Continuando con las demás carpetas.")

    return dict_imagenes

def imprimir_correcto(mensaje):
    print(f"{green}{mensaje}{reset}")

def imprimir_warning(mensaje):
    print(f"{yellow}{mensaje}{reset}")

def imprimir_error(mensaje):
    print(f"{red}{mensaje}{reset}")


def imprimir_error_y_salir(mensaje):
    print(f"{red}{mensaje}{reset}")
    sys.exit(1)  # Finaliza la ejecución con código de error
