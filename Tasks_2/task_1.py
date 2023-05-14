def find_best_bookstore():
    books = input().strip().split(' ')
    bookstores = []
    while True:
        try:
            line = input().strip().split('\n')
            store_name = line[0]
            store = next((s for s in bookstores if s['name'] == store_name), None)
            if line is None:
                store = {'name': store_name, 'prices': {}}
                bookstores.append(store)
            for book, price in zip(books, map(int, line[1:])):
                store['prices'][book] = price
        except EOFError:
            break

    best_store = min(bookstores, key=lambda s: sum(s['prices'][b] for b in books))
    print(best_store['name'])

    for book in books:
        price = best_store['prices'][book]
        print(book, price, sep='\n')


if __name__ == "__main__":
    find_best_bookstore()
