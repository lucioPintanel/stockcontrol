#!/bin/bash

	case $1 in
		INIT)
			rm -fr migrations/ app/main/*.db

			flask db init
			flask db migrate --message '$2'
			flask db upgrade
		;;
			
		UP)
			flask db migrate --message '$2'
			flask db upgrade
		;;
			
		*)
			echo "Sorry, I don't understand"
		;;
	esac
