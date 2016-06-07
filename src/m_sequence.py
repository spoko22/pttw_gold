# author: spoko

import numpy
import math
import correlation as cor

preferred_pairs = {5: [[5,2], [5,4,3,2]], 6: [[6,1], [6,5,2,1]], 7: [[7,3], [7,3,2,1]],
                   # 8: [[8,7,6,5,2,1], [8,7,6,1]],
                   9: [[9,4], [9,6,4,3]]}

available_lengths = preferred_pairs.keys()


def generated_mls_from_preferred_pair(L):
    if L in preferred_pairs:
        register_1 = preferred_pairs[L][0]
        register_2 = preferred_pairs[L][1]
        return mls_generation(L, register_1), mls_generation(L, register_2)
    elif L > 9:
        print 'Generating code with ' + str(L) + ' registers would take too long. Aborting.'
        return None, None
    else:
        print 'No preferred pairs for this length of shift registers'
        return None, None


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
        print 'One or both of the sequences does not exist'
        return False
    if len(seq1) != len(seq2):
        print 'Sequences are not the same length'
        return False

    values_set = set(cor.correlation(seq1, seq2))

    if len(values_set) == 3:
        L = float(len(seq1))
        l = math.log(int(L+1), 2)
        m = 2 if l%2 == 0 else 1
        t = float(1 + 2**((l+m)/2))

        acceptable_values = [float("{0:.5f}".format(-t/L)), float("{0:.5f}".format(-1/L)), float("{0:.5f}".format((t-2)/L))]

        for value in values_set:
            if value not in acceptable_values:
                message = 'Autocorrelation of preferred pair can only have three values and these are: '
                for acceptable_value in acceptable_values:
                    message += '\n' + str(acceptable_value)
                message += '\nOne of existing values (' + str(value) + ') is not a valid one.'
                print message
                return False
        print 'Preferred pair was found. Gold codes will be generated shortly.'
        return True
    else:
        print 'Crosscorrelation function does not have three values: ' + str(len(values_set))
        return False