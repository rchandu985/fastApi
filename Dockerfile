FROM python:3.11.4
COPY api_app.py /app/
COPY bands.py /app/
COPY next_process_trigger.py /app/ 
COPY layer_stack_dates.json /app/
WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
EXPOSE 7000
CMD ["/bin/sh", "-c", "$FASTAPI_COMMAND"]

