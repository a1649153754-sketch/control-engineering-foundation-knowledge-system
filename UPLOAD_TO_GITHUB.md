# 上传到 GitHub

默认仓库名：

```text
control-engineering-foundation-knowledge-system
```

## 推荐流程

1. 在 GitHub 创建空仓库，或让脚本创建。
2. 不要提前添加 README、`.gitignore` 或 License；项目中已经包含。
3. Windows 双击 `UPLOAD_TO_GITHUB.cmd`。
4. 在官方浏览器页面完成 `gh auth login`，不要把密码或 Token 粘贴到聊天。
5. 上传后进入 `Settings → Pages`，将 Source 设为 `GitHub Actions`。

## 手动命令

```bash
git init
git add .
git commit -m "feat: publish control engineering foundation knowledge system v1.0.0"
git branch -M main
git remote add origin https://github.com/a1649153754-sketch/control-engineering-foundation-knowledge-system.git
git push -u origin main
```

预计 Pages 地址：

```text
https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/
```
