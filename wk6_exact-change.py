# write a program that takes a payment, compares it to the price of an item, and returns exact change. 


def exactChange(cost, payment):
    DENOMINATIONS = [100,50,20,10,5,1,0.25,0.1,0.05,0.01]
    change_owed = payment-cost
    list_of_change = []

    if change_owed > 0:
        while change_owed>DENOMINATIONS[-1]:
            for denomination in DENOMINATIONS:
                if denomination < change_owed:
                    change_owed-denomination
                    list_of_change.append(DENOMINATIONS)
                    break 

    print(list_of_change)


exactChange(7.50, 10)



# DID NOT WORK CODE
    # if change > 0:
    #     if int(change)!=0:
    #         print(int(change))
        
    #     if change-int(change) > 0:
    #         for u in denominations:
    #             if u<=change-int(change)>0:
    #                 print(u)

# GOOD CODE FOR THE END
    # elif dif<0:
    #     print("You don't have enough.")
    # else:
    #     print("Thank you for your payment.")
  
# BONUS assignment
# code a sorting algorithm