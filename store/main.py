from product import Product

class Article(Product):
  def addToCart(self):
    return f"Agregando {self.quantity} unidades del artículo {self.name} al carrito"
    pass
  
class Service(Product):
  def addToCart(self):
    return f"Agregando el servicio {self.quantity} al carrito"
  
class Cart:
  def __init__(self):
    self.products = []
  
  def addProduct(self, product):
    self.products.append(product)
    return product.addToCart()
  
  def deleteProduct(self, product):
    self.products.remove(product)
  
  def calculateTotal(self):
    return sum([(product.price * product.quantity) for product in self.products])
  
  def getProducts(self):
    return self.products[:]

# book = Article("Libro", 100, 2);
# course = Service("Curso", 120, 1);

# cart = Cart();
# cart.addProduct(book);
# cart.addProduct(course);
# print(cart.calculateTotal());