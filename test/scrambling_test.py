import unittest
import scrambling

class TestScramblingMethods(unittest.TestCase):
    def test_xnor_method(self):
        gold_sequence = [0,1,0,0,1,0]#0,1,0,0,1,0]
        test_sequence = [1,1,1,1,0,0, 0,0,0,0,1,0]
        expected_seq  = [0,1,0,0,0,1, 1,0,1,1,1,1]
        self.assertEqual(expected_seq, scrambling.xnor_sequence_and_gold(test_sequence, gold_sequence))

    def test_scrambling_method(self):
        gold_sequence = [0,1,1,0,1,0]#0,1,1,0,1,0]
        test_sequence = [1,1,1,1,0,0, 0,0,1,0,1,0]
        expected_seq  = [0,1,1,0,0,1, 1,0,1,1,1,1]
        scrambler = scrambling.Scrambler(gold_sequence)
        self.assertEqual(expected_seq, scrambler.scramble(test_sequence))


    def test_descrambling_method(self):
        gold_sequence = [0,1,1,0,1,0]#0,1,1,0,1,0]
        test_sequence = [0,1,1,0,0,1, 1,0,1,1,1,1]
        expected_seq  = [1,1,1,1,0,0, 0,0,1,0,1,0]

        descrambler = scrambling.Descrambler(gold_sequence)
        self.assertEqual(expected_seq, descrambler.descramble(test_sequence))


