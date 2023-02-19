FROM python:3.7-slim AS base

WORKDIR /usr/src/app
RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install libmagic-dev libxml2

FROM base AS env

COPY Pipfile* ./
RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install build-essential && \
    python -m venv .venv && \
    export PATH="/.venv/bin:$PATH" && \
    pip install pipenv && \
    pipenv install --deploy --ignore-pipfile && \
    apt-get -y remove build-essential && apt-get clean

FROM base AS runtime

COPY --from=env /usr/src/app/.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# args
ARG TELEGRAM_API_TOKEN

# envs
ENV TELEGRAM_API_TOKEN=${TELEGRAM_API_TOKEN}

EXPOSE 8080
EXPOSE 3306
COPY telegram_bot ./telegram_bot
ENTRYPOINT python -m telegram_bot.app
