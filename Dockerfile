FROM python:3.8.5-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./ /app


CMD [ "uvicorn", "main:app", "--host","0.0.0.0", "--reload", "--port","8000" ]

#SUPER RUN
#ENTRYPOINT /user/local/bin/gunicorn \
#    -b 0.0.0.0:80 \
#    -w 4 \
#    -k uvicorn.workers.UvicornWorkers main:app \
#    --chdir /app \
#    --access-logfile "${ACCESS_LOG}" \
#    --error-logfile "${ERROR_LOG}"
