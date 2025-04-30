# 访问百度热搜https://top.baidu.com/board?tab=realtime
# 1. 获取前十名的数据，并保存到文件中
import os
import requests
from bs4 import BeautifulSoup

url = "https://top.baidu.com/board?tab=realtime"
output_dir = "src/assets/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

def get_baidu_hot():
    try:
        print("正在获取百度热搜...")
        response = requests.get(url, headers=headers)
        response.encoding = "utf-8"
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        html_file_path = os.path.join(output_dir, 'baidu_hot.html')
        with open(html_file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        # 获取热搜标题列表
        hot_list = soup.select(".c-single-text-ellipsis")

        file_name = "baidu_hot_10.txt"
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            for i, hot in enumerate(hot_list):
                file.write(f"{i+1}. {hot.text}\n")
        print("已保存到文件:", file_path, "\n")
    except requests.exceptions.RequestException as e:
        print("请求失败:", e)
    else:
        print("获取百度热搜完成")


if __name__ == "__main__":
    get_baidu_hot()
