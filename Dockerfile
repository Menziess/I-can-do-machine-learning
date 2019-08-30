FROM python:3.6

WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app

RUN pip install -U setuptools pip
RUN pip install pipenv
RUN apt-get -y update && apt-get -y install unixodbc-dev
RUN pipenv install --system --deploy
COPY dist/* /app
COPY res/ /app/res/
COPY src/models/ /app/src/models/

RUN pip install ./*.whl
RUN rm /app/*.whl

CMD python -m training_sklearn.app
