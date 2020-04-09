#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

if [ "${ENVTYPE:-}" == "dev" ]; then

    echo "detected ${ENVTYPE} environment..."
    pip install -e .

fi

# custom exports go here
# ----------------------

#if [ -z "${SOMEVAR:-}" ]; then
#    export SOMEVAR="FOO"
#fi

# custom functions (e.g. wait-for-postgres) goes here
# ---------------------------------------------------

#postgres_ready() {
#python << END
#import sys
#
#import psycopg2
#
#try:
#    psycopg2.connect(
#        dbname="${POSTGRES_DB}",
#        user="${POSTGRES_USER}",
#        password="${POSTGRES_PASSWORD}",
#        host="${POSTGRES_HOST}",
#        port="${POSTGRES_PORT}",
#    )
#except psycopg2.OperationalError:
#    sys.exit(-1)
#sys.exit(0)
#
#END
#}
#until postgres_ready; do
#  >&2 echo 'Waiting for PostgreSQL to become available...'
#  sleep 1
#done
#>&2 echo 'PostgreSQL is available'

exec "$@"
