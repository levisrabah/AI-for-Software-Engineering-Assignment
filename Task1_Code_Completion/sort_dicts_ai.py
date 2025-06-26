"""
Task 1: AI-suggested implementation of sorting a list of dictionaries by a specific key.
(Simulated Copilot/Tabnine suggestion)
"""

def sort_by_key(lst, key):
    """
    Sort a list of dictionaries by a given key.
    Args:
        lst (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(lst, key=lambda d: d[key])

# Example usage
data = [
    {"name": "Levis", "age": 31},
    {"name": "Samson", "age": 23},
    {"name": "Moses", "age": 15}
]

print("Sorted by age:", sort_by_key(data, "age")) 