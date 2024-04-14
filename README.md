![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.


# Docker Set-Up

To run the web app, first makle sure you have docker installed and setup on your computer.

1. Set up the docker networks for the apps

```bash
docker network create mynetwork
```

2. Set up the docker container for the ml app


You need to build the ml client first

```bash
docker build -t ml_app .
```

Then you have to run it on the network with a very specific name: 'goofy_austin'

```bash
docker run -p 5001:5001 --network=mynetwork --name goofy_austin -d ml_app
```

It should result in a running container


3. Set up the docker container for the web app


You need to build the ml client first

```bash
docker build -t web_app .  
```

Then you have to run it on the network

```bash
docker run --env-file .env -p 5000:5000 --network=mynetwork -d web_app
```

It should result in a running container



4. Set up the docker container for the mongodb app

You have to run it on the network with a specific name: mongo_container

```bash
docker run -d --network mynetwork --name mongo_container mongo:latest                                         
```

It should result in a running container


# Usage

After everything is set up you can now run the web app and it should be connected with your other apps. If you have docker-desktop, you can click on the container and a link to the flask app should appear. The default link should be this: http://127.0.0.1:5000

Navigate to the 'submit melody' tab. You should then upload your audio file and submit it. Then wait a moment and you should be prompted that the upload is sucessful.

To get an analysis of the last uploaded file, navigate to the 'see your melody' tab. The results of your analysis will be here.

# Contributors
[Neal Haulsey](https://github.com/nhaulsey)

[Denzel Prudent](https://github.com/denprud)

[Rakshit Sridhar](https://github.com/RakSridhar23)

[Babamayokun Okudero](https://github.com/Mokudero)




