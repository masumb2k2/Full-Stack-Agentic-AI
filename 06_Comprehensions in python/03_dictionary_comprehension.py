tea_prices ={
    'Masala Tea': 100,
    'Green tea': 150,
    'Lemon Tea': 500
}

tea_price_in_USD = {tea:price / 127 for tea, price in tea_prices.items()}
print(tea_price_in_USD)