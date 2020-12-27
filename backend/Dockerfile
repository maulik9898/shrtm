FROM python:3.9

RUN pip install pipenv
# Setting an environment variable with the directory
# where we will be running the app
ENV APP /app

# Creating a directory and instructing Docker to work on this from now on
RUN mkdir $APP
WORKDIR $APP

# Exposing the port for Gunicorn
EXPOSE 5000

COPY Pipfile* ./



# Copying requirements to the APP directory in order to install the required libs

# Install Python dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Copying rest of the code to WORKDIR
COPY . .

# Finally, run the app with Gunicorn command
CMD [ "gunicorn", "-c", "gunicorn.conf.py", "wsgi:app" ]
