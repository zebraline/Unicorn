#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-17
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def get_comment_list(marker_id, page=1, page_size=10):
    """获取评论列表"""
    start = (page - 1) * page_size
    sql = "select user_id, content, create_time, nickname, avatar_url from comment, user where comment.user_id = user.id and marker_id = %s limit %s, %s;"
    return db.query(sql, marker_id, start, page_size)

def add_comment(user_id, marker_id, content):
    """增加评论"""
    create_time = datetime.now()
    sql = "insert into comment (marker_id, user_id, content, create_time) values (%s, %s, %s, %s);"
    return db.execute(sql, marker_id, user_id, content, create_time)
