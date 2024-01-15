FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN rm requirements.txt
WORKDIR /app/src

EXPOSE 5000
#Flask Environment Variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development

CMD ["flask", "run"];