
### mypy
- python从3.5开始支持类型注解，但是python不会自动检查类型，执行类型错误的代码不会报错。
- mypy是python类型检查工具。

#### 安装
```
1. pip install mypy
2. poetry add --group dev mypy

```

#### 配置
- pyproject.toml中添加
```
[tool.mypy]
python_version = "3.13"  # 根据项目实际情况调整
strict = true  # 启用严格类型检查
exclude = ["tests"]
```
- 使用单独的mypy.ini文件

#### 使用
- mypy直接执行文件
- 配置在pyproject.toml中
```
[tool.poetry.scripts]
mypy = "mypy ."
```

#### vscode支持

settings.json
```
{
  "python.pythonPath": "/path/to/your/poetry/env/bin/python",  // 自动推断或手动设置
  "python.linting.mypyEnabled": true,
  "python.linting.enabled": true,
  "python.analysis.typeCheckingMode": "off"  // 关闭 Pyright，避免与 MyPy 冲突
}

python.pythonPath用 poetry env info --path 获取或者不填写

```
保存配置后reload vscode