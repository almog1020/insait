FROM python:3.11.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

CMD [ "gunicorn", "insait.server:app", "-c", "insait/gunicorn_config.py" ]