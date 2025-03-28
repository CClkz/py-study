# Python 学习与实践项目


## 升级python版本


## 更换镜像源
### windows
```
打开配置文件
pip config edit --editor notepad

写入以下内容
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn

临时使用
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

镜像源
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：https://mirrors.aliyun.com/pypi/simple
豆瓣：https://pypi.douban.com/simple
华为云：https://repo.huaweicloud.com/repository/pypi/simple

```

## 依赖管理

### 使用poetry创建pyproject.toml
python >= 3.10
```
1. 安装poetry
pip install poetry

2. 初始化、生成pyproject.toml
poetry init

3. 安装依赖
poetry install numpy

4. 依赖加到配置文件
poetry add numpy
```
