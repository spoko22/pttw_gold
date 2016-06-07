import numpy


class Scrambler:
    def __init__(self, gold_sequence):
        self.gold_sequence = gold_sequence

    def scramble(self, input_sequence):
        if not self.__validate_input(input_sequence):
            return None

        return xnor_sequence_and_gold(input_sequence, self.gold_sequence)

    def __validate_input(self, input_sequence):
        return True


class Descrambler:
    def __init__(self, gold_sequence):
        self.gold_sequence = gold_sequence

    def descramble(self, scrambled_sequence):
        if not self.__validate_input(scrambled_sequence):
            return None

        return xnor_sequence_and_gold(scrambled_sequence, self.gold_sequence)

    def __validate_input(self, spreaded_sequence):
        return True


def xnor_sequence_and_gold(seq, gold):
    gold_len = len(gold)
    result_sequence = []

    for i in xrange(len(seq)):
        bit = seq[i]
        gold_bit = gold[i % gold_len]
        bit = (bit + gold_bit + 1) % 2  # this simulates XNOR gate. If gold_bit = 1, bit is unchanged. If gold_bit = 0, bit is flipped
        result_sequence.append(bit)

    return result_sequence
