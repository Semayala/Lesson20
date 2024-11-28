
from collections import Counter


product_count = Counter()

with open('input.txt', encoding='utf-8') as input_file:
    print(input_file.read())

    for line in csvFile:
        buyer = line['Vevő neve']
        products = line['Vásárolt termékek'].split(',')
        price = float(line['Ár'])
        print(line)
        for product in products:
            product_count[product] += 1

        buyer_spending[buyer] += price

most_purchased_product = product_count.most_common(1)[0]
print(most_purchased_product)
print(f"The most purchased product:{most_purchased_product[0]}, amount: {most_purchased_product[1]}")

highest_spending_buyer = max(buyer_spending.items(), key=lambda x: x[1])
print(highest_spending_buyer)
print(f"The customer who buys the highest amount: {highest_spending_buyer[0]}, amount: {highest_spending_buyer[1]} Ft")
