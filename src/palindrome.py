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
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo')
            else:
                print(f'"{entrada}" no es un palíndromo. Su inverso es: "{entrada[::-1]}"')
