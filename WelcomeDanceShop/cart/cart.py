from WelcomeDanceShop.settings import CART_SESSION_ID
from goods.models import Goods

'''В данном файле прописаны методы для работы с корзиной. Представления корзины находятся в cart/views.py'''


class Cart:
    # Инициализация корзины в сессии:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

        # print('-----------------')
        # print(cart)
        # print(list(cart.keys())) - можно использовать для провеки работы метода __init__ в консоли

    # Появление товара в корзине и увеличение количества конкретного товара:
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранить состояние корзины:
    def save(self):
        self.session.modified = True

    # Удалить товар из корзины:
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    # Метод для отображения всех имеющихся в корзине товаров
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Goods.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Получение количества единиц в корзине для менеджера контекста
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # Получение итоговой стоимости всей корзины для дальнейшей оплаты
    def get_total_price(self):
        return sum(int(item['price']) * int(item['quantity'])
                   for item in self.cart.values())

    # Очистка корзины после создания заказа и при выходе из сессии
    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()


# Менеджер контекста
def cart(request):
    return {'cart': Cart(request)}
