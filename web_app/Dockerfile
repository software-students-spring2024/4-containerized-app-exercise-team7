FROM python:3

WORKDIR /machine-learning-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "test_app.py" ]