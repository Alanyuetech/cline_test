import pytz
from datetime import datetime

def get_region_time(region):
    """
    根据输入的地区名返回该地区的当前时间
    
    参数:
        region (str): 地区名，例如 'Asia/Shanghai', 'America/New_York' 等
                      完整的时区列表可以通过 pytz.all_timezones 获取
    
    返回:
        tuple: (datetime对象, 格式化的时间字符串)
    """
    try:
        # 获取指定时区
        timezone = pytz.timezone(region)
        # 获取当前UTC时间
        utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
        # 转换为指定时区的时间
        local_time = utc_now.astimezone(timezone)
        # 格式化时间
        formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        return local_time, formatted_time
    except pytz.exceptions.UnknownTimeZoneError:
        return None, f"错误: 未知时区 '{region}'。请使用有效的时区名称，例如 'Asia/Shanghai'"

def calculate_time_difference(region1, region2):
    """
    计算两个地区之间的时差，并显示它们当前的时间
    
    参数:
        region1 (str): 第一个地区的名称
        region2 (str): 第二个地区的名称
    
    返回:
        dict: 包含两个地区当前时间和时差的字典
    """
    # 获取第一个地区的时间
    dt1, formatted_time1 = get_region_time(region1)
    
    # 获取第二个地区的时间
    dt2, formatted_time2 = get_region_time(region2)
    
    result = {
        "region1": {
            "name": region1,
            "current_time": formatted_time1
        },
        "region2": {
            "name": region2,
            "current_time": formatted_time2
        }
    }
    
    # 如果有任一地区返回的是错误信息，则无法计算时差
    if dt1 is None or dt2 is None:
        result["time_difference"] = "无法计算时差，请检查地区名称是否正确"
        return result
    
    # 计算时差（小时）
    time_diff_seconds = (dt2.utcoffset().total_seconds() - dt1.utcoffset().total_seconds())
    time_diff_hours = time_diff_seconds / 3600
    
    # 格式化时差
    if time_diff_hours > 0:
        result["time_difference"] = f"{region2} 比 {region1} 早 {abs(time_diff_hours):.1f} 小时"
    elif time_diff_hours < 0:
        result["time_difference"] = f"{region2} 比 {region1} 晚 {abs(time_diff_hours):.1f} 小时"
    else:
        result["time_difference"] = f"{region1} 和 {region2} 处于同一时区"
    
    return result

if __name__ == "__main__":
    # 示例用法
    region1 = "Asia/Shanghai"  # 北京时间
    region2 = "America/New_York"  # 纽约时间
    
    result = calculate_time_difference(region1, region2)
    
    print(f"地区 1: {result['region1']['name']}")
    print(f"当前时间: {result['region1']['current_time']}")
    print(f"\n地区 2: {result['region2']['name']}")
    print(f"当前时间: {result['region2']['current_time']}")
    print(f"\n时差: {result['time_difference']}")
    
    # 示例：让用户输入两个地区
    print("\n\n请输入两个地区来计算时差:")
    user_region1 = input("地区 1 (例如 Asia/Shanghai): ")
    user_region2 = input("地区 2 (例如 America/New_York): ")
    
    user_result = calculate_time_difference(user_region1, user_region2)
    
    print(f"\n地区 1: {user_result['region1']['name']}")
    print(f"当前时间: {user_result['region1']['current_time']}")
    print(f"\n地区 2: {user_result['region2']['name']}")
    print(f"当前时间: {user_result['region2']['current_time']}")
    print(f"\n时差: {user_result['time_difference']}") 