def group_anagrams(words):
    return {
        "".join(sorted(w)): [word for word in words if sorted(word) == sorted(w)]
        for w in words
    }