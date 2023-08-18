from pay import Pay
from paypal import PayPal
from cash import Cash
from card import Card

def process_pay(payment_method, amount):
  return payment_method.make_pay(amount)

pay = Pay()
print(process_pay(pay, 400))

paypal = PayPal("test@mail.com")
print(process_pay(paypal, 240))

cash = Cash()
print(process_pay(cash, 400))  

card = Card("4913478952471122")
print(process_pay(card, 100))

card1 = Card("913478952471122")
print(process_pay(card1, 100))