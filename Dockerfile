FROM python:3.9
LABEL author="Nejc Petkoski"
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py"]