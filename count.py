from collections import Counter

word_count = Counter()

with open('input.txt', encoding='utf-8') as input_file:
    for line in input_file:
        words = line.split(' ')
        word_count.update(words)
        print(word_count)

most_common_words = word_count.most_common(3)

for word in most_common_words:
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(f'{most_common_words}')


