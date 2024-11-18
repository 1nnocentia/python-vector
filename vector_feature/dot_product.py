#dot product vector
def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Ukuran vetor harus sama")
    return sum(a * b for a, b in zip(vec1, vec2))
