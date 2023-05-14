class Bookstore:
    def __init__(self, name):
        self.name = name
        self.prices = {}

    def add_price(self, book, price):
        self.prices[book] = price

    def get_price(self, book):
        return self.prices.get(book, float('inf'))


books = input("Введите список книг через пробел: ").strip().split(' ')
bookstores = []

while True:
    store_name = input("Введите название магазина (или нажмите Enter для завершения): ").strip()
    if not store_name:
        break

    store = next((s for s in bookstores if s.name == store_name), None)
    if store is None:
        store = Bookstore(store_name)
        bookstores.append(store)

    prices = input(f"Введите цены для книг в магазине '{store_name}', разделенные запятыми: ").strip().split(' ')
    for book, price in zip(books, map(int, prices)):
        store.add_price(book, price)

best_store = min(bookstores, key=lambda s: sum(s.get_price(b) for b in books))
print(f"Лучший магазин: {best_store.name}")
for book in books:
    price = best_store.get_price(book)
    print(f"{book}: {price}")
