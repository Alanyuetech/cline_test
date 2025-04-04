from datetime import datetime

def print_current_time():
    """打印当前时间"""
    now = datetime.now()
    print(f"当前时间是: {now.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    print_current_time()