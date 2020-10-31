FROM python:3

ADD src/my_script.py /

RUN pip install pystrich

CMD [ "python", "./my_script.py" ]