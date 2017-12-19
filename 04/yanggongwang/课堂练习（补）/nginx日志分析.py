# encoding: utf-8

# 日志分析与统计函数
# 函数直接使用老师课堂上成果
# 返回值是用户指定的TopN条日志
def LogAnalysis(log_file, topN=10):
    # 第一步：打开文件，统计IP,URL,status获取访问次数
    rt_dict = {}
    log_files = open(log_file, 'r')
    while True:
        line = log_files.readline()
        if not line:
            break
        (ip, url, status) = line.split()[0], line.split()[6], line.split()[8]
        rt_dict[(ip, url, status)] = rt_dict.get((ip, url, status), 0) + 1
    log_files.close()
    # 字典数据转换成list，方便排序
    rt_list = rt_dict.items()
    result = sorted(rt_list, key=lambda x: x[1], reverse=True)[:10]
    return result

# 定义一个文件写入函数
# 该函数接收两个参数：文件名，统计数据
# 展示使用的web页面通过模版文件生成
# index.tpl是模版文件，作为常量写入代码中了
def file_write(htmlfile,Count_IP_URL_Status):
    with open(htmlfile,'w') as f:
        with open('index.tpl') as f_read:
            f.writelines(f_read.read().format(Count_IP_URL_Status=Count_IP_URL_Status))


# 调用函数
if __name__ == '__main__':
    log_file = 'access.txt'
    result = LogAnalysis(log_file, topN=12)

    Count_IP_URL_Status = ''
    htmlfile = 'index.html'

    #_count 变量用于标明每一行的序号
    _count = 0
    for i in result:
        _count += 1
        Count_IP_URL_Status += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(_count,i[1],i[0][0],i[0][1],i[0][2])

    file_write(htmlfile, Count_IP_URL_Status)
