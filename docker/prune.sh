#!/usr/bin/env bash

docker system prune -f
#docker image prune -a --filter "until=6h" --force
#docker container prune --force --filter "until=6h"
#docker volume prune --force --filter "label!=keep"
