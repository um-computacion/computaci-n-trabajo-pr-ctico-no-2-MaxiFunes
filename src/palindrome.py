def is_palindrome(text):
    texto_limpio = text.lower()
    
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ü': 'u', 'ñ': 'n',
    }
    
    for acento, sin_acento in reemplazos.items():
        texto_limpio = texto_limpio.replace(acento, sin_acento)
    
    resultado = ""
    for caracter in texto_limpio:
        if caracter.isalnum():
            resultado += caracter
    
    return resultado == resultado[::-1]

if __name__ == "__main__":
    try:
        while True:
            entrada = input("Ingrese una palabra o frase (0 para salir): ")
            if entrada == "0":
                print("Programa finalizado.")
                break
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo')
            else:
                print(f'"{entrada[::-1]}" no es un palíndromo. ' + entrada[::-1])    
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")