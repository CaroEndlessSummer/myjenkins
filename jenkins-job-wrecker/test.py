# encoding: utf-8
__author__ = 'caro'
#!/usr/bin/env python

# from __future__ import absolute_import, unicode_literals, print_function
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import os

cur_path = os.path.split(__file__)[0]
is_test = True

def get_config():
    if is_test:
        # getcmds = r'set JJW_USERNAME=admin&& set JJW_PASSWORD=admin&& jjwrecker -s http://10.10.82.200:8080'
        getcmds = r'set JJW_USERNAME=zhaogenyuan&& set JJW_PASSWORD=zhaosen0&& jjwrecker -s http://10.10.82.226:8080'
    else:
        getcmds = r'set JJW_USERNAME=zhaogenyuan&& set JJW_PASSWORD=zhaosen0&& jjwrecker -s http://10.10.82.226:8080'

    print('yes')
    os.system(getcmds)

def commit_config():
    workspace = os.path.join(cur_path, 'output')
    cmds = r'svn svn commit -m "update configs"'
    os.system(cmds)

def update_config():
    if is_test:
        cmds = r'jenkins-jobs --conf D:\em\scripts_zgy\py2\jenkins\test_jenkins_jobs.ini update output\CRM_trunk_sonar.yml'
    else:
        cmds = r'jenkins-jobs --conf D:\em\scripts_zgy\py2\jenkins\jenkins_jobs.ini update output'

    os.system(cmds)

if __name__ == '__main__':
    # get_config()
    # commit_config()
    # update_config()
    # --conf  D:\github\myjenkins\jenkins-job-builder\jenkins_jobs.ini update D:\github\myjenkins\jenkins-job-wrecker\jenkins_job_wrecker\output\test.yml test2
    u = unicode('\u6d4b\u8bd5', 'unicode_escape')
    print(u)
    # f = open(r'D:\github\myjenkins\jenkins-job-wrecker\jenkins_job_wrecker\output\test4.yml', 'r')
    # st = f.read()
    # print(type(st))
    mse = u'测试'
    print(type(mse))
    print(mse)
    # print(mse.decode('utf-8').encode('unicode_escape'))

    m = '测试'
    print(type(m))
    print(m.decode('utf-8').encode('unicode_escape'))
    # print(m.decode('utf-8').encode('unicode_escape'))
    # f = open('text.txt', 'w')
    # f.write(m)
    # f.write(m.decode('utf-8').encode('unicode_escape'))
    # # f.close()
    m = open(r'D:\github\myjenkins\jenkins-job-wrecker\jenkins_job_wrecker\output\test4.yml', 'r')
    n = m.read()
    for line in n.decode('utf-8'):
        print(line)
        # print(line.decode('gbk').encode('unicode_escape'))
    # print(type(n))
    # l = unicode(n, 'unicode_escape')
    # print(l)