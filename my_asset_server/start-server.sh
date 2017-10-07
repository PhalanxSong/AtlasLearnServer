#!/bin/bash

# 任何语句的执行结果不是true则应该退出
# set -o errexit 或 set -e
set -e

logProgress () {
  echo "Start Server Log : $1 ======";
}

IMAGE_BASE_NAME="phalanx-asset-server"
RUN_PORT="8010:8010"
CONTAINER_NAME="phalanx-asset-server"

options=$(getopt -o o:t: --long old:,tag: -- "$@")
[ $? -eq 0 ] || {
  echo "Incorrect options provided"
  exit 1
}
eval set -- "$options"

while true; do
  case "$1" in
    --old)
      shift
      OLD_CONTAINER_ID=$1
      ;;
    --tag)
      shift
      TAG_NAME=$1
      IMAGE_NAME="$IMAGE_BASE_NAME:$TAG_NAME"
      ;;
    --)
      shift
      break
      ;;
  esac
  shift
done

[[ ! -z $TAG_NAME ]] || {
  echo "Missing tag name (use --tag or -t to set)"
  exit 1
}

logProgress "Begin build image of $IMAGE_NAME ...";

docker build -t "$IMAGE_NAME" .

logProgress "Finish build image ..."

if [[ ! -z $OLD_CONTAINER_ID ]]; then
  logProgress "Begin remove old container $OLD_CONTAINER_ID ..."
  docker stop "$OLD_CONTAINER_ID"
  docker rm "$OLD_CONTAINER_ID"
  logProgress "Finish remove old container ..."
fi

logProgress "Start new container ..."

docker run -v "/home/$IMAGE_BASE_NAME/uploads:/app/uploads" -p "$RUN_PORT" --link phalanx-server-mongo:mongo --name "$CONTAINER_NAME" --env-file ./env.list -d "$IMAGE_NAME" npm run start

logProgress "Start server success ..."
