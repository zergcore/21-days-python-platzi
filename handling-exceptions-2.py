# En este desafío, debes crear una función llamada calculate_discounted_price que calcule el precio con descuento de un producto. La función recibirá dos parámetros: price (precio) y discount (descuento). Tu objetivo es implementar la lógica necesaria para calcular el precio con el descuento aplicado.

# Sin embargo, hay algunas condiciones y manejo de excepciones que debes tener en cuenta:

# Si el precio o el descuento son valores negativos, deberás lanzar una excepción del tipo ValueError con el mensaje "El precio y el descuento deben ser valores positivos".

# Si el precio o el descuento no son números, deberás lanzar una excepción del tipo TypeError con el mensaje "El precio y el descuento deben ser números".

# En caso de que ocurra cualquier otro tipo de excepción no prevista, deberás capturarla y lanzar una excepción genérica del tipo Exception con el mensaje "Ha ocurrido un error inesperado" seguido del mensaje de la excepción original para obtener más detalles.

# Tu función debe retornar el precio con el descuento aplicado. Si el cálculo se realiza correctamente, deberás retornar el resultado. En caso de producirse alguna excepción, deberás propagarla para que pueda ser manejada en el contexto adecuado.

# Ejemplo 1:


# Input: calculate_discounted_price(100, 0.2)
# Output: 80.0

# Ejemplo 2:


# Input: calculate_discounted_price(-50, 0.2)
# Output: ValueError: El precio y el descuento deben ser valores positivos

def calculate_discounted_price(price, discount):
  if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
    raise TypeError("El precio y el descuento deben ser números")

  if price < 0 or discount < 0:
    raise ValueError("El precio y el descuento deben ser valores positivos")
  
  try:
    discounted_price = price - (price * discount)
    return discounted_price
  except Exception as e:
    raise Exception("Ha ocurrido un error inesperado: " + str(e))

calculate_discounted_price(-50, 0.2)