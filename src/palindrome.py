def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    while True:
        entrada = input("Ingrese una palabra o frase: ")
        if is_palindrome(entrada):
            print(f'"{entrada}" es un palíndromo')
        else:
            print(f'"{entrada[::-1]}" no es un palíndromo')    
