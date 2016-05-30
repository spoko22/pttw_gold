# author: spoko

import numpy

def autocorrelation(input_seq):
    return correlation(input_seq, input_seq)


def correlation(in_seq1, in_seq2):
    if len(in_seq1) != len(in_seq2):
        print 'Length of sequences should be the same! ' \
              'Length of seq. 1. is ' + str(len(in_seq1)) + ' and length of seq. 2. is ' + str(len(in_seq2))
        raise

    seq_1 = []
    seq_2 = []
    seq_length = len(in_seq1)
    for bit in in_seq1:
        if bit:
            seq_1.append(1)
        else:
            seq_1.append(-1)

    for bit in in_seq2:
        if bit:
            seq_2.append(1)
        else:
            seq_2.append(-1)

    seq_stable = seq_1
    seq_shift = seq_2
    values_set = []
    for i in xrange(seq_length):
        value = 0
        for j in xrange(seq_length):
            value += (seq_stable[j] * seq_shift[j])
        # value = value/float(seq_length)
        # value = float("{0:.5f}".format(value))
        values_set.append(value)
        seq_shift = numpy.roll(seq_shift, 1)
    return values_set