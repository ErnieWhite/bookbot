def get_sorted_character_counts(counts):
    sorted_list = []
    for k, v in counts.items():
        sorted_list.append({k: v})
    sorted_list.sort(key=lambda x: x[next(iter(x))], reverse=True)
    return sorted_list 

     
def get_character_counts(contents):
    counts = {}
    for c in contents.lower():
        counts[c] = counts.get(c, 0) + 1
    return counts


def get_num_words(contents):
    word_count = len(contents.split())
    return word_count
