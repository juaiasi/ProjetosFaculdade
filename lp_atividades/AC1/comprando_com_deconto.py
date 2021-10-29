price = float(input())
amount = int(input())
no_discount = amount*price
basic_discount = no_discount*0.9
total_discount = basic_discount-no_discount*(amount*0.01)
print(f"{no_discount:.2f}")
print(f"{total_discount:.2f}")