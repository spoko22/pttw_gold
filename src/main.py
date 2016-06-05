# author: spoko

import numpy
import pylab
import mls
import filter
import gold
import correlation
import m_sequence


seq1 = m_sequence.mls_generation(5, [5,3])
seq2 = m_sequence.mls_generation(5, [5,1,3,2])
# seq1, seq2 = m_sequence.generated_mls_from_preferred_pair(6)
is_preferred = m_sequence.is_pair_preferred(seq1, seq2)

if is_preferred:
    gold_codes = gold.generate_gold(seq1, seq2)
    frequency = dict()
    i = 0
    print '\n\n---------------- GOLD CODES ----------------'
    for gold_code in gold_codes:
        if i<50 and len(gold_code) < 128:
            print gold_code
        elif i == 50 and len(gold_code) < 128:
            print 'And ' + str(len(gold_codes)-50) + ' more...'
        values_set = set(correlation.correlation(gold_code, gold_code))
        if frequency.get(len(values_set)) is None:
            frequency[len(values_set)] = 1
        else:
            frequency[len(values_set)] += 1
        i += 1
    print '\n\n---------------- SUMMARY ----------------'
    for value in frequency:
        print str(value) + " unique values occurency count: " + str(frequency[value])

elif seq1 is not None and seq2 is not None:
    print "Given pair of sequences is not a preferred one. Exiting."
else:
    print "Exiting."