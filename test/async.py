import asyncio
import numpy as np

def func(sec):
    dum = []
    for j in np.arange(1000*sec):
        dum_ = np.cos(j*180/np.pi)
        dum.append(dum_)
    return dum
        

 
async def app_sleep(sec):
    """
    非同期スリープ。与えられた秒数後に完了する関数
    :param sec:
    :return:
    """
    loop = asyncio.get_event_loop()
    print(f"start{sec}")
    # asyncio の提供する非同期スリープ。await でこの関数内においては同期的に用いる
    #await asyncio.sleep(sec)
    await v = loop.run_in_executor(None, func, sec)
    print(f"end{sec}")
    print(v)
    return f"これは app_sleep({sec}) の返り値"



async def main():
    # 二つの非同期関数を非同期実行して返り値を得る
    a = app_sleep(5)
    b = app_sleep(1)
    [ret_a, ret_b] = await asyncio.gather(a, b)
    # 返り値を表示
    print(ret_a)
    print(ret_b)
 
 
if __name__ == '__main__':
    print('ここは同期処理のはじまり')
    # asyncio.run は同期処理の中から非同期処理を呼び出せます
    asyncio.run(main())
    print('ここは同期処理のおわり')
 
"""
ここは同期処理のはじまり
start3
start1
end1
end3
これは app_sleep(3) の返り値
これは app_sleep(1) の返り値
ここは同期処理のおわり
"""