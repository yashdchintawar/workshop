'''
    @Author: Yashdchintawar
    @Date: 2022-04-19 10:19:00
    @Last Modified by: yashdchintawar
    @Last Modified time: 2022-04-19 10:19:00
    @Title : Atm MAchine Code that Simulates All Notes.

'''

def rupee_notes(user_amount):
    note_1, note_10,note_100,note_500,note_1000,note_2000 = 0

    if (user_amount>2000):
        note_2000 = int(user_amount/2000)
        note_amount = note_2000 * 2000
        user_amount -= note_amount 
    
    if (user_amount>1000):
        note_1000 = int(user_amount/1000)
        note_amount = note_1000 * 1000
        user_amount -= note_amount 
    
    if (user_amount>500):
        note_500 = int(user_amount/500)
        note_amount = note_500 * 500
        user_amount -= note_amount 
    
    if (user_amount>100):
        note_100 = int(user_amount/100)
        note_amount = note_100 * 100
        user_amount -= note_amount 
    
    if (user_amount>10):
        note_10 = int(user_amount/10)
        note_amount = note_10 * 10
        user_amount -= note_amount 
    
    if (user_amount>1):
        note_1 = user_amount 

    amount_dict = {2000: note_2000, 1000: note_1000, 500: note_500, 100: note_100, 10: note_10, 1: note_1}

    return amount_dict

if __name__ == '__main__':
    
    user_amount = int(input("Enter The Amount To check"))
    final_amount = rupee_notes(user_amount)

    print(final_amount)