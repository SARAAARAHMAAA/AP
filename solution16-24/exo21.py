import math

def length(lst):
    if not isinstance(lst, list):
        raise TypeError("The input must be a list.")
    return len(lst)

def mean(lst):
    if not isinstance(lst, list):
        raise TypeError("The input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    return sum(lst) / len(lst)

def range_of_list(lst):
    if not isinstance(lst, list):
        raise TypeError("The input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    return max(lst) - min(lst)

def median(lst):
    if not isinstance(lst, list):
        raise TypeError("The input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

def standard_deviation(lst):
    if not isinstance(lst, list):
        raise TypeError("The input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    mean_value = mean(lst)
    squared_diff = [(x - mean_value) ** 2 for x in lst]
    variance = sum(squared_diff) / len(lst)
    return math.sqrt(variance)

def list_statistics(lst):
    if not isinstance(lst, list):
        raise TypeError("The input must be a list.")
    
    stats = {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }
    
    return stats


if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        [],
        [7],
        [-1, -2, -3, -4, -5],
        [1.5, 2.5, 3.5],
        [10, 20, 30, 40, 50]
    ]
    
    for test_list in test_lists:
        print(f"Testing list: {test_list}")
        try:
            print("Length:", length(test_list))
            print("Mean:", mean(test_list))
            print("Range:", range_of_list(test_list))
            print("Median:", median(test_list))
            print("Standard Deviation:", standard_deviation(test_list))
            print("Statistics Dictionary:", list_statistics(test_list))
        except Exception as e:
            print(f"Error: {e}")
        print()
