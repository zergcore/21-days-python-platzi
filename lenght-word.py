# En este desafío, debes crear una función llamada count_words_by_length que recibe una lista de palabras y devuelve un diccionario que mapea la longitud de las palabras a la cantidad de palabras que tienen esa longitud.

# Ejemplo 1:

# Input:
# count_words_by_length([
#   "apple",
#   "banana",
#   "orange",
#   "grapefruit",
#   "pear",
#   "kiwi"
# ])

# Output:
# {5: 1, 6: 2, 10: 1, 4: 2}

# Ejemplo 2:

# Input:
# count_words_by_length([
#   "apple",
#   "banana",
#   "orange"
# ])

# Output:
# {5: 1, 6: 2}

def count_words_by_length(words):
  return {len(word):sum(1 for w in words if len(w) == len(word)) for word in words}

print(count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
]))