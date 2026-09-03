# 贡献指南

提交补充或纠错前请遵守：

1. 不上传教材、习题解、原题或答案全文。
2. 新内容必须挂接稳定节点，并写明触发信号、主路线、条件和失效边界。
3. 旧编号不改；新增 `Q/B/D/E/J-C` 编号按序追加。
4. 软件结果必须注明单位、版本相关差异和验证方式。
5. 运行：

```bash
python scripts/validate_project.py
python scripts/build_bundle.py
zensical build --clean --strict
```

Pull Request 中说明修改模块、来源边界、验证方式和是否影响编号/规模。
