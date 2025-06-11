def average(ns):
    if not ns:
        raise ValueError("List cannot be empty.")
    return sum(ns) / len(ns)