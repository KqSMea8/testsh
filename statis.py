#! /usr/bin/python
# author:liuzhe
# 2019.3.8

import subprocess

id = "wb-lz525541"
year ="2001"
mounth = "3"
day = "7"
zzz = 2
class Gitlines():

    def __init__(self,id,year,mounth,day):
        self.id = id
        self.year = year
        self.mounth = mounth
        self.day = day
        self.insert_lines = 0
        self.delete_lines = 0
        self.branch = []
    def slovecontradiction(self):
        '''解决冲突'''
        subprocess.call("git add .")
        subprocess.call("git commit -m 代码统计")
        p = subprocess.call("git pull")
    def selectbranch(self):
        '''选择分支'''
        subprocess.call("git add .")
        subprocess.call("git commit -m 代码统计")
        p = subprocess.call("git pull")
        if not p:
            branch = input("请输入分支:")
            if branch in self.branch:
                print("统计过的分支")
                return None
            subprocess.call("git add .")
            subprocess.call("git commit -m 代码统计")
            status = subprocess.call("git checkout {}".format(branch))
            print(status)
            if status:

                print('分支不存在')
                return None

            self.branch.append(branch)
            self.getresult()
    def getresult(self):
        '''
        获得统计结果
        :param id:
        :param year:
        :param mounth:
        :param day:
        :return:
        '''
        a = subprocess.check_output('git log --author="{0}@alibaba-inc.com" '
                                    '--numstat --after={1}-{2}-{3}'.format(
                                    self.id,self.year,self.mounth,self.day)).decode()
        lines_num = [x for x in a.split('\n') if x ]
        dict = {int(x.split('\t')[0]):int(x.split('\t')[1]) for x in lines_num if x[0].isdigit()}
        insert_lines = sum(dict.keys())
        delete_lines = sum(dict.values())
        effective_lines = insert_lines-delete_lines
        self.insert_lines += insert_lines
        self.delete_lines += delete_lines
        print("{}分支\n新增行数{},删除行数{},有效行数{}".format(self.branch[-1],insert_lines, delete_lines, effective_lines))
        print("{}分支\n新增行数{},删除行数{},有效行数{}".format(','.join(self.branch),self.insert_lines, self.delete_lines, self.insert_lines-self.delete_lines))


if __name__ == '__main__':
    lines = Gitlines(id,year,mounth,day)
    # while True:
    lines.slovecontradiction()
