def make_alpha_dict(text):
    words = text.split()
    return {
        char: [w for w in words if char in w]
        for char in set(text) if char.isalpha()
    }