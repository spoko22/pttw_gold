
def transform_array_to_string(sequence):
    string_form = ''
    for bit in sequence:
        string_form += str(int(bit))
    return string_form


def transform_string_to_array(input_sequence):
    sequence = []
    for bit in input_sequence:
        sequence.append(int(bit))
    return sequence
