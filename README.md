# Web项目简介

## 项目名称
基于django的用户博客

## 项目概述
该项目是一个基于Django框架的用户博客系统，允许用户注册、创建个人资料并上传头像。系统使用Django的内置用户模型，并扩展了用户资料功能。
允许用户创建发表贴文，并对自己的贴文进行删除与编辑。

## 功能特性
- 用户注册：用户可以通过填写用户名和密码进行注册。
- 贴文发布与管理：用户可以发布贴文，并对自己的贴文进行管理
- 用户资料管理：用户可以更新个人资料，包括头像和性别。

## 技术栈
- **后端**: Django(Python 3.12.4)
- **数据库**: SQLite
- **前端**: HTML, CSS, JavaScript（可选）

## 安装与运行
1. 克隆项目：
   ```bash
   git clone https://github.com/heyuzhao1/django_blog.git
   cd my_project
   ```

2. 创建虚拟环境并激活：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 .\.venv\Scripts\Activate.ps1
   ```

3. 框架版本：
   django 5.1.1

4. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```

5. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

6. 访问应用：
   打开浏览器并访问 `http://127.0.0.1:8000/`


7.创建管理员账户：
```bash
  python manage.py createsuperuser
```
## 交流学习
欢迎任何形式的贡献！请提交问题或拉取请求，自用学习项目，请多指教。

