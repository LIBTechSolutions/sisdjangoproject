#!/bin/bash
set -e


# Define help message
show_help() {
    echo """
    Commands
    manage        : Invoke django manage.py commands
    setuplocaldb  : Create empty database for django-datacatalogue
    setupproddb   : Create empty database for production
    test_coverage : runs tests with coverage output
    start         : start webserver behind nginx (prod for serving static files)
    """
}

setup_local_db() {
    set +e
    cd /code/datacatalogue/
    /var/env/bin/python manage.py sqlcreate | psql -U $DB_USERNAME -h $DB_HOSTNAME
    set -e
    /var/env/bin/python manage.py migrate
}

setup_prod_db() {
    set +e
    cd /code/datacatalogue/
    set -e
    /var/env/bin/python manage.py migrate
}

case "$1" in
    manage )
        cd /code/datacatalogue/
        /var/env/bin/python manage.py "${@:2}"
    ;;
    setuplocaldb )
        setup_local_db
    ;;
    setupproddb )
        setup_prod_db
    ;;
    test_coverage)
        source /var/env/bin/activate
        coverage run --rcfile="/code/.coveragerc" /code/manage.py test core
        mkdir /var/annotated
        coverage annotate --rcfile="/code/.coveragerc"
        coverage report --rcfile="/code/.coveragerc"
        cat << "EOF"
  ____                 _     _       _     _
 / ___| ___   ___   __| |   (_) ___ | |__ | |
| |  _ / _ \ / _ \ / _` |   | |/ _ \| '_ \| |
| |_| | (_) | (_) | (_| |   | | (_) | |_) |_|
 \____|\___/ \___/ \__,_|  _/ |\___/|_.__/(_)
                          |__/

EOF
    ;;
    start )
        cd /code/datacatalogue/
        /var/env/bin/python manage.py collectstatic --noinput
        /usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf
        nginx -g "daemon off;"
    ;;
    bash )
        bash "${@:2}"
    ;;
    *)
        show_help
    ;;
esac
