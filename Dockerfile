FROM ubuntu
MAINTAINER cammann.tom@gmail.com
RUN apt-get update && apt-get install -y --no-install-recommends python-pip git python-dev build-essential
RUN useradd foosball
RUN mkdir -p /home/foosball/foosball && chown foosball:foosball /home/foosball/foosball

ADD foosball /home/foosball/foosball/foosball/
ADD run.py /home/foosball/foosball/
ADD db /home/foosball/foosball/db
ADD requirements.txt /home/foosball/foosball/

RUN pip install -r /home/foosball/foosball/requirements.txt
RUN mkdir -p /var/log/foosball/ && chown foosball:foosball /var/log/foosball
USER foosball

WORKDIR /home/foosball/foosball
ENTRYPOINT ["/home/foosball/foosball/run.py"]
CMD ["-d", "-c"]
EXPOSE 8080
