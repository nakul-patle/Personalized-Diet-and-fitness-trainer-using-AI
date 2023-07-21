from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    # print(product,cart)
    for id in keys:
              
        if int(id) == product.id:
            return True
    return False

@register.filter(name='quantity_cart')
def quantity_cart(product,cart):
    keys=cart.keys()
    # print(product,cart)
    for id in keys:
              
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product,cart):
    return product.price *  quantity_cart(product,cart)

@register.filter(name='currency')
def currency(numbers):
    return "₹ " + str(numbers)

@register.filter(name='multipy')
def multipy(number,number1):
    return number * number1

@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum=0
    for p in products:
        sum+=price_total(p,cart)
    
    return sum
   

