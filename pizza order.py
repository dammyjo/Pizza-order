print("Welcome to Pizza deliveries please make your order")
size=input(str("which size do you want? small medium or large"))
add_pepperoni=input(str("do you want pepperoni yes or no"))
cheese=input(str("do you want cheese yes or no"))
small_pizza=15
medium_pizza=20
large_pizza=25
small_pepperoni=2
lm_pepperoni = 3
extra_cheese=1
if size==("small"):
    total=small_pizza
    print(f"the total amount of your pizza is ${total}")
    if add_pepperoni == ("yes"):
        total=small_pizza+small_pepperoni
        print(f"the amount of your pizza with pepperoni is ${total}")
        if cheese == ("yes"):
            total=small_pizza+small_pepperoni+extra_cheese
            print (f"the total amount of your pizza with pepperoni and cheese is ${total}")
        else:
            total = small_pizza + small_pepperoni + extra_cheese
            print (f"the total amount of your pizza with pepperoni and cheese is ${total}")
    else:
        print(f"the total amount of your pizza is ${total}")

elif size==("medium"):
    total=medium_pizza
    print(f"the total amount of your pizza is ${total}")
    if add_pepperoni == ("yes"):
        total=medium_pizza+ lm_pepperoni
        print(f"the amount of your pizza is ${total}")
        if cheese == ("yes"):
            total = medium_pizza + lm_pepperoni + extra_cheese
            print (f"the total amount of your pizza is ${total}")
        else:
            total = medium_pizza +lm_pepperoni + extra_cheese
            print(f"the total amount of your pizza is ${total}")

    else:
        print(f"the total amount of your pizza is ${total}")

elif size==("large"):
    total=large_pizza
    print(f"the total amount of your pizza is ${total}")
    if add_pepperoni == ("yes"):
        total=large_pizza+lm_pepperoni
        print(f"the amount of your pizza is ${total}")
        if cheese == ("yes"):
            total = large_pizza+lm_pepperoni + extra_cheese
            print (f"the total amount of your pizza is ${total}")
        else:
            total = large_pizza + lm_pepperoni + extra_cheese
            print (f"the total amount of your pizza with pepperoni and cheese is ${total}")
    else:
        print(f"the total amount of your pizza is ${total}")

else:
    print("invalid order")
