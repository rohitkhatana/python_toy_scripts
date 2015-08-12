import sys
import fileinput
from collections import defaultdict

total_n_word, total_m_word = sys.stdin.readline().split(' ')

occurence_of_n_with_index = defaultdict(list)

for index in range(1, int(total_n_word)+1):
    occurence_of_n_with_index[sys.stdin.readline().rstrip('\n')].append(index)

m_words = []

for index in range(int(total_m_word)):
    m_words.append(sys.stdin.readline().rstrip('\n'))

for word in m_words:
    if len(occurence_of_n_with_index[word]) == 0:
        sys.stdout.write('-1')
    for exists_index in occurence_of_n_with_index[word]:
        sys.stdout.write(str(exists_index) + ' ')
    sys.stdout.write('\n')


