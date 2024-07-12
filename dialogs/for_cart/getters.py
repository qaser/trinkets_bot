from aiogram_dialog import DialogManager
from bson.objectid import ObjectId

from config.mongo_config import products, product_categories, carts


async def get_cart_positions(dialog_manager: DialogManager, **middleware_data):
    user_id = dialog_manager.event.from_user.id
    context = dialog_manager.current_context()
    user_cart = carts.find_one({'user_id': user_id})
    saved_pos = context.dialog_data.get('pos_num')
    positions = user_cart.get('positions') if user_cart is not None else []
    pos_num = 0 if saved_pos is None else saved_pos
    pos_sum = len(positions)
    if pos_sum > 0:
        context.dialog_data.update(pos_sum=pos_sum)
        context.dialog_data.update(pos_num=pos_num)
        prod = products.find_one({'_id': positions[pos_num]['product']})
        cart_price = 0
        nav_is_on = True if pos_sum > 1 else False
        for i in positions:
            prod_id = i['product']
            price = products.find_one({'_id': prod_id})['price']
            amount_price = price * i['amount']
            cart_price += amount_price
        data = {
            'cart_price': cart_price,
            'pos_num': pos_num + 1,
            'pos_sum': pos_sum,
            'date': positions[pos_num]['datetime'].strftime('%d.%m.%Y'),
            'product': prod['title'],
            'size': prod['size'],
            'color': positions[pos_num]['color'],
            'amount': positions[pos_num]['amount'],
            'price': prod['price'],
            'full_price': positions[pos_num]['full_price'],
            'nav_is_on': nav_is_on,
            'cart_not_empty': True,
            'cart_is_empty': False
        }
    else:
        data = {
            'cart_not_empty': False,
            'cart_is_empty': True
        }
    return data
