#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author by jacksyen[hyqiu.syen@gmail.com]
---------------------------------------
全局变量存储
"""
import os

class Global:

    GLOBAL_DB_FILE = 'gk7-douban-read-send-kindle.db'

    ## 书籍信息表
    GLOBAL_DB_TBL_BOOK_NAME = 'gk7_douban_books'

    ## 书籍图片路径表
    GLOBAL_DB_TBL_BOOK_IMG_NAME = 'gk7_douban_book_img'

    ## 全局配置表
    GLOBAL_DB_TBL_GLOBAL_NAME = 'gk7_douban_global'

    ## 等待发送邮件表
    GLOBAL_DB_TBL_WAIT_EMAILS_NAME = 'gk7_douban_wait_emails'

    ## 书籍html等待转换表
    GLOBAL_DB_TBL_WAIT_HTMLS = 'gk7_douban_wait_htmls'

    GLOBAL_DATA_DIRS = '%s/data' %(os.path.abspath('.'))

    GLOBAL_OUT_DATA_DIRS = '%s/out-data' %(os.path.abspath('.'))

    # 输出文件格式
    GLOBAL_OUT_FILE_FORMAT = 'mobi'

    # 书籍路径表分割字符
    GLOBAL_DB_BOOK_IMG_PATH_SPLIT = ';'

    GLOBAL_BOOK_PAGE_SPLIT = 'pagebreak'

    ## email配置
    GLOBAL_EMAIL_SMTP = 'smtp.gmail.com'

    GLOBAL_EMAIL_SMTP_PORT = '25'

    GLOBAL_EMAIL_USER = 'hyqiu.syen@gmail.com'

    GLOBAL_EMAIL_PWD = '' # TODO email密码

    GLOBAL_EMAIL_ENCODE = 'utf-8'

    def __init__(self):
        pass

'''
全局状态
+ 邮件表
+ htmls转换表
'''
class Global_Status:

    WAIT = 'wait'

    COMPLETE = 'complete'

    ERROR = 'error'


'''
全局日志配置
'''
class global_logs:

    LOG_DIRS = '%s/logs' %(os.path.abspath('.'))

class GlobalThread:

    POOL_NUMBER = 4

