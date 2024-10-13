import requests
products_json_url = 'https://dummyjson.com/products?limit=200'
response = requests.get(products_json_url)
response_json = response.json()
products: list[dict] = response_json['products']
cost = 0
for product in products:
# 1
    if product.get('brand') == 'TechGear':
        print('Products id created by TechGear:', product['id'])
# 3
    if product['price'] >= 800:
        cost = product['price'] * product['stock']
# print('General products cost, which price is more than 800$', cost)

# 2
url_picture = "https://cdn.dummyjson.com/products/images/smartphones/Vivo%20V9/3.png"
response1 = requests.get(url_picture)
with open('phone.png', mode='wb') as file:
    file.write(response1.content)
