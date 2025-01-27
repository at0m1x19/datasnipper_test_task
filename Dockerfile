FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN python -m playwright install chromium --with-deps

COPY . .

CMD ["pytest", "tests", "-v"]