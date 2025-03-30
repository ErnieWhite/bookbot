def get_character_counts(contents):
    counts = {}
    for c in contents.lower():
        counts[c] = counts.get(c, 0) + 1
    return counts


def get_num_words(contents):
    word_count = len(contents.split())
    return word_count
