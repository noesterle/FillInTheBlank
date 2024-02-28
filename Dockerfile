FROM python:3.10.13-slim-bookworm

WORKDIR /FillInTheBlank

COPY quiz/ ./quiz/
COPY Pipfile .
COPY Pipfile.lock .

RUN apt update && apt upgrade && apt install -y git
RUN python -m pip install pipenv

RUN pipenv sync

EXPOSE 5000/TCP

CMD [ "pipenv", "run", "flask", "--app", "quiz", "run", "--debug", "--host=0.0.0.0"]
