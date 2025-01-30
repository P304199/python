
product_dict = {}

# product names and prices
while True:
    product_name = input("Enter product name (or type 'done' to stop): ").strip()
    if product_name.lower() == 'done':
        break
    try:
        price = float(input(f"Enter price for {product_name}: "))
        product_dict[product_name] = price
    except ValueError:
        print("Please enter a valid price.")

# product names to display their prices
while True:
    search_product = input("Enter a product name to get the price (or type 'exit' to quit): ").strip()
    if search_product.lower() == 'exit':
        break
    if search_product in product_dict:
        print(f"The price of {search_product} is ${product_dict[search_product]:.2f}")
    else:
        print(f"Sorry, {search_product} is not in the dictionary.")


