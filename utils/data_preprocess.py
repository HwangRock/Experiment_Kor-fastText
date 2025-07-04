def text_preprocess(input_data):
    pairs = []

    with open(input_data, "r", encoding="utf-8") as f:
        for i in f:
            words = i.strip().split("\t")
            word1, word2 = words
            pairs.append((word1, word2))

    return pairs
