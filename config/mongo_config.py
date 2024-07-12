import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)

db = client['trinket_db']
products = db['products']
product_categories = db['product_categories']
users = db['users']
orders = db['orders']
carts = db['carts']


'''
структура данных cart
    '_id': дефолтный первичный ключ
    'user_id':
    'positions': [{product, amount, color, datetime}]

структура данных products
    '_id': дефолтный первичный ключ
    'title': название товара (брелок, стенд, фурнитура)
    'category': категория товаров
    'size': размер товара,
    'price': цена товара,
    'dimensions': размеры для расчета доставки

структура данных users
    '_id': дефолтный первичный ключ
    'user_id':
    'address':
    'username':

структура данных orders
    '_id': дефолтный первичный ключ
    'user_id':
    'datetime':
    'address':
    'products': []
'''
