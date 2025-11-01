

def deduplicate_with_time_window(api_calls, time_window=2):
    # Assume api_calls is a list containing class name, method name, timestamp, and backtrace
    deduplicated_calls = []
    current_window = []
    last_timestamp = None

    for call in api_calls:
        # Convert timestamp to seconds (assume it's a floating UNIX timestamp in seconds)
        timestamp = call['Timestamp']
        call_id = (call['Class Name'], call['Method Name'], tuple(call['Backtrace']))

        # Check whether the current timestamp is within the time window (e.g., 2 seconds)
        if last_timestamp is None or timestamp - last_timestamp <= time_window:
            # If the current call occurs within 2 seconds of the last one, add it to the current window
            if call_id not in [(c['Class Name'], c['Method Name'], tuple(c['Backtrace'])) for c in current_window]:
                current_window.append(call)
        else:
            # If the time exceeds 2 seconds, process the current window and reset it
            deduplicated_calls.append(current_window)
            current_window = [call]

        last_timestamp = timestamp

    # Add the final window
    if current_window:
        deduplicated_calls.append(current_window)

    return deduplicated_calls

# Example API call data
api_calls = [
    {"Timestamp": 1681902000.1, "Class Name": "CLLocation", "Method Name": "- timestamp",
     "Backtrace": [
            "0x101e148f8 /private/var/containers/Bundle/Application/9E6A2889-43F2-4CA5-AB84-2BBF2929DFC6/BaiduLiteApp.app/BaiduLiteApp!-[BBAIPLocationHelper _getIPLocationInfo]",
            "0x101e195b8 /private/var/containers/Bundle/Application/9E6A2889-43F2-4CA5-AB84-2BBF2929DFC6/BaiduLiteApp.app/BaiduLiteApp!-[BBAIPLocationHelper _getIPLocationInfo]"
    ]},
    {"Timestamp": 1681902006.0, "Class Name": "CLLocation", "Method Name": "- timestamp",
     "Backtrace": [
            "0x101e148f8 /private/var/containers/Bundle/Application/9E6A2889-43F2-4CA5-AB84-2BBF2929DFC6/BaiduLiteApp.app/BaiduLiteApp!-[BBAIPLocationHelper _getIPLocationInfo]"
    ]},
    {"Timestamp": 1681902006.2, "Class Name": "CLLocation", "Method Name": "- timestamp",
     "Backtrace": [
            "0x101e148f8 /private/var/containers/Bundle/Application/9E6A2889-43F2-4CA5-AB84-2BBF2929DFC6/BaiduLiteApp.app/BaiduLiteApp!-[BBAIPLocationHelper _getIPLocationInfo]"
    ]},
]

# Perform deduplication
deduplicated_calls = deduplicate_with_time_window(api_calls, time_window=2)

# Output the deduplicated results
for group in deduplicated_calls:
    print(f"Time Window:")
    for call in group:
        print(f"  Timestamp: {call['Timestamp']} | Class: {call['Class Name']} | Method: {call['Method Name']} | Backtrace: {call['Backtrace']}")
