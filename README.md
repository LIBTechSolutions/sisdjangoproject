# Template for Django Project setup with Docker and Docker Compose

## Getting started

To get started, run a Docker build, as follows 

```sh
docker-compose build sisproject
```

Next, run the database

```sh
docker-compose up -d db
```

and then migrate the database

```sh
docker-compose run sisproject setuplocaldb
```

Finally, run the webserver

```sh
docker-compose up sisproject
```

and visit http://localhost:8000 in your browser.
