'''
    @Author: Yashdchintawar
    @Date: 2022-04-20 10:36:00
    @Last Modified by: yashdchintawar
    @Last Modified time: 2022-04-20 10:36:00
    @Title : Electricity bill Genrator.

'''

def unit_price_check(user_unit):
    charge_amount = 0

    unit = 1
    for i in range(50):
        user_unit -= 1
        unit += 1
        if user_unit == 0:
            break

    unit = 0
    for i in range(100): # 51-150
        if user_unit == 0:
            break
        user_unit -= 1
        unit += 1
    charge_amount += unit * 1

    unit = 0
    for i in range(100): # 151-250
        if user_unit == 0:
            break
        user_unit -= 1
        unit += 1
    charge_amount += unit * 3

    unit = 0
    while True: # Above 250 Unit
        if user_unit == 0:
            break
        user_unit -= 1
        unit += 1
    charge_amount += unit * 5

    return charge_amount


if __name__ == '__main__':
    user_unit = int(input("Enter The Unit To Get Bill!"))

    print(f"Total Charge For {user_unit} Is: ",unit_price_check(user_unit))

