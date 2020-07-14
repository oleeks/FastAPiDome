# FastAPiDome

FastAPi+Gino+MySql

### 安装

 - 安装FastApi 
   `pip install FastApi[all]`
 - 安装支持mysql的gino模块 
   `pip install git+https://github.com/wwwjfy/gino.git@mysql-support`

### 项目结构

```
fastapi_dome
├─ __init__.py
├─ app
│    ├─ __init__.py
│    ├─ api
│    │    ├─ __init__.py
│    │    └─ user.py
│    ├─ config
│    │    ├─ __init__.py
│    │    ├─ base.py
│    │    └─ db_config.py
│    ├─ core
│    │    ├─ __init__.py
│    │    └─ mgino.py
│    ├─ exts.py
│    ├─ models
│    │    ├─ __init__.py
│    │    ├─ db
│    │    │    ├─ __init__.py
│    │    │    ├─ base.py
│    │    │    └─ user.py
│    │    └─ schemas
│    │           ├─ __init__.py
│    │           └─ user.py
│    ├─ run.py
│    └─ utils
│           ├─ __init__.py
│           └─ tools.py
└─ requirements.txt
```
