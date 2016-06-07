import unittest
import scrambling
import sequence_converter

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

    def test_whole_method(self):
        gold_sequence = [0,1,1,0,0,1,0]
        input_sequence = [0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0]
        scrambler = scrambling.Scrambler(gold_sequence)
        descrambler = scrambling.Descrambler(gold_sequence)
        scrambled_sequence = scrambler.scramble(input_sequence)
        retrieved_sequence = descrambler.descramble(scrambled_sequence)

        self.assertEqual(input_sequence, retrieved_sequence)

    def test_sequence_converter_string_to_array(self):
        string_seq = '01010100101'
        seq = sequence_converter.transform_string_to_array(string_seq)
        self.assertEqual(seq, [0,1,0,1,0,1,0,0,1,0,1])

    def test_sequence_converter_array_to_string(self):
        seq = [0,1,0,1,0,1,0,0,1,0,1]
        string_seq = sequence_converter.transform_array_to_string(seq)
        self.assertEqual(string_seq, '01010100101')