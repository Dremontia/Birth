"""
dict 客户端
功能：根据用户输入发送请求，得到结果
结构：一级界面 --> 注册 登录 退出
     二级界面 --> 查单词 历史记录 注销

"""

from socket import *
from getpass import getpass  # 运行只能使用终端 不能在pycham中运行
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8000)

# 功能函数都需要套接字，定义为全局变量
s = socket()
s.connect(ADDR)


# 注册函数
def do_register():
    while True:
        name = input("姓名：")
        passwd = getpass('密码：')
        passwd_ = getpass('确认密码：')

        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格！")
            continue
        if passwd != passwd_:
            print("两次密码不一致.")
            continue

        msg = 'R %s %s' % (name, passwd)
        s.send(msg.encode())  # 发送请求
        data = s.recv(1024).decode()  # 接收反馈信息
        if data == "OK":
            print("注册成功")
        else:
            print("注册失败")
        return


# 登录函数
def do_sign():
    while True:
        name = input("姓名：")
        passwd = getpass('密码：')
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格！")
            continue
        msg = 'S %s %s' % (name, passwd)
        s.send(msg.encode())  # 发送请求
        data = s.recv(1024).decode()  # 接收反馈信息
        if data == "OK":
            print("登录成功")
            do_interface(name)  # 登陆成功更换到二级界面
        else:
            print("登录失败,用户名或密码错误.")
        return


# 查询单词处理
def do_words(name):
    while True:
        words = input("请输入单词：")
        if words == '##':
            break
        msg = 'W %s %s' % (words, name)
        s.send(msg.encode())  # 发送请求
        data = s.recv(1024).decode()  # 接收反馈信息
        if data:
            print("查询结果：", data)
        else:
            print("查询错误，无此单词")


def do_history(name):
    msg = 'H %s' % name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(128).decode()
            if data == '##':
                break
            print(data)
    else:
        print("没有历史记录")


# 二级界面
def do_interface(name):
    while True:
        print("""
        =======================welcome======================
        1) 查询单词           2) 查询历史                3) 注销
        ====================================================
        
        """)
        cmd = input("输入选项：")
        if cmd == "1":
            do_words(name)
        elif cmd == "2":
            do_history(name)
        elif cmd == "3":
            return
        else:
            print("请输入正确选项")


# 搭建客户端网络
def main():
    while True:
        print("""
        =======================welcome======================
        1) 注册                 2) 登录                3) 退出
        ====================================================
        """)
        cmd = input("输入选项：")
        if cmd == "1":
            do_register()
        elif cmd == "2":
            do_sign()
        elif cmd == "3":
            s.send(b'E')
            sys.exit('谢谢使用')
        else:
            print("请输入正确选项")


if __name__ == '__main__':
    main()
