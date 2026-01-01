#!/bin/sh
docker build . -t admin-panel
docker container rm -f admin-panel
docker run --rm --name admin-panel -p 80:80 admin-panel