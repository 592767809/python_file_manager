# 使用的基本镜像
FROM python:3.12.8
# 进入目录
WORKDIR /root
# 拉取项目源码
RUN git clone https://github.com/592767809/python_file_manager.git
WORKDIR /root/python_file_manager
# 启动源码
RUN python -m pip install --upgrade pip
RUN pip install django
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
ARG SU_USERNAME
ARG SU_EMAIL
ARG SU_PASSWORD
ENV DJANGO_SUPERUSER_USERNAME=$SU_USERNAME
ENV DJANGO_SUPERUSER_EMAIL=$SU_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD=$SU_PASSWORD
RUN python manage.py createsuperuser --noinput
# 导出端口
EXPOSE 80
# 指定运行时的启动指令
CMD python manage.py runserver 0.0.0.0:80
