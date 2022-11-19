FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install pip --upgrade
RUN pip install -U -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]