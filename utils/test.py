import datetime as dt

import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)

db = client['trinket_db']
products = db['products']
users = db['users']
orders = db['orders']
materials = db['materials']
product_categories = db['product_categories']

CATEGORIES = {
    'Брелоки': [10, 30, 50, 100, 200, 300, 500, 1000],
    'Стенды': [10, 30, 50, 100, 200, 300, 500, 1000],
    'Фурнитура': [10, 100]
}
PRODUCTS = {
    '1': {
        'title': 'Брелок',
        'category': 'Брелоки',
        'size': 'до 3 см',
        'price': 100,
        'dimensions': [],
    },
    '2': {
        'title': 'Брелок',
        'category': 'Брелоки',
        'size': 'до 6 см',
        'price': 200,
        'dimensions': [],
    },
    '3': {
        'title': 'Брелок',
        'category': 'Брелоки',
        'size': 'до 8 см',
        'price': 300,
        'dimensions': [],
    },
    '4': {
        'title': 'Стенд',
        'category': 'Стенды',
        'size': '4-25 см',
        'price': 500,
        'dimensions': [],
    },
}
COLORS = ['Цветной', 'Прозрачный', 'Голо', 'Свт', 'Золотой', 'Флуор']
MATERIAL = ['Акрил']

for title, amounts in CATEGORIES.items():
    product_categories.insert_one({'title': title, 'amounts': amounts, 'colors': COLORS})

for item in PRODUCTS.values():
    products.insert_one(
        {
            'title': item['title'],
            'category': product_categories.find_one({'title': item['category']})['_id'],
            'size': item['size'],
            'price': item['price'],
            'dimensions': item['dimensions'],
        }
    )
# for m in MATERIAL:
#     materials.insert_one({'type': m, 'colors': COLORS})
