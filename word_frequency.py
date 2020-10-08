#!/usr/local/bin/python3
from string import punctuation

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


# def is_punct(s):
#     return s.isprintable() and not (s.isalpha() or s.isspace() or s.isdigit())

def format_word_freq(wf):
    format_width = max(len(w) for w in wf)
    output_string = ""

    for w in sorted(wf, key=wf.get, reverse=True):
        count = wf[w]
        output_string += f"{w:>{format_width}} : {count} {'*' * count}\n"
    
    return output_string


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    with open(file) as wordsfile:
        words = wordsfile.read()
    
    words = words.lower()

    # print(words)

    for p in punctuation:
        words = words.replace(p, '')

    wordslist = words.split()

    for s_w in STOP_WORDS:
        while s_w in wordslist:
            wordslist.remove(s_w)

    wordcount = {}

    for w in wordslist:
        if w in wordcount:
            wordcount[w] += 1
        else:
            wordcount[w] = 1

    formatted = format_word_freq(wordcount)
    print(formatted)



# boiler plate


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
