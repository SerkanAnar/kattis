from collections import defaultdict

n = int(input())
for i in range(n):
    words = input().strip().split()
    freq = defaultdict(int)
    for word in words:
        freq[word[0]] += 1
    max_value = max(freq.values())
    characters = [letter for letter in freq.keys() if freq[letter] == max_value]
    print(sorted(characters)[0])