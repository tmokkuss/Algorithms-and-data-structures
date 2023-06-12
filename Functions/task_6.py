class BankTransaction:
    def __init__(self):
        self.transactions = {}

    def get_transactions(self, t):
        if t == "print_it":
            self.print_transactions()
        else:
            phone, transaction_type, amount = self.parse_transaction(t)
            self.update_statistics(transaction_type, amount)

    def parse_transaction(self, transaction):
        parts = transaction.split("-")
        phone = parts[0]
        transaction_info = parts[1].split(":")
        transaction_type = transaction_info[0]
        amount = int(transaction_info[1])
        return phone, transaction_type, amount

    def update_statistics(self, transaction_type, amount):
        if transaction_type not in self.transactions:
            self.transactions[transaction_type] = {"count": 1, "total_amount": amount}
        else:
            self.transactions[transaction_type]["count"] += 1
            self.transactions[transaction_type]["total_amount"] += amount

    def print_transactions(self):
        for transaction_type, info in self.transactions.items():
            count = info["count"]
            total_amount = info["total_amount"]
            print(f"{count} транзакции типа '{transaction_type}', сумма: {total_amount}")


bank = BankTransaction()
transactions = [
    "111111111-перевод:1000",
    "222222222-снятие:500",
    "111111111-перевод:2000",
    "333333333-покупка:1500",
    "222222222-перевод:3000"
]

for transaction in transactions:
    bank.get_transactions(transaction)

bank.get_transactions("print_it")
