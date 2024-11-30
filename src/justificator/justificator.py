import os
import shutil

import image_highlighter

from documento_justificacion import DocumentoJustificacion
from utilidades import leer_frontmatter, buscar_imagenes_en_carpetas, imprimir_error, imprimir_correcto

# Constantes Generales
DOCUMENT_SAVE_PATH = "justificacion/"
IMAGES_SOURCE_DIR = "justificacion/images"
IMAGES_DEST_DIR = "justificacion/images_justificated"
IMAGEN_WIDTH_INCHES = 6.268
IMAGEN_HEIGHT_INCHES = 3.356

# Lista completa de Imágenes usadas durante la Justificación, con sus claves de busqueda como archivo
IMAGENES_A_BUSCAR = {
    "justificacion/images_justificated/1": ["titu", "ip", "fecha", "whois"],
    "justificacion/images_justificated/2": ["pagina1", "pagina2", "pagina3"],
    "justificacion/images_justificated/3": ["movil", "escritorio", "tablet"],
    "justificacion/images_justificated/4": ["wp-login", "upload", "page=nestedpages","action=edit","action=elementor"],
    "justificacion/images_justificated/5": ["cylex", "hotfrog", "firmania"],
    "justificacion/images_justificated/6.1": ["translate-settings", "translate-plugin"],
    "justificacion/images_justificated/6.2": ["tradu1", "tradu2", "tradu3"],
}

# Nombres de documentos a justificar
FILENAME_TITULARIDAD = "2. Titularidad y Fecha de Expiración del Dominio.docx"
FILENAME_PUBLICIDAD = "3. Captura Publicidad Web.docx"
FILENAME_DIRECTORIOS = "A4. Directorios.txt.docx"
FILENAME_PKD = "PKD_P1C_Sitio_Web.docx"
FILENAME_ACCESIBILIDAD = "Informe_Revision_Accesibilidad_Sitios_web.xlsx"

# Listas de palabras a reemplazar (en el docx tienen  ___clave___ )
CLAVES_PALABRAS_TITULARIDAD = ["Beneficiario", "DNI", "Inicio Servicio", "Fin Servicio", "Website Home"]
CLAVES_PALABRAS_DIRECTORIOS = ["Directorio Cylex", "Directorio Firmania", "Directorio Hotfrog", "WP version",
                               "Website Home", "Website Page2","Website Page3","traduccion","site name","tipo negocio",
                               "atraer a","servicios negocio","interesados en","seo titulo 1","seo titulo 2",
                               "site page2 name", "site page3 name"]
CLAVES_PALABRAS_PKD = ["Beneficiario", "DNI", "Inicio Servicio", "Fin Servicio", "Website Home","Website Page2",
                       "Website Page3", "site page2 name", "site page3 name", "Directorio Cylex", "Directorio Hotfrog",
                       "Directorio Firmania"]

# Lista de claves a reemplazar por imagenes (en el docx tienen el valor ___img_clave_)
CLAVES_IMAGENES_TITULARIDAD = ["titu", "ip", "fecha", "whois"]
CLAVES_IMAGENES_PKD_CON_TRADUCCION = [value for sublist in IMAGENES_A_BUSCAR.values() for value in sublist]
filtered_dict = {key: value for key, value in IMAGENES_A_BUSCAR.items() if key != "justificacion/images_justificated/6.2"}
CLAVES_IMAGENES_PKD_SIN_TRADUCCION  = [value for sublist in filtered_dict.values() for value in sublist]


CLAVES_IMAGENES_TRADUCCION = ["tradu1","tradu2","tradu3"]

# The Main Method
def main():
    # Marcar Imágenes con rectangulos rojos para la justificacion

    image_highlighter.main(IMAGES_SOURCE_DIR, IMAGES_DEST_DIR)

    # Diccionario de imagenes con la clave de busqueda y sus valores siendo una lista de imágenes
    dict_imagenes = buscar_imagenes_en_carpetas(IMAGENES_A_BUSCAR)

    # Leer frontmatter del archivo markdown
    datos_frontmatter = leer_frontmatter(os.getcwd(), "notas")

    # Obtener la ruta del script de ejecución
    script_folder = os.path.dirname(os.path.abspath(__file__))
    template_folder = os.path.join(script_folder, "justificacion_template")

    # Justificacion Documento Titularidad
    imagenes_titularidad = {clave: dict_imagenes[clave] for clave in CLAVES_IMAGENES_TITULARIDAD}

    documento_titularidad = DocumentoJustificacion(FILENAME_TITULARIDAD)
    documento_titularidad.cargar_documento(template_folder)
    documento_titularidad.reemplazar_textos(CLAVES_PALABRAS_TITULARIDAD, datos_frontmatter, autoagregar_enlaces=True)
    documento_titularidad.reemplazar_imagenes(imagenes_titularidad, IMAGEN_WIDTH_INCHES, IMAGEN_HEIGHT_INCHES)
    documento_titularidad.guardar_documento(DOCUMENT_SAVE_PATH)
    documento_titularidad.imprimir_estadisticas()

    # Copia la imagen de la publicidad y prepara el archivo docx en blanco para la edicción manual
    try:
        imagen_publicidad = dict_imagenes["pagina1"][-1]
        shutil.copy(imagen_publicidad, os.path.join(DOCUMENT_SAVE_PATH,"CAPTURA DE PUBLICIDAD.png"))
        shutil.copy(os.path.join(template_folder, FILENAME_PUBLICIDAD), DOCUMENT_SAVE_PATH)
        imprimir_correcto(f"Imagenes de publicidad y Documento de publicidad copiados correctamente")
    except Exception as e:
        imprimir_error(f"Error al copiar los archivos de publicidad: {e}")

    # Justificacion Documento Directorios
    documento_directorios = DocumentoJustificacion(FILENAME_DIRECTORIOS)
    documento_directorios.cargar_documento(template_folder)
    documento_directorios.reemplazar_textos(CLAVES_PALABRAS_DIRECTORIOS, datos_frontmatter, autoagregar_enlaces=True)
    documento_directorios.guardar_documento(DOCUMENT_SAVE_PATH)
    documento_directorios.imprimir_estadisticas()

    # Justificacion Documento PKD
    if "no" in datos_frontmatter["traduccion"].lower():
        dict_imagenes = {clave: dict_imagenes[clave] for clave in CLAVES_IMAGENES_PKD_SIN_TRADUCCION}
    else:
        dict_imagenes = {clave: dict_imagenes[clave] for clave in CLAVES_IMAGENES_PKD_CON_TRADUCCION}

    # Copia archivo de Accesibilidad
    try:
        shutil.copy(os.path.join(template_folder, FILENAME_ACCESIBILIDAD), DOCUMENT_SAVE_PATH)
        imprimir_correcto(f"Archivo de Accesibilidad copiado correctamente")
    except Exception as e:
        imprimir_error(f"Error al copiar el archivo de Accesibilidad: {e}")

    documento_pkd = DocumentoJustificacion(FILENAME_PKD)
    documento_pkd.cargar_documento(template_folder)
    documento_pkd.reemplazar_textos(CLAVES_PALABRAS_PKD, datos_frontmatter, autoagregar_enlaces=True)
    documento_pkd.reemplazar_imagenes(dict_imagenes, IMAGEN_WIDTH_INCHES, IMAGEN_HEIGHT_INCHES)
    documento_pkd.guardar_documento(DOCUMENT_SAVE_PATH)
    documento_pkd.imprimir_estadisticas()


if __name__ == "__main__":
    main()
