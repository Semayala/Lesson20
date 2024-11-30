import re
from collections import Counter


word_count = Counter()


with open('input.txt', encoding='utf-8') as input_file:
    for line in input_file:
        words = re.findall(r'\b\w{4,}\b', line.lower())
        word_count.update(words)
        print(word_count)

most_common_words = word_count.most_common(3)
print(most_common_words)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    for word, count in most_common_words:
        output_file.write(f'{word}: {count}\n')
