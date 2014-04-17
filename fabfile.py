# -*- coding: latin-1 -*-
"""
Basic fab file for deploying to EC2
➜ fab deploy
"""

from __future__ import with_statement
from contextlib import contextmanager as _contextmanager
from fabric.api import *
from fabric.colors import *

# from theartling.local_settings import PEM_KEY_DIR
PEM_KEY_DIR = '/Users/redapesolutions/Downloads/theartling.pem'

env.user = 'ubuntu'
# Staging
env.hosts = ['54.251.247.163']
# env.hosts = []
# Production
# env.hosts.append('54.251.39.22')

env.key_filename = PEM_KEY_DIR
env.forward_agent = True
env.directory = '/home/ubuntu/theartling'
env.activate = 'source /home/ubuntu/theartling_env/bin/activate'

@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield

def git_reset(where):
    with cd('%s' % env.directory):
        run('git reset --hard %s' % where)

def git_pull(branch):
    with cd('%s' % env.directory):
        run("git checkout %s" % branch)
        run("git pull --no-edit origin %s" % branch)

def git_create(branch):
    with cd('%s' % env.directory):
        run("git checkout -b %s" % branch)

def install_requirements():
    with cd('%s' % env.directory):
        run('pip install -r requirements.txt')

def migrate():
    with cd('%s' % env.directory):
        run('python manage.py migrate')

def collectstatic():
    with cd('%s' % env.directory):
        run('python manage.py collectstatic --noinput')

def supervisor_restart_all():
    sudo('supervisorctl restart all')

def restart_nginx():
    sudo('service nginx restart')

def deploy():
    print(cyan('➜   Connected to The Artling instance....'))
    with virtualenv():
        # git_pull('PaypalDev')
        # git_create('Books')
        git_pull('Books')
        # install_requirements()
        # git_reset('2c9232b')
        # migrate()
        collectstatic()
        supervisor_restart_all()
        restart_nginx()
    print(green('\n➜  Deployment succesful! kthnxbye'))
