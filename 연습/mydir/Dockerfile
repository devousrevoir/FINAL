FROM python:3.9.16
COPY . /mydir
WORKDIR /mydir
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt
CMD ["uwsgi", "uwsgi.ini"]