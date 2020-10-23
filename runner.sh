#!/bin/bash
echo "Criando variavel de ambiente"
export FLASK_APP="manage.py"
export FLASK_ENV="development"
export FLASK_DEBUG=1
export FLASK_RUN_PORT=8000

echo "Varivel FLASK_APP foi setada com : $FLASK_APP"

flask run #-h $(./__ipAddd.sh)
