# FastAPiDome

最近比较火，就试着用 FastAPi+Gino+MySql搞了个dome,做个参考吧

### 项目结构

```
FastAPiDome-master
├─ README.md
├─ alembic
│    ├─ README
│    ├─ env.py
│    ├─ script.py.mako
│    └─ versions
│           ├─ 0a220b1ed311_修改说明11.py
│           ├─ 5a5ca20e7fd1_提交说明.py
│           ├─ 5fa961ca272c_修改说明11.py
│           ├─ __pycache__
│           ├─ b366a8494641_add_user_id.py
│           ├─ b60b676c2ca2_posts.py
│           └─ c0488b41feec_posts.py
├─ alembic.ini
├─ app
│    ├─ __init__.py
│    ├─ api
│    │    ├─ __init__.py
│    │    ├─ __pycache__
│    │    ├─ admin
│    │    └─ v1
│    ├─ core
│    │    ├─ __init__.py
│    │    ├─ curd_base.py
│    │    ├─ curd_redis.py
│    │    ├─ deps.py
│    │    ├─ jwt.py
│    │    ├─ responses.py
│    │    └─ security.py
│    ├─ exts
│    │    ├─ __init__.py
│    │    ├─ mgino.py
│    │    └─ mredis.py
│    ├─ models
│    │    ├─ __init__.py
│    │    ├─ base.py
│    │    ├─ posts.py
│    │    └─ user.py
│    ├─ run.py
│    ├─ schemas
│    │    ├─ __init__.py
│    │    ├─ common.py
│    │    ├─ token.py
│    │    └─ user.py
│    ├─ setting
│    │    ├─ __init__.py
│    │    └─ base.py
│    └─ utils
│           ├─ __init__.py
│           ├─ __pycache__
│           ├─ exceptions.py
│           ├─ logging.py
│           └─ tools.py
└─ requirements.txt
```
### 安装

 - `pip install -r requirements.txt`
### 启动
 - 直接运行`run.py`

### 表结构初始化与更新
```
alembic revision --autogenerate -m "修改说明"
alembic upgrade head
```