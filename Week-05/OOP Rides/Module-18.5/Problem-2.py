def count_words(S):
    words = S.split()

    freq_dict = {}

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    for word,count in freq_dict.items():
        print(word.capitalize(),count)
S = "We tried list and we tried dicts also we tried Zen"
count_words(S)

