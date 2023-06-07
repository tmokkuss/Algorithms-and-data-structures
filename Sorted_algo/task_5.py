def sort_products_by_sales(categories):
    for category in categories:
        products = category['products']
        sorted_products = sorted(products, key=lambda x: x['sales'], reverse=True)
        category['products'] = sorted_products

    return categories

categories = [
    {
        'name': 'Electronics',
        'products': [
            {'name': 'Laptop', 'sales': 50},
            {'name': 'Smartphone', 'sales': 100},
            {'name': 'Tablet', 'sales': 30}
        ]
    },
    {
        'name': 'Clothing',
        'products': [
            {'name': 'Shirt', 'sales': 80},
            {'name': 'Jeans', 'sales': 60},
            {'name': 'Dress', 'sales': 40}
        ]
    },
    {
        'name': 'Books',
        'products': [
            {'name': 'Novel', 'sales': 20},
            {'name': 'Biography', 'sales': 10},
            {'name': 'Self-help', 'sales': 5}
        ]
    }
]

sorted_categories = sort_products_by_sales(categories)

for category in sorted_categories:
    print("Категория:", category['name'])
    for product in category['products']:
        print("Товар:", product['name'], "Продажи:", product['sales'])
    print()
