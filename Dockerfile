FROM python:3.8.5

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip3 install pipenv
RUN pipenv install --system

CMD ["python", "velog_back/manage.py", "runserver", "0.0.0.0:8000"]