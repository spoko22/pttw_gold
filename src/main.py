# author: spoko

import numpy
import pylab
import mls
import filter
import gold
import correlation
import m_sequence


seq1 = m_sequence.mls_generation(5, [5,2], [0,1,1,1,0])
seq2 = m_sequence.mls_generation(5, [5,4,3,2], [0,1,1,1,0])
is_preferred = m_sequence.is_pair_preferred(seq1, seq2)

if is_preferred:
    gold_codes = gold.gen_gold(seq1, seq2)
    # var = set(filter.ccorr(gold_code, gold_code).real)
    frequency = dict()
    for gold_code in gold_codes:
        values_set = set(correlation.correlation(gold_code, gold_code))
        if frequency.get(len(values_set)) is None:
            frequency[len(values_set)] = 1
        else:
            frequency[len(values_set)] += 1



    for value in frequency:
        print str(value) + " unique values occurency count: " + str(frequency[value])

else:
    print "Given pair of sequences is not a preferred one"
