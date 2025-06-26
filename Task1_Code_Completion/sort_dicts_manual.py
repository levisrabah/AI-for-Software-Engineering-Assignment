"""
Task 1: Manual implementation of sorting a list of dictionaries by a specific key.
"""

def sort_dicts_by_key(dict_list, sort_key):
    """
    Sorts a list of dictionaries by the specified key.
    Args:
        dict_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.
    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x.get(sort_key, None))

# Example usage
data = [
    {"name": "Levis", "age": 31},
    {"name": "Samson", "age": 23},
    {"name": "Moses", "age": 15}
]

sorted_data = sort_dicts_by_key(data, "age")
print("Sorted by age:", sorted_data) 