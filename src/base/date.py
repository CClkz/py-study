from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print(f"当前时间: {now}")

# 格式化时间
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"格式化时间: {formatted_time}")

# 时间计算（加减天数）
one_day_later = now + timedelta(days=1)
one_day_earlier = now - timedelta(days=1)
print(f"一天后: {one_day_later}")
print(f"一天前: {one_day_earlier}")

# 解析字符串为时间
date_str = "2023-10-01 12:00:00"
parsed_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"解析后的时间: {parsed_time}")

# 计算时间差
time_diff = one_day_later - now
print(f"时间差: {time_diff}")
print(f"时间差（秒）: {time_diff.total_seconds()}")

# 获取特定时间
specific_time = datetime(2023, 10, 1, 12, 0, 0)
print(f"特定时间: {specific_time}")
