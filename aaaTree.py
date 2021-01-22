import  requests
import time
url='https://movie.douban.com/j/chart/top_list'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 '
                  'Safari/537.36 SE 2.X MetaSr 1.0 '}
params={
'type': '5',
'interval_id': '100:90',
'action':'',
'start': '100',
'limit': '20'
}
res=requests.get(url=url,params=params,headers=header).json()
print(res)
time.sleep(1)
with open('file.txt','w',encoding='utf8')as f:
    f.write(str(res))
    print('成功')
