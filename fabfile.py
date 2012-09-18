from fabric.api import local, settings, abort, run, cd, env

env.hosts = ['ubuntu@ec2-75-101-210-85.compute-1.amazonaws.com:22']

#config.project_name = 'deploytest'
#
## environments
#
#def awsbox():
#    "Use the local virtual server"
#    config.hosts = ['awsbox']
#    config.path = '/home/ubuntu/'
#    config.user = 'ubuntu'
#    config.virtualhost_path = "/"
#
#
#def test():
#    require('hosts', provided_by=[awsbox])
#    require('path')


def hello():
    print("Hello world!")
    run("whoami")
