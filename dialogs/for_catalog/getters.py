from aiogram_dialog import DialogManager
from bson.objectid import ObjectId

from config.mongo_config import products, product_categories, carts


async def get_product_category(dialog_manager: DialogManager, **middleware_data):
    categories = list(product_categories.find({}))
    data = [(i['title'], i['_id']) for i in categories]
    return {'categories': data}


async def get_sizes(dialog_manager: DialogManager, **middleware_data):
    context = dialog_manager.current_context()
    category_id = context.dialog_data['category_id']
    sizes = products.distinct('size', {'category': ObjectId(category_id)})
    return {'sizes': sizes}


async def get_amounts(dialog_manager: DialogManager, **middleware_data):
    context = dialog_manager.current_context()
    category_id = context.dialog_data['category_id']
    amounts = product_categories.find_one({'_id': ObjectId(category_id)})['amounts']
    return{'amounts': amounts}


async def get_colors(dialog_manager: DialogManager, **middleware_data):
    context = dialog_manager.current_context()
    category_id = context.dialog_data['category_id']
    colors = product_categories.find_one({'_id': ObjectId(category_id)})['colors']
    return{'colors': colors}


async def get_product(dialog_manager: DialogManager, **middleware_data):
    context = dialog_manager.current_context()
    category_id = context.dialog_data['category_id']
    size = context.dialog_data['size']
    amount = context.dialog_data['amount']
    product = products.find_one({'category': ObjectId(category_id), 'size': size})
    price = product['price']
    full_price = int(amount) * price
    return {
        'product': product['title'],
        'size': size,
        'amount': amount,
        'color': context.dialog_data['color'],
        'price': price,
        'full_price': full_price
    }


async def get_positions(dialog_manager: DialogManager, **middleware_data):
    user_id = dialog_manager.event.from_user.id
    user_cart = carts.find_one({'user_id': user_id})
    positions = user_cart.get('positions') if user_cart is not None else []
    return {'pos_sum': len(positions)}
