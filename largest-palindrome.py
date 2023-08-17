# En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.

# Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista, la función debe devolver None. Si hay más de un palíndromo con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.

# Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante como hacia atrás.

# Ejemplo 1:


# Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

# Output: "racecar"

# Ejemplo 2:


# Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])

# Output: None

def isPalindrome(word):
  return word == word[::-1]

def find_largest_palindrome(words):
  palindromes = [word for word in words if isPalindrome(word.lower())]
  if len(palindromes)>0:
    return max(palindromes)
  else: return None

print(find_largest_palindrome(['cooc', 'boob']))