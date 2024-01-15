FROM python:3.11-slim

# Add HEALTHCHECK instruction
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD curl -f http://localhost:5000/ || exit 1
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/src

EXPOSE 5000
#Flask Environment Variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development

CMD ["flask", "run"]

# create user
RUN adduser -D donkey
USER donkey
