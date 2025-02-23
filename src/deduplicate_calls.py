

def deduplicate_with_time_window(api_calls, time_window=2):
    # 假设api_calls是一个包含类名、方法名、时间戳和Backtrace的列表
    deduplicated_calls = []
    current_window = []
    last_timestamp = None

    for call in api_calls:
        # 将时间戳转为秒（假设时间戳是一个浮动的UNIX时间戳，单位是秒）
        timestamp = call['Timestamp']
        call_id = (call['Class Name'], call['Method Name'], tuple(call['Backtrace']))

        # 检查当前时间是否在当前窗口内（例如时间窗口为2秒）
        if last_timestamp is None or timestamp - last_timestamp <= time_window:
            # 如果当前调用和上次调用在2秒内，则加入当前时间窗口
            if call_id not in [(c['Class Name'], c['Method Name'], tuple(c['Backtrace'])) for c in current_window]:
                current_window.append(call)
        else:
            # 如果时间超出了2秒，处理当前窗口，并重置窗口
            deduplicated_calls.append(current_window)
            current_window = [call]

        last_timestamp = timestamp

    # 加入最后一个窗口
    if current_window:
        deduplicated_calls.append(current_window)

    return deduplicated_calls

# 示例API调用数据
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

# 去重操作
deduplicated_calls = deduplicate_with_time_window(api_calls, time_window=2)

# 输出去重后的结果
for group in deduplicated_calls:
    print(f"Time Window:")
    for call in group:
        print(f"  Timestamp: {call['Timestamp']} | Class: {call['Class Name']} | Method: {call['Method Name']} | Backtrace: {call['Backtrace']}")
