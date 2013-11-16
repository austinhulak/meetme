FROM ubuntu:quantal
MAINTAINER Roberto Aguilar roberto@baremetal.io

RUN apt-get update
RUN apt-get install -y git libpq-dev python-dev python-pip


# Just add the requirements.txt file because adding the entire project will
# likely introduce other changes that then bust the cache
ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt


# Now add the entire application
ADD . /app/


# Customize the container environment

# This will allow these ports to be exposed when run via vanilla `docker run`
EXPOSE 8000

ENV HOME /app

# These *_PORT environment variables give the ports names and will allow istari
# to orchestrate between services across servers.
# these ports will be exposed regardless if the EXPOSE command above is used
ENV SERVICE_PORT 8000

# The service name provided by this container.  When orchestrated across other
# containers the ports above will be prefixed with this name; for example:
# SERVICES__MEETME__SERVICE_PORT=8000
ENV SERVICE meetme


# The default command to run
CMD gunicorn_django /app/baseline/settings.py -b 0.0.0.0:8000
