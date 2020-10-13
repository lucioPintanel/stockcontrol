#!/bin/bash
echo Criando variavel de ambiente
export FLASK_APP="run.py"
echo "Varivel FLASK_APP foi setada com : $FLASK_APP"

flask run -h $(./__ipAddd.sh)
