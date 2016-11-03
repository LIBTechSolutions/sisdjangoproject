FROM ubuntu:14.04

ENV TERM screen-256color

RUN locale-gen --no-purge en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

ADD conf/apt-packages.txt /tmp/apt-packages.txt
RUN apt-get update -qq && cat /tmp/apt-packages.txt | xargs apt-get --yes --force-yes install

RUN apt-get install -y wget
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main 9.4" > /etc/apt/sources.list.d/pgdg.list

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /var/log/sisproject

ADD conf/entrypoint.sh /usr/local/bin/entrypoint.sh 
RUN chmod +x /usr/local/bin/entrypoint.sh

RUN mkdir -p /etc/supervisor/conf.d && mkdir -p /var/log/supervisor

ADD conf/supervisord.conf /etc/supervisor/supervisord.conf

ADD conf/nginx.sisproject.conf /etc/nginx/sites-enabled/default

RUN mkdir -p /var/www/static && chmod -R 760 /var/www/static/ && chown -R www-data:www-data /var/www/static

WORKDIR /code/

COPY sisproject/ /code/

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]
CMD ["start"]
