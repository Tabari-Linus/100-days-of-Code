# import clear
#HINT: You can call clear() to clear the output in the console.
bid_data = {}

def larg(name):
    pos = ''
    larges = 0
    for name in bid_data:
        if larges < bid_data[name]:
            larges = bid_data[name]
            pos = name
    return pos

biding = True
while biding:
    name = input("What is your name?: ")
    bid_data[name] = float(input("What's your bid?: "))

    will_bid = input("Yes to bid No to stop")
    if will_bid.lower() == 'no':
        biding = False
    # clear()
    print("-----------------\n\n")

print( f"The winner is {larg(bid_data)}: ${bid_data[larg(bid_data)]}")
