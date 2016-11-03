#!/bin/bash
set -e


# Define help message
show_help() {
    echo """
    Commands
    manage        : Invoke django manage.py commands
    setuplocaldb  : Create empty database for django-sisproject
    setupproddb   : Create empty database for production
    run_tests     : runs tests
    start         : start webserver behind nginx (prod for serving static files)
    """
}

setup_local_db() {
    set +e
    cd /code/
    python manage.py sqlcreate | psql -U $DB_USERNAME -h $DB_HOSTNAME
    set -e
    python manage.py migrate
}

setup_prod_db() {
    set +e
    cd /code/
    set -e
    python manage.py migrate
}

case "$1" in
    manage )
        cd /code/
        python manage.py "${@:2}"
    ;;
    setuplocaldb )
        setup_local_db
    ;;
    setupproddb )
        setup_prod_db
    ;;
    run_tests)
        cd /code/
        python manage.py test
    ;;
    start )
        cd /code/
        python manage.py collectstatic --noinput
        /usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf -n
    ;;
    bash )
        bash "${@:2}"
    ;;
    *)
        show_help
    ;;
esac
