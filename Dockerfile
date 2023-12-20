FROM circleci/python:3.10.0
USER root
WORKDIR /apps

COPY ./ /apps/
ADD ./requirements.txt ./requirements.txt
RUN  pip3 install -i https://mirrors.aliyun.com/pypi/simple -r ./requirements.txt

RUN chmod +x ./start.sh

EXPOSE 8080

CMD ["./start.sh"]
