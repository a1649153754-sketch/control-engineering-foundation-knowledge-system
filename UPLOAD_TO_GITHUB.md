# Windows 一键同步到 GitHub

双击 `UPLOAD_TO_GITHUB.cmd`。脚本会通过 GitHub CLI 的官方网页授权完成同步，不需要把密码、Token、验证码或 SSH 私钥写入文件。

## 它会做什么

1. 检查 `git` 与 `gh`；
2. 读取 `VERSION`，识别当前发布版本；
3. 登录 GitHub 并识别当前账号；
4. 若仓库不存在，询问公开/私有后创建；
5. 若仓库已存在，先抓取 `main` 历史，再把当前解压目录作为新版本工作树；
6. 运行项目校验、单文件构建和再次校验；
7. 提交并推送到 `main`，触发 GitHub Pages 自动部署。

## 使用前提

- Windows 10/11；
- 已安装 Git；
- 已安装 GitHub CLI；
- 解压后的目录结构完整；
- 当前账号对目标仓库有写入权限。

运行时会显示账号、仓库和版本，只有输入 `YES` 才会提交。已有仓库不会被重新创建；脚本会保留 Git 历史，并把包内缺失的旧文件视为删除。

目标仓库：

```text
control-engineering-foundation-knowledge-system
```
