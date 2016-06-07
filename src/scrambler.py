import sys
import os
import m_sequence
import scrambling
import gold
import random as rnd
import sequence_converter as seq_conv

print("Your file should have one line constisting of zeros and ones. No commas, no white spaces, no dots, no JSON structures, just zeros and ones like this: 0101010101")
user_file_input = raw_input("Enter the path of your file: ")

assert os.path.exists(user_file_input), "I did not find the file at, " +str(user_file_input)
f = open(user_file_input, 'r+')
sequence = seq_conv.transform_string_to_array(f.read().rstrip())
print('OK, I read your input. Please, be aware that the scrambler reads ONLY one, first line. Your file is:\n') + str(sequence)

print('Now we need the desired length of LSFR. Assuming the value you enter here is called \'L\' the length of Gold sequence will be 2^L - 1.')
user_gold_length = 0
while True:
    available_lengths = m_sequence.available_lengths
    for length in available_lengths:
        print "L = " + str(length) + ", which produces Gold sequence with length: " + str((2**length)-1)
    user_gold_length = int(raw_input("Enter the length of LSFR: "))
    if user_gold_length in available_lengths:
        break
    else:
        print("Invalid LSFR length value: "+str(user_gold_length)+". Try again.")
        continue

if user_gold_length > 0:
    seq1, seq2 = m_sequence.generated_mls_from_preferred_pair(user_gold_length)
    gold_codes = gold.generate_gold(seq1, seq2)
    gold_code = rnd.sample(gold_codes, 1)[0]
    gold_code_filename = 'gold_code.txt'
    gold_file = open(gold_code_filename, 'w+')
    gold_file.write(seq_conv.transform_array_to_string(gold_code))
    gold_file.close()
    print 'Your gold code was written to file: ' + gold_code_filename + '. Don\'t lose this, you will need this code to descramble the message!'
    scrambler = scrambling.Scrambler(gold_code)
    scrambled_sequence_filename = 'output.txt'
    scrambled_sequence = open('output.txt', 'w+')
    scrambled_sequence.write(seq_conv.transform_array_to_string(scrambler.scramble(sequence)))
    scrambled_sequence.close()
    print 'The scrambled sequence was written to file: ' + scrambled_sequence_filename + '. Insert this file along with Gold code into the descrambler to see the world being descrambled.'

f.close()