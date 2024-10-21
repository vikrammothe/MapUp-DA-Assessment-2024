from typing import Dict, List

import pandas as pd
import itertools
import re
import polyline
from geopy.distance import geodesic
import numpy as np





def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    result = []
    for i in range(0,len(lst), n);
    sublist = lst[i:i+n]
    reversed_sublist = []
    for j in range(len(sublist)-1, -1, -1):
    return lst
    print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8,], 3))
    print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4))


def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
    # Your code here
    result = {]
        for word in lst:
              length = len(word)
    if length not in result:
        result[length] =[]
        result[length].append(word)
        return dict(sorted(result.items()))
        print(group_by_length(["apple", "bat", "cat", "elephant", "dog", "bear"]))
        

def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    # Your code here
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for idx, item in enumerate(v):
                items.extend(flatten_dict(item, f"{new_key}[{idx}]", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

print(flatten_dict(nested_dict))



def unique_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.
    
    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Your code here
    return list(map(list, set(itertools.permutations(lst))))
    print(unique_permutations([1, 1, 2]))  
    pass


def find_all_dates(text: str) -> List[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.
    
    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    pattern = r"\b(?:\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2})\b"
    return re.findall(pattern, text)
    text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
    print(find_all_dates(text))  
    pass

def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
     coords = polyline.decode(encoded_string)
    df = pd.DataFrame(coords, columns=["latitude", "longitude"])
    df['distance'] = df.apply(lambda row: geodesic(coords[0], (row['latitude'], row['longitude'])).meters if row.name > 0 else 0, axis=1)
    return df
encoded_string = "encoded_polyline_string_here"
df = decode_polyline_to_df(encoded_string)
print(df)
##return pd.Dataframe()


def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate the given matrix by 90 degrees clockwise, then multiply each element 
    by the sum of its original row and column index before rotation.
    
    Args:
    - matrix (List[List[int]]): 2D list representing the matrix to be transformed.
    
    Returns:
    - List[List[int]]: A new 2D list representing the transformed matrix.
    """
    # Your code here
    n = len(matrix)
    rotated = [[matrix[n-j-1][i] for j in range(n)] for i in range(n)]
    transformed = []
    for i in range(n):
        row_sum = sum(rotated[i])
        transformed_row = []
        for j in range(n):
            col_sum = sum(rotated[k][j] for k in range(n))
            transformed_row.append(row_sum + col_sum - 2 * rotated[i][j])
        transformed.append(transformed_row)
    
    return transformed
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_and_transform(matrix))
    ##return []


def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df['start_time'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_time'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    def has_full_coverage(group):
        total_time = sum((group['end_time'] - group['start_time']).dt.total_seconds()) / 86400
        return total_time >= 7  # Covering all 7 days
        return df.groupby(['id', 'id_2']).apply(has_full_coverage)
        df = pd.read_csv('dataset-1.csv')
        print(check_full_week_coverage(df))

    ##return pd.Series()
