import time

def get_current_timestamp():
    """
    Returns the current timestamp in seconds since the epoch.
    """
    return int(time.time())
  
# print(get_current_timestamp())

def convert_timestamp_to_readable_format(timestamp):
    """
    Converts a timestamp in seconds since the epoch to a human-readable format.
    
    Args:
        timestamp (int): The timestamp to convert.
        
    Returns:
        str: The formatted date and time string.
    """
    try:
        result = int(timestamp);
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result))
    except (ValueError, TypeError):
        return "无效时间戳"

# print(convert_timestamp_to_readable_format(get_current_timestamp()))