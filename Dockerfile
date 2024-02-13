FROM python:3.10-slim-buster  
  
WORKDIR /app  
  
COPY requirements.txt requirements.txt  
  
RUN python -m venv venv  
ENV PATH="/app/venv/bin:$PATH"  

RUN pip install --upgrade pip && \  
    pip install --no-cache-dir -r requirements.txt  
  
COPY . .

RUN chmod -R 777 translations  
  
CMD ["python3", "./run.py"]  
