def discount_checker(threshold, *purchases):
    exceeding_customers = []
    for customer_num, purchase in enumerate(purchases, start=1):
        if purchase > threshold:
            exceeding_customers.append(customer_num)
    return exceeding_customers


if __name__ == '__main__':
    result = discount_checker(1000, 500, 1500, 800, 1200)
    print(result)
