# emotion-server

## Setup

  #### Provide your IBM Watson Natural Language Understanding Credentials
  1. `$ cp src/modules/emotion/credentials.sample.py src/modules/emotion/credentials.py`
  2. Edit [credentials.py](/src/modules/emotion/credentials.py).

  #### Build the server
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
  
## Running tests

  ```sh
  $ pip install pytest pytest-cov
  $ py.test -v --cov=src
  ```
