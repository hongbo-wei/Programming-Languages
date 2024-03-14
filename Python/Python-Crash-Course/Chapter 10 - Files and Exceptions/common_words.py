# 10-10 Common Words

from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in a file."""
    path = Path(filename)

    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print('Please make sure the file is in the same directory as this program')
    else:
        # count('the') and count('the ') are different, the first one count any
        # word has 'the' in it, for example: they.
        count = content.lower().count('the ')
        print(f"The file '{filename.removesuffix('.txt')}' "
              f"has {count} 'the' word(s) in it")


text_files = ['the_dreams.txt',
              'Yale_literary_magazine.txt',
              'miles_straight_up.txt']

for file in text_files:
    count_words(file)
