FROM tiangolo/meinheld-gunicorn-flask:python3.7

ENV VIRTUAL_ENV=~/.pyenvs/echoes_calculator
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt .

RUN pip install -r requirements.txt


COPY ./ /app

