# author: spoko

import numpy
import correlation as cor

def mls_generation(L, xors, seed=None):
    max_length = 2**L - 1

    if seed is None:
        seed = list(numpy.ones(L))
    if len(seed) != L:
        print 'Seed length different than given L. Default seed (an array of ones) will be taken.'
        seed = list(numpy.ones(L))

    for xor in xors:
        if xor > L or xor < 0:
            print 'You try to XOR the unexisting cell of registry! XOR: ' + str(xor) + ', L: ' + str(L)
            raise

    current_register = seed
    m_sequence = []
    if len(xors) > 0:
        for i in xrange(max_length):
            m_sequence.append(current_register[L-1])
            sum = 0
            for xor in xors:
                sum += current_register[xor-1]
            sum = sum % 2
            current_register = numpy.roll(current_register, 1)
            current_register[0] = sum
            if numpy.array_equal(current_register, seed):
                break

        if len(m_sequence) == max_length:
            return m_sequence
    return None

def is_pair_preferred(seq1, seq2):
    if seq1 is None or seq2 is None:
        return False
    values_set = set(cor.correlation(seq1, seq2))
    return len(values_set) == 3
