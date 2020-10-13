#!/bin/bash

echo `hostname -I | sed 's/\:/ /'|awk '{print $1}'`
