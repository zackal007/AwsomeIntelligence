# Git 配置指南

## 前提条件

确保您的系统已经安装了 Git。如果没有安装，请先安装 Git：

- **Windows**: 下载 [Git for Windows](https://git-scm.com/download/win)
- **macOS**: `brew install git` 或从 [git-scm.com](https://git-scm.com/download/mac) 下载
- **Linux**: `sudo apt install git` (Ubuntu/Debian) 或 `sudo yum install git` (CentOS/RHEL)

## 配置步骤

### 1. 初始化 Git 仓库

```bash
# 进入项目目录
cd path/to/your/project

# 初始化 Git 仓库
git init
```

### 2. 配置用户信息

```bash
# 设置用户名和邮箱（替换为您的实际信息）
git config --global user.name "zackal"
git config --global user.email "your-email@example.com"
```

### 3. 添加远程仓库

```bash
# 添加远程仓库地址
git remote add origin https://gitcode.com/zackal/AwesomeIntelligence.git
```

### 4. 提交代码

```bash
# 添加所有文件
git add .

# 进行首次提交
git commit -m "feat: initial commit - Apple-style website for Awesome Intelligence"

# 推送到远程仓库
git push -u origin main
```

## 如果远程仓库已存在内容

如果远程仓库已经有内容，您可能需要先拉取：

```bash
# 拉取远程仓库内容（如果有）
git pull origin main --allow-unrelated-histories

# 然后再推送
git push -u origin main
```

## 分支策略

建议使用以下分支策略：
- `main`: 主分支，包含生产就绪的代码
- `develop`: 开发分支，用于日常开发
- `feature/*`: 功能分支，用于新功能开发

## 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

## 示例工作流程

```bash
# 1. 克隆仓库（如果是新项目则跳过）
git clone https://gitcode.com/zackal/AwesomeIntelligence.git
cd AwesomeIntelligence

# 2. 创建开发分支
git checkout -b develop

# 3. 进行开发工作...

# 4. 提交更改
git add .
git commit -m "feat: add new feature description"

# 5. 推送到远程
git push origin develop

# 6. 创建Pull Request到main分支
```

## 故障排除

### 问题：权限被拒绝
**解决方案**: 
- 确保您有仓库的写权限
- 如果使用SSH，确保SSH密钥已正确配置
- 如果使用HTTPS，可能需要输入用户名和密码

### 问题：远程仓库非空
**解决方案**: 
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### 问题：行尾符警告
**解决方案**: 
```bash
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # macOS/Linux
```

---

完成以上步骤后，您的项目就会成功配置到 Git 仓库 `https://gitcode.com/zackal/AwesomeIntelligence.git` 中！