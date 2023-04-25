FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED=1

ADD . /oclettings-docker/

WORKDIR /oclettings-docker

COPY requirements.txt .

RUN  pip install --upgrade pip \
&& pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "oc_lettings_site.wsgi"]