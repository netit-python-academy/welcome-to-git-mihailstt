budget = 600000.00
people = 100
ticket_type = 'vip'

if people >=1 and people <= 4:
    transport = (budget * 75) / 100
    money = budget - transport
    if ticket_type == 'normal':
        ticket_price = people * 249.99
    elif ticket_type == 'vip':
        ticket_price = people * 499.99
    if (money - ticket_price) > 0:
            print ("Yes! Money left: {:.2f}".format(money - ticket_price))
    elif (money - ticket_price) <= 0:
            print("No! You need {:.2f}".format(money - ticket_price))

if people >=5 and people <= 9:
    transport = (budget * 60) / 100
    money = budget - transport
    if ticket_type == 'normal':
        ticket_price = people * 249.99
    elif ticket_type == 'vip':
        ticket_price = people * 499.99
    if (money - ticket_price) > 0:
            print ("Yes! Money left: {:.2f}".format(money - ticket_price))
    elif (money - ticket_price) <= 0:
            print("No! You need {:.2f}".format(money - ticket_price))

if people >=10 and people <= 24:
    transport = (budget * 50) / 100
    money = budget - transport
    if ticket_type == 'normal':
        ticket_price = people * 249.99
    elif ticket_type == 'vip':
        ticket_price = people * 499.99
    if (money - ticket_price) > 0:
            print ("Yes! Money left: {:.2f}".format(money - ticket_price))
    elif (money - ticket_price) <= 0:
            print("No! You need {:.2f}".format(money - ticket_price))

if people >=25 and people <= 49:
    transport = (budget * 40) / 100
    money = budget - transport
    if ticket_type == 'normal':
        ticket_price = people * 249.99
    elif ticket_type == 'vip':
        ticket_price = people * 499.99
    if (money - ticket_price) > 0:
            print ("Yes! Money left: {:.2f}".format(money - ticket_price))
    elif (money - ticket_price) <= 0:
            print("No! You need {:.2f}".format(money - ticket_price))

if people >= 50:
    transport = (budget * 25) / 100
    money = budget - transport
    if ticket_type == 'normal':
        ticket_price = people * 249.99
    elif ticket_type == 'vip':
        ticket_price = people * 499.99
    if (money - ticket_price) > 0:
            print ("Yes! Money left: {:.2f}".format(money - ticket_price))
    elif (money - ticket_price) <= 0:
            print("No! You need {:.2f}".format(money - ticket_price))