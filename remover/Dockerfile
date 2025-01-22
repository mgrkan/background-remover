FROM python:3.11.2-slim
WORKDIR /app

RUN apt update && apt install ffmpeg libsm6 libxext6 python3-opencv libgl1-mesa-glx -y

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip \
  && pip3 install --no-cache-dir -r requirements.txt
ENV NUMBA_CACHE_DIR=/tmp

COPY src/ ./src
RUN mkdir images

RUN useradd app
RUN chown -R app:app /app
RUN chmod -R 777 /app
RUN mkdir /home/app
RUN chown -R app:app /home/app
RUN chmod -R 777 /home/app
USER app



CMD ["python", "src/worker.py"]