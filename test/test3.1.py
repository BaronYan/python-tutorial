amount = 1000

def show_amount():
    print(amount)

show_amount()

def add_amount(count):
    global amount
    amount += count


add_amount(1000)

show_amount()
