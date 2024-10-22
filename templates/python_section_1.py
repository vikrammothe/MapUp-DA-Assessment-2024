from typing import Dict, List

import pandas as pd


def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    result = []
    length = len(lst)

    for i in range(0, length, n):
        # Calculate the end index for the current group
        end = min(i + n, length)
        group = []

        # Collect the current group of elements
        for j in range(i, end):
            group.append(lst[j])

        # Reverse the collected group manually and append to result
        for j in range(len(group) - 1, -1, -1):
            result.append(group[j])

    return result
    return lst


def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
        Groups the strings by their length and returns a dictionary.
    """
    length_dict = {}
    
    for string in lst:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(string)

    sorted_length_dict = dict(sorted(length_dict.items()))
    return sorted_length_dict

    # Your code here
    return dict


def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    # Your code here
     def flatten(current_dict: Dict, parent_key: str = ''):
        for key, value in current_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            
            if isinstance(value, dict):
                flatten(value, new_key)
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        flatten(item, f"{new_key}[{index}]")
                    else:
                        flattened[f"{new_key}[{index}]"] = item
            else:
                flattened[new_key] = value

    flatten(nested_dict)
    return flattened
    
    return dict



def unique_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.
    
    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Your code here
    def backtrack(start: int):
        
        if start == len(nums):
            result.append(nums[:])  
            return
        
        seen = set()  
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue  
            seen.add(nums[i])  
            
            nums[start], nums[i] = nums[i], nums[start]
          
            backtrack(start + 1)
            
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    nums.sort()  
    backtrack(0)
    return result
    pass
print(unique_permutations([1, 1, 2]))





def find_all_dates(text: str) -> List[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.
    
    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    patterns = [
        r'\b(\d{2})-(\d{2})-(\d{4})\b',         # dd-mm-yyyy
        r'\b(\d{2})/(\d{2})/(\d{4})\b',         # mm/dd/yyyy
        r'\b(\d{4})\.(\d{2})\.(\d{2})\b'        # yyyy.mm.dd
    ]
    
   
    combined_pattern = '|'.join(patterns)
    
    
    matches = re.findall(combined_pattern, text)
    
   
    valid_dates = []
    for match in matches:
        for date in match:
            if date:  # Ensure we only append non-empty matches
                valid_dates.append(date)
    
  
    return list(set(valid_dates))
    pass




def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """

    latitudes = []
    longitudes = []
    distances = [0.0]  # First point has a distance of 0
    
    for lat, lon in coordinates:
        latitudes.append(lat)
        longitudes.append(lon)
    
    
    for i in range(1, len(coordinates)):
        distance = haversine(latitudes[i-1], longitudes[i-1], latitudes[i], longitudes[i])
        distances.append(distance)

   
    df = pd.DataFrame({
        'latitude': latitudes,
        'longitude': longitudes,
        'distance': distances
    })
    
    return df
    return pd.Dataframe()


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
    # Create a new matrix for the rotated version
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated

def transform_matrix(rotated: List[List[int]]) -> List[List[int]]:
    n = len(rotated)
    final_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
           
            row_sum = sum(rotated[i]) - rotated[i][j]
            col_sum = sum(rotated[k][j] for k in range(n)) - rotated[i][j]
            final_matrix[i][j] = row_sum + col_sum
            
    return final_matrix

def rotate_and_transform_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated = rotate_matrix(matrix)
    final_matrix = transform_matrix(rotated)
    return final_matrix
    return []



def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df['start_datetime'] = pd.to_datetime(df['startDay'].astype(str) + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'].astype(str) + ' ' + df['endTime'])

   
    grouped = df.groupby(['id', 'id_2'])

    def check_coverage(group):
        
        full_week = pd.date_range(start=group['start_datetime'].min().floor('D'), 
                                   end=group['end_datetime'].max().ceil('D'), 
                                   freq='D')

       
        days_covered = group['start_datetime'].dt.date.unique()
        is_full_week = len(days_covered) >= 7

        
        full_24_hour = all(
            group[(group['start_datetime'].dt.date == day)]['start_datetime'].min() <= pd.Timestamp(day) + pd.Timedelta(hours=0) and
            group[(group['start_datetime'].dt.date == day)]['end_datetime'].max() >= pd.Timestamp(day) + pd.Timedelta(hours=23, minutes=59, seconds=59)
            for day in days_covered
        )

        return not (is_full_week and full_24_hour)  # Return True if there's a problem

   
    result = grouped.apply(check_coverage)

   
    return result.rename_axis(index=['id', 'id_2'])

    return pd.Series()
