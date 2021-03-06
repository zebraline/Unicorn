#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from api.base import BaseHandler
import module.user_ctrl as user_ctrl
import module.marker_ctrl as marker_ctrl

class ListHandler(BaseHandler):
    """签到列表"""
    def get(self):
        user_filter_id = self.get_argument("u", 0) # u 表示 user_id
        page = self.get_argument("page", 1)
        page_size = self.get_argument("page_size", 200) # 先不做分页

        if user_filter_id > 0:
            marker_list = marker_ctrl.get_user_marker_list(int(user_filter_id), int(page), int(page_size))
        else:
            marker_list = marker_ctrl.get_marker_list(int(page), int(page_size))
        user_id = self.get_current_user()
        user_info = user_ctrl.get_user(user_id)
        self.render("marker_list.html", result={
            "marker_list": marker_list, 
            "user_id": user_id, 
            "user_filter_id": user_filter_id,
            "user_info": user_info
        })

class AddHandler(BaseHandler):
    """增加新签到"""
    @tornado.web.authenticated
    def get(self):
        return self.redirect("/marker/list")

    @tornado.web.authenticated
    def post(self):
        title = self.get_argument("title", "")
        marker = self.get_argument("marker", "")
        if not (title and marker):
            return self.render_string("标题和内容不能为空")
        user_id = self.get_current_user()
        marker_ctrl.add_marker(title, marker, user_id)
        return self.redirect("/marker/list")
