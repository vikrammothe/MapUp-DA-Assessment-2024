import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    unique_ids = pd.unique(df[['from_id', 'to_id']].values.ravel('K'))

   
    distance_matrix = pd.DataFrame(np.inf, index=unique_ids, columns=unique_ids)
    
    
    np.fill_diagonal(distance_matrix.values, 0)

  
    for _, row in df.iterrows():
        distance_matrix.loc[row['from_id'], row['to_id']] = row['distance']
        distance_matrix.loc[row['to_id'], row['from_id']] = row['distance']  # Ensure symmetry

    
    for k in unique_ids:
        for i in unique_ids:
            for j in unique_ids:
                if distance_matrix.loc[i, k] + distance_matrix.loc[k, j] < distance_matrix.loc[i, j]:
                    distance_matrix.loc[i, j] = distance_matrix.loc[i, k] + distance_matrix.loc[k, j]

    return distance_matrix

    return df



def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
   
    unrolled_data = []

    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:  
                distance = distance_matrix.loc[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    ref_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()
    
    if pd.isna(ref_avg_distance):
        return pd.DataFrame(columns=['id_start', 'average_distance'])  # Return empty if no distances found

    lower_bound = ref_avg_distance * 0.9
    upper_bound = ref_avg_distance * 1.1

    avg_distances = df.groupby('id_start')['distance'].mean().reset_index()
    avg_distances.columns = ['id_start', 'average_distance']

  
    filtered_ids = avg_distances[(avg_distances['average_distance'] >= lower_bound) & 
                                  (avg_distances['average_distance'] <= upper_bound)]

    
    sorted_result = filtered_ids.sort_values(by='average_distance')

    return sorted_result

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
     rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

   
    for vehicle, coefficient in rate_coefficients.items():
        df[vehicle] = df['distance'] * coefficient


    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    
    df['start_day'] = np.random.choice(days_of_week, size=len(df))
    df['end_day'] = np.random.choice(days_of_week, size=len(df))

 
    df['start_time'] = pd.to_datetime(np.random.choice(pd.date_range("00:00:00", "23:59:59", freq='1H'), size=len(df))).dt.time
    df['end_time'] = pd.to_datetime(np.random.choice(pd.date_range("00:00:00", "23:59:59", freq='1H'), size=len(df))).dt.time

    
    def apply_discount(row):
        start_day = row['start_day']
        start_time = row['start_time']

        if start_day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:  # Weekdays
            if start_time < pd.to_datetime("10:00:00").time():
                discount_factor = 0.8
            elif start_time < pd.to_datetime("18:00:00").time():
                discount_factor = 1.2
            else:
                discount_factor = 0.8
        else:  # Weekends
            discount_factor = 0.7

        
        for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
            row[vehicle] *= discount_factor

        return row

  
    df = df.apply(apply_discount, axis=1)

    return df
