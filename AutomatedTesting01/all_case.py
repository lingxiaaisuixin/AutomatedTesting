# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@name:
@description:运行测试案例，并发送执行测试报告到邮箱
"""
import smtplib
from email.mime.text import MIMEText
import unittest
import HTMLTestRunner
import time,os
from email.mime.multipart import MIMEMultipart
from email.header import Header
import json
from testcase import super_class
#=============定义QQ企业邮箱发送邮件==========
def sendEmail(file_new):
    sender="xxxx"
    receiver="xxxx"
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    send_content=MIMEMultipart()
    #传输的html文本
    message = MIMEText(mail_body, 'html', 'utf-8')
    #传输的附件
    file_new = file_new[28:]
    file=MIMEText(mail_body,'base64','utf-8')
    file["Content-Type"] = 'application/octet-stream'
    file["Content-Disposition"] = 'attachment; filename='+file_new
    send_content.attach(message)
    send_content.attach(file)
    send_content['From'] = Header('xx', 'utf-8')
    send_content['To'] = Header('xx', 'utf-8')
    send_content['Subject'] = Header('xxxx'+time.strftime("%Y_%m_%d_%H_%M_%S"), 'utf-8')
    # smtpObj = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
    smtpObj=smtplib.SMTP_SSL(host='smtp.exmail.qq.com',port=465)
    smtpObj.login(sender, 'xxxxx')
    smtpObj.sendmail(sender, receiver, send_content.as_string())
    smtpObj.close()
    print("邮件发送成功")
# ======查找测试报告目录找到最新生成的测试报告文件==
def send_report(testreport):
    result_dir = testreport
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    #print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print(file_new)
    #调用发邮件模块
    sendEmail(file_new)
#================将用例添加到测试套件===========
def creatsuite():
    testunit=unittest.TestSuite()
    loader=unittest.TestLoader()
    #读取案例
    with open("config/case_to_run.json","r") as f:
        run_cases=json.loads(f.read())
    print(run_cases)
    for run_case in run_cases :
        testunit.addTests(loader.loadTestsFromName("testcase."+run_case))
    print(testunit)
    return testunit
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    testreport = '.\\report\\'
    filename = testreport+now+'result.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'自动化测试报告',
    description=u'用例执行情况：')
    alltestnames = creatsuite()
    runner.run(alltestnames)
    # unittest.TextTestRunner(verbosity=2).run(alltestnames)
    fp.close() #关闭生成的报告
    send_report(testreport) #发送报告
