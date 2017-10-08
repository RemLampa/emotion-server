# emotion-server

## Setup

  1. Install [Docker](https://docs.docker.com/engine/installation/).
  2. Execute via CLI:
  
  ```sh
  $ git clone https://github.com/ibleedfilm/emotion-server.git
  $ cd emotion-server
  $ sudo chmod u+x bootstrap.sh
  $ ./bootstrap.sh
  ```

## Starting/Stopping the server

  ```sh
  $ eval $(docker-machine env emotion-machine)
  $ docker start/stop/restart emotion-server
  ```

## Accessing the app
  `$ docker-machine ip emotion-machine`
  
  Take note of the ip address. You may access it via your browser or provide it in the client.