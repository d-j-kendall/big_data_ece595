#!/usr/bin/python3
import sys
def withdraw():
    try:
        val = int(input('Please enter the withdrawal amount(multiples of 5): '))
        if val%5 != 0 or val < 0:
            raise ValueError
        else:
            return val
    except ValueError:
        print("\nYou have entered an invalid value, try again.\n")
        return withdraw()
    except Exception as e:
        print(f"An error occured\n\n{e}")
        sys.exit()

w_amount = withdraw()

bill_dict = {
 "$100" : 0,
 "$50"  : 0,
 "$20"  : 0,
 "$10"  : 0,
 "$5"   : 0
}

bill_dict["$100"] = int(w_amount/100)
w_amount = w_amount%100
bill_dict["$50"] = int(w_amount/50)
w_amount = w_amount%50
bill_dict['$20'] = int(w_amount/20)
w_amount = w_amount%20
bill_dict['$10'] = int(w_amount/10)
w_amount = w_amount%10
bill_dict['$5'] = int(w_amount/5)
w_amount = w_amount%5

print('\n\nYou will receive the following bills : \n\n')

for denomination, amount in bill_dict.items():
    if(amount is not 0):
        print(f"{denomination} : {amount}")
