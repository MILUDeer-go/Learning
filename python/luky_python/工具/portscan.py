from scapy.all import *
from time import time
from scapy.layers.inet import IP, TCP

# 使用TCP Connect扫描
def TCP_Connect(ip, num):
    print(f"***TCP_Connect开始扫描{ip}***")
    t1 = time()
    count = 0

    for port in range(1, num):
        p = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=0.1, verbose=0)
        # 没有收到响应包，则为关闭
        if str(type(p)) == "<class 'NoneType'>":
            p1 = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=0.1, verbose=0)
            if str(type(p1)) == "<class 'NoneType'>":
                pass
        # 收到不是TCP的数据包就跳过
        elif p.haslayer(TCP) == False:
            pass
        # 收到flags为“SA”的SYN/ACK包
        elif p["TCP"].flags == "SA":

            # 再发送一个RST/ACK包给目标主机建立连接
            p1 = sr1(IP(dst=ip) / TCP(dport=port, flags="A"), timeout=0.1, verbose=0)
            p2 = sr1(IP(dst=ip) / TCP(dport=port, flags="R"), timeout=0.1, verbose=0)
            print(f"{ip}: {port}  Open")
            count += 1
        # 收到的flags为“R”的RST（复位）包
        else:
            # print(f"{ip}: {i} Close")
            pass
    print(f"***扫描结束,端口开放{count}个****共耗时：{time() - t1}")


# 使用TCP SYN扫描
def TCP_SYN(ip, num):
    print(f"***TCP_SYN开始扫描{ip}***")
    t1 = time()
    count = 0

    for port in range(1, num):
        p = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=0.1, verbose=0)
        # 没有收到响应包
        if str(type(p)) == "<class 'NoneType'>":
            pass
        # 收到flags为“SA”的SYN/ACK包
        elif p.haslayer(TCP) == False:
            pass
        elif p["TCP"].flags == "SA":
            # 发送一个RST包复位
            send(IP(dst=ip) / TCP(dport=port, flags="R"))
            print(f"{ip}: {port} Open")

            count += 1
        # 收到的flags为“R”的RST（复位）包
        else:
            # print(f"{ip}: {i} Close")
            pass
    print(f"***扫描结束,端口开放{count}个****共耗时：{time() - t1}")

# TCP ACK扫描:
# 只能判断目标主机是否过滤端口，开放或关闭都返回RST；过滤端口返回ICMP或者无响应；没过滤返回RST
def TCP_ACK(ip, num):
    print(f"***TCP_ACK开始扫描{ip}***")
    t1 = time()
    count = 0

    for port in range(1, num):
        p = sr1(IP(dst=ip) / TCP(dport=port, flags="A"), timeout=0.1, verbose=0)
        # 没有收到响应包，则为关闭
        if str(type(p)) == "<class 'NoneType'>":
            pass
        # 收到的flags为“R”的RST（复位）包
        elif p["TCP"].flags == "R":
            print(f"{ip}: {port}   Unfiltered")

            count += 1

        else:
            # print(f"{ip}: {i} Close")
            pass
    print(f"***扫描结束,端口没过滤{count}个****共耗时：{time() - t1}")


# TCP_NULL/XMAS/FIN扫描
# 返回RST则端口关闭，没有响应则可能是开放或者被屏蔽
# windows主机不可用，都返回RST

def TCP_NXF(ip, num):
    flag = ""
    while True:
        print("请输入N来进行NULL扫描；输入X进行XMAS扫描；输入F进行FIN扫描！")
        flag_ = str(input("flag=")).upper()
        if flag_ == "N":
            break
        elif flag_ == "X":
            flag += "PFU"
            break
        elif flag_ == "F":
            flag += "F"
            break
        else:
            print("输入格式错误")

    print(f"***TCP_NXF开始扫描{ip}***")

    t1 = time.time()
    count = 0

    for port in range(1, num):
        p = sr1(IP(dst=ip) / TCP(dport=port, flags=flag), timeout=0.1, verbose=0)
        # 没有收到响应包，则为开放或者没被屏蔽
        if str(type(p)) == "<class 'NoneType'>":
            # 可能是丢包再发一次
            p1 = sr1(IP(dst=ip) / TCP(dport=port, flags=flag), timeout=0.1, verbose=0)
            if str(type(p1)) == "<class 'NoneType'>":
                print(f"{ip}: {port}   Open or Unfiltered")
                count += 1
            else:
                pass
        # 收到flags为“RA”的RST/ACK包
        elif p["TCP"].flags == "RA":
            pass

        # 收到的其他类型包
        else:
            print(f"{ip}: {port} Open or Unfiltered")
            count += 1
            # pass
    print(f"***扫描结束,端口开放或无过滤{count}个****共耗时：{time.time() - t1}")


if __name__ == '__main__':
    ip = str(input("请输入正确格式IP地址："))
    # ip = '169.254.157.128'
    try:
        num = int(input("请输入要扫描的端口数(默认1024个端口)："))
    except ValueError:
        num = 1025
    count = 0
    while True:
        print("请输入TCP扫描方式：")
        print("1.TCP SYN输入：S\t2.TCP_Connect输入：T\t")
        print("3.TCP ACK输入：A\t4.TCP NULL/XMAS/FIN输入：Y\t")
        print("5.退出请按：q")
        select = str(input("select:"))
        if select == 's' or select == 'S':
            TCP_SYN(ip, num)
        elif select == "t" or select == 'T':
            TCP_Connect(ip, num)
        elif select == 'a' or select == "A":
            TCP_ACK(ip, num)

        elif select == 'q' or select == 'Q':
            break
        elif select == 'y' or select == 'Y':
            TCP_NXF(ip, num)
        else:
            print("输入格式错误！")
        print("=" * 40)
