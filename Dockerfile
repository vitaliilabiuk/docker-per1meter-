FROM python:3.9.1

ADD ./app /app

ADD ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

# This variables will be used in ./gunicorn.sh
ENV FLASK_APP=perimeter
ENV FLASK_DEBUG=true
EXPOSE 5000

ENTRYPOINT ["gunicorn", "perimeter:app", "-w 2", "-b 0.0.0.0:5000"]