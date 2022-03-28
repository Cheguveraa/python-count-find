
from sys import stderr
import paramiko
import sys, time
import json
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.108.228.72',username='raju',password='Blueblue@123',port=22)
stdin, stdout, stderr= ssh.exec_command('vmstat')
print("Output of the command is")
print(stdout.readlines())

----------------------------------------------
import sys 
import paramiko
import os 
import time 
import json
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="",username="", password="", port="")
stdin, stdout, stderr=ssh.exec_command('vmstat')
print(f"Output of {stdout} is")
print(stdout.readlines())
                                       


