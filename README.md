# Template for Django Project setup with Docker and Docker Compose

## Getting started

To get started, run a Docker build, as follows 

```sh
docker-compose build datacataglogue
```

Next, run the database

```sh
docker-compose up -d db
```

and then migrate the database

```sh
docker-compose run datacatalogue setuplocaldb
```

Finally, run the webserver

```sh
docker-compose up datacatalogue
```

and visit http://localhost:8000 in your browser.
