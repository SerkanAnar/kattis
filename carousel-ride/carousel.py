while True:
    n, m = map(int, input().strip().split())
    if n == 0 and m == 0:
        break
    minimum_discount = 0
    best_a = 0
    best_b = 0
    for i in range(n):
        a, b = map(int, input().strip().split())
        price_per_ticket = a / b
        if price_per_ticket == minimum_discount and a <= m:
            if a > best_a:
                best_a = a
                best_b = b
                minimum_discount = price_per_ticket
        elif price_per_ticket > minimum_discount and a <= m:
            best_a = a
            best_b = b
            minimum_discount = price_per_ticket
    if minimum_discount == 0:
        print("No suitable tickets offered")
    else:
        print(f'Buy {best_a} tickets for ${best_b}')