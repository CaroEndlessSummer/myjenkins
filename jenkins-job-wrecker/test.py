__author__ = 'caro'
#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, unicode_literals, print_function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
    update_config()