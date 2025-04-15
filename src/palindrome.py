def is_palindrome(text):
    """
    Verifica si una cadena de texto es un palíndromo.
    
    Args:
        text (str): La cadena de texto a verificar
        
    Returns:
        bool: True si es un palíndromo, False en caso contrario
    """
    # Implementación básica de la estructura de la función
    # Esta función será completada en otras ramas
    pass

if __name__ == '__main__':
    """
    Programa para verificar palíndromos.
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