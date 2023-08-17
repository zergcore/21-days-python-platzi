# Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.

# Ejemplo 1:


# Input: "Hola mundo"

# Output: {
#   'H': 1, 
#   'o': 2, 
#   'l': 1, 
#   'a': 1, 
#   ' ': 1, 
#   'M': 1, 
#   'u': 1, 
#   'n': 1, 
#   'd': 1
# }

def count_letters(phrase):
  return {letter:phrase.count(letter) for letter in phrase}

count_letters("Hola mundo")