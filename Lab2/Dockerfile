
FROM python:3.11-slim

WORKDIR /Illarionov_3_11

COPY translator_app.py .

RUN pip install googletrans==3.1.0a0

ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

CMD ["python", "translator_app.py"]