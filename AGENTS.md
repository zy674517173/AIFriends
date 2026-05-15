# 项目智能总结

## 项目简介

AIFriends 是一个基于 Django 后端和 Vue3 + Vite 前端的全栈项目，旨在实现用户注册、登录、信息管理等基础社交功能。

---

## 主要技术栈

- **后端**：
  - Django 6
  - Django REST Framework
  - SimpleJWT（JWT 认证）
  - CORS Headers
  - Sqlite3
- **前端**：
  - Vue 3
  - Vite
  - Pinia（状态管理）
  - Axios（HTTP 请求）
  - TailwindCSS + DaisyUI（UI 框架）

---

## 目录结构

- backend/
  - Django 项目与 web 应用，包含用户模型、视图、API 路由、静态与媒体文件管理
- frontend/
  - Vue3 + Vite 前端工程，包含页面、组件、路由、状态管理、API 封装

---

## 核心功能

- 用户注册、登录、登出、信息获取、Token 刷新
- JWT 认证，Access/Refresh Token 管理，支持 Cookie 存储
- 用户信息（头像、简介等）管理
- 前后端分离，支持跨域
- 前端页面包括主页、好友、创建、用户空间、个人资料、登录/注册等

---

## 运行方式

### 后端
1. 进入 backend 目录，安装依赖：
   ```sh
   pip install -r requirements.txt
   ```
2. 启动 Django 服务：
   ```sh
   python manage.py runserver
   ```

### 前端
1. 进入 frontend 目录，安装依赖：
   ```sh
   npm install
   ```
2. 启动开发服务器：
   ```sh
   npm run dev
   ```

---

## 其他说明

- 支持本地开发与调试，生产环境需关闭 DEBUG 并配置 ALLOWED_HOSTS。
- 详细功能与接口可参考源码及注释。

---

> 本 AGENTS.md 文件由 Copilot 智能生成，适用于快速了解和协作本项目。
