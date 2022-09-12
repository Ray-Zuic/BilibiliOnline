import time

import schedule1


# 引入schedule和time

def job():
    print("I'm working...")


# 定义一个叫job的函数，函数的功能是打印'I'm working...'

schedule1.every().day.at("9:00").do(job)  # 部署在每天的10:30执行job()函数的任务

while True:
    schedule1.run_pending()
    time.sleep(1)
# 设置调度的参数，这里是每2秒执行一次
# schedule.every(2).seconds.do(job)
if __name__ == '__main__':
    while True:
        schedule.run_pending()
# 执行结果
# a simple scheduler in python.
# a simple scheduler in python.
# a simple scheduler in python.
# ...
