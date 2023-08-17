FROM python:3.8.10 AS builder

WORKDIR /app
COPY requirements.txt .

RUN python3 -m venv venv
RUN venv/bin/pip3 install --no-cache-dir -r requirements.txt
RUN echo "building..."

# NNI app
FROM python:3.8.10-slim

WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY ./NNI/NNI.py .
COPY ./NNI/bbox /app/bboxs


CMD ["venv/bin/python3", "NNI.py"]
