FROM python:3.12

# ENV
ENV port 5000

# py 기본 디렉토리
# requiremnet, main install 
WORKDIR /usr/src/app
COPY ./requirements.txt ./
COPY ./main ./
# --no-cache-dir : cache 방지
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $port

CMD ["python", "./app.py"]