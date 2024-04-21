# 使用Python作为基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . /app

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露所使用的端口
EXPOSE 8000

# 启动Flask应用程序
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
