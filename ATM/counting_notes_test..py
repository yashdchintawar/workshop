'''
    @Author: Yashdchintawar
    @Date: 2022-04-19 10:19:00
    @Last Modified by: yashdchintawar
    @Last Modified time: 2022-04-19 10:19:00
    @Title : Testihng Atm Machine Code that Simulates All Notes.

'''

import counting_notes
import unittest

class counting_notes_test(unittest.TestCase):

    def test_rupee_notes(self):
        result = counting_notes.rupee_notes(5835)
        self.assertEqual(result, {2000: 2, 1000: 1, 500: 1, 100: 3, 10: 3, 1: 5})

if __name__ == '__main__':
    unittest.main()