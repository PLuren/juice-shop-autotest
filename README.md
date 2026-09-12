# Juice Shop 接口自动化测试项目

基于 Python + requests + pytest 的接口自动化测试练习项目，被测系统为本地 OWASP Juice Shop。

## 技术栈

- Python 3.12
- requests
- pytest
- python-dotenv
- pytest-html

## 项目结构

```text
api/      接口层，封装请求
common/   公共请求、日志和统一断言
data/     测试数据
test_*.py 测试用例