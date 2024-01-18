two_digit_number = input("Type a two digit number: ")
results = 0
digits = [int(i) for i in two_digit_number]
result =  sum(digits)
# for i in digits:
#     results +=i 
#print(results)
print(result)