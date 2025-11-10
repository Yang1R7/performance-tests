FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install termcolor
CMD ["python", "docker_example.py"]