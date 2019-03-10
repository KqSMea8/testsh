#! /usr/bin/python
# author:liuzhe
# 2019.3.8

import subprocess

id = "wb-lz525541"
year ="2001"
mounth = "3"
day = "7"




def getresult(id,year,mounth,day):
    '''
    获得统计结果
    :param id:
    :param year:
    :param mounth:
    :param day:
    :return:
    '''
    a = subprocess.check_output('git log --author="{0}@alibaba-inc.com" --numstat --after={1}-{2}-{3}'.format(id,year,mounth,day)).decode('gbk')
    lines_num = [x for x in a.split('\n') if x ]
    dict = {int(x.split('\t')[0]):int(x.split('\t')[1]) for x in lines_num if x[0].isdigit()}
    insert_lines = sum(dict.keys())
    delete_lines = sum(dict.values())
    effective_lines = insert_lines-delete_lines
    return insert_lines,delete_lines,effective_lines

if __name__ == '__main__':
    insert_lines, delete_lines, effective_lines = getresult(id,year,mounth,day)
    print("新增行数{}\n删除行数{}\n有效行数{}".format(insert_lines,delete_lines,effective_lines))