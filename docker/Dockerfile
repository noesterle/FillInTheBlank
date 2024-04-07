FROM python:3.10.13-slim-bookworm

WORKDIR /FillInTheBlank

COPY quiz/ ./quiz/
COPY Pipfile .
COPY Pipfile.lock .

RUN apt update && apt upgrade -y && apt install -y git
RUN python -m pip install pipenv

RUN pipenv sync

EXPOSE 8080/TCP

CMD [ "pipenv", "run", "waitress-serve", "--call", "quiz:create_app" ]
