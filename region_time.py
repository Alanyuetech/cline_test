import pytz
from datetime import datetime

def get_region_time(region):
    """
    根据输入的地区名返回该地区的当前时间
    
    参数:
        region (str): 地区名，例如 'Asia/Shanghai', 'America/New_York' 等
                      完整的时区列表可以通过 pytz.all_timezones 获取
    
    返回:
        str: 格式化的时间字符串
    
    示例:
        >>> get_region_time('Asia/Shanghai')
        '2023-04-25 14:30:45 CST'
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
        return formatted_time
    except pytz.exceptions.UnknownTimeZoneError:
        return f"错误: 未知时区 '{region}'。请使用有效的时区名称，例如 'Asia/Shanghai'"

if __name__ == "__main__":
    # 示例使用
    print("北京时间:", get_region_time('Asia/Shanghai'))
    print("纽约时间:", get_region_time('America/New_York'))
    print("伦敦时间:", get_region_time('Europe/London'))
