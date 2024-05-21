FROM python:3.12.3-alpine
RUN mkdir /bible_channel
WORKDIR /bible_channel
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]