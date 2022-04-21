'''
    @Author: Yashdchintawar
    @Date: 2022-04-20 10:36:00
    @Last Modified by: yashdchintawar
    @Last Modified time: 2022-04-20 10:36:00
    @Title : Electricity bill Genrator.

'''

import electricity_bill
import unittest

class Electricity_bill_Test(unittest.TestCase):
    def test_unit_price_check(self):
        consumer_units = 500
        self.assertEqual(1650,electricity_bill.unit_price_check(consumer_units))

if __name__ == '__main__':
    unittest.main()