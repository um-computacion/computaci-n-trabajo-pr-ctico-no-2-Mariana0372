
import sys
import os
import re
import unicodedata

# Agregar el directorio superior al path para poder importar correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def is_palindrome(text):
    """
    Verifica si una cadena de texto es un palíndromo.

    Un palíndromo es una palabra o frase que se lee igual de izquierda a 
    derecha que de derecha a izquierda, ignorando espacios, puntuación
    y diferencias entre mayúsculas y minúsculas.

    Args:
        text (str): La cadena de texto a verificar
        
    Returns:
        bool: True si es un palíndromo, False en caso contrario
    """
    # Si el texto está vacío, es un palíndromo por definición
    if not text:
        return True
    
    # Normalizar texto: eliminar acentos
    normalized_text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if not unicodedata.combining(c)
    )
    
    # Convertir a minúsculas y eliminar caracteres que no sean alfanuméricos
    clean_text = re.sub(r'[^a-z0-9]', '', normalized_text.lower())
    
    # Si después de la limpieza no hay caracteres, es un palíndromo
    if not clean_text:
        return True
    
    # Comparación final
    return clean_text == clean_text[::-1]

if __name__ == '__main__':
    """

    Programa interactivo para verificar palíndromos.
    Presiona Ctrl+C para salir.

    """
    try:
        while True:
            user_input = input("Ingrese una palabra o frase: ")
            if is_palindrome(user_input):
                print(f'"{user_input}" es un palíndromo')
            else:
                print(f'"{user_input}" no es un palíndromo')
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")



