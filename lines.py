import subprocess
a = subprocess.check_output('git log --author=wb-lz525541@alibaba-inc.com --since=1month.ago | wc -l',shell=True).decode(encoding='gbk')
print(a)