FROM python:3.10-slim

WORKDIR /app

# 1) copy & install Python dependencies
COPY ./api/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 2) copy your app code
COPY . .

# 3) default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
