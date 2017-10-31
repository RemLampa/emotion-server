#!/usr/bin/env bash

if ! [ -d ${PWD}/src ]
then
    echo Directory not found: ${PWD}/src
elif ! [ -d ${PWD}/config ]
then
    echo Directory not found: ${PWD}/config
else
  docker-machine create --driver virtualbox emotion-machine

  docker-machine stop emotion-machine

  echo Adding src to VM sharedfolder...
  VBoxManage sharedfolder add emotion-machine --automount --name "src" --hostpath ${PWD}/src

  docker-machine start emotion-machine

  echo Mounting src folder...
  docker-machine ssh emotion-machine 'sudo mkdir --parents /mnt/src'
  docker-machine ssh emotion-machine 'sudo mount -t vboxsf src /mnt/src'

  echo Creating Docker image...
  eval $(docker-machine env emotion-machine)
  docker build -t emotion:latest .

  echo Creating Docker container...
  docker run -it -d --restart=always -p 80:80 --name emotion-server -v /mnt/src:/src emotion:latest
fi