#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 11:38
# @Author  : 冉勇
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# @desc    : 全局配置文件
import os
from pydantic import BaseSettings
from pathlib import Path
from typing import List

# 项目根目录 父一级再父一级再父一级 root根路径
base_dir = Path(__file__).absolute().parent.parent


class Settings(BaseSettings):
    # DEBUG模式
    debug: bool = True
    # 数据库—server
    MYSQL_HOST: str = None  # 数据库主机
    MYSQL_PORT: int = None  # 数据库端口
    MYSQL_USER: str = None  # 数据库用户名
    MYSQL_PWD: str = None  # 数据库密码
    DBNAME: str = None  # 数据库表名
    # sqlalchemy_server
    SQLALCHEMY_DATABASE_URI: str = ''
    # 项目标题
    project_title = "Sakura_Mini_Admin"
    # 项目描述
    project_description: str = """
#### Description/说明
<details>
<summary>点击展开/Click to expand</summary>
> [中文/Chinese]
- 🌸Mini后台管理，更多功能正在开发中。
- 本项目开源在[GitHub：Sakura_Mini_Admin](https://github.com/ranyong1997/Sakura_Mini_Admin)。
- 本项目仅供学习交流使用，严禁用于违法用途，如有侵权请联系作者。
</details>
#### Contact author/联系作者
<details>
<summary>点击展开/Click to expand</summary>
- WeChat: RanY_Luck
- Email: [ranyong1209@gmail.com](mailto:ranyong1209@gmail.com)
- Github: [✶  🎀  GitHub地址  🎀  ✶](https://github.com/ranyong1997)
</details>
"""
    # Tags数据
    tags_metadata = [
        {
            "name": "Casbin权限验证",
            "description": "",
        },
        {
            "name": "Casbin资源",
            "description": "",
        },
        {
            "name": "Casbin行为",
            "description": "",
        },
        {
            "name": "角色",
            "description": "角色相关操作，增删改查",
        },
        {
            "name": "系统登录",
            "description": "获取token",
        },
        {
            "name": "用户",
            "description": "用户相关操作，增删改查",
        },
    ]
    # 项目版本
    project_version: str = '0.0.3'
    # host
    server_host: str = "0.0.0.0"
    # port
    server_port: int = 5555
    # 配置允许域名
    # origins: List[str] = ["http://localhost", "http://localhost:5555", "http://127.0.0.1:5555", "http://127.0.0.1:5174"]
    # 所有域名可访问
    origins: List[str] = ["*"]
    # 配置允许访问方式
    cors_allow_methods: List[str] = ["PUT", "POST", "GET", "DELETE", "OPTIONS"]
    # 配置允许访问请求头
    cors_allow_headers: List[str] = ["*"]
    # url的前缀
    url_prefix: str = "/v1/token"
    # jwt加密的key >>>openssl rand -hex 32<<<
    jwt_secret_key: str = "c71336cfb4c32c0266ba636cf449e71e64e2c3cfe01728182cf5c3ddb33e357b"
    # jwt 加密算法
    jwt_algorithm: str = "HS256"
    # token过期时间，单位：秒
    jwt_exp_seconds: int = 7 * 24 * 60 * 60
    # 将当前目录添加到系统变量中
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))  # 当前项目路径
    LOG_PATH = os.path.join(BASE_DIR, '../logs')  # log_path为存放日志的路径
    BANNER: str = """
      ____        _                        __  __ _ _   _ _        _       _           _       
 / ___|  __ _| | ___   _ _ __ __ _    |  \/  (_) \ | (_)      / \   __| |_ __ ___ (_)_ __  
 \___ \ / _` | |/ / | | | '__/ _` |   | |\/| | |  \| | |     / _ \ / _` | '_ ` _ \| | '_ \ 
  ___) | (_| |   <| |_| | | | (_| |   | |  | | | |\  | |    / ___ \ (_| | | | | | | | | | |
 |____/ \__,_|_|\_\\__,_|_|  \__,_|___|_|  |_|_|_| \_|_|___/_/   \_\__,_|_| |_| |_|_|_| |_|
                                 |_____|              |_____|                                                                                                                                                                                                              
    """


class Dev_Config(Settings):
    # 开发者模式
    class Config:
        env_file = os.path.join(base_dir, "conf", "dev.env")


class Pro_Config(Settings):
    # 正式环境
    class Config:
        env_file = os.path.join(base_dir, "conf", "pro.env")


# 获取sakura_mini环境变量
Sakura_Mini_ENV = os.environ.get("sakura_mini_env", "dev")
# 如果sakura_mini存在且为pro
Config = Pro_Config() if Sakura_Mini_ENV and Sakura_Mini_ENV.lower() == "pro" else Dev_Config()
# 初始化 sqlalchemy（由 apscheduler 使用）
Config.SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{Config.MYSQL_USER}:{Config.MYSQL_PWD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{Config.DBNAME}'
