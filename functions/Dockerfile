FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /functions
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt
# Run the web service on container startup. Here we use the gunicorn

# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
EXPOSE 8080
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080", "--workers", "4", "--threads", "8", "--timeout", "0"]
