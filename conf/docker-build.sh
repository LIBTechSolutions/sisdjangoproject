#!/bin/bash
set -e
set -x

TAG=$TRAVIS_TAG
COMMIT=$TRAVIS_COMMIT
BRANCH=$TRAVIS_BRANCH
PR=$TRAVIS_PULL_REQUEST

echo $TAG
echo $BRANCH
echo $PR
export TAG

if [ -z $TAG ]
then
    echo "No tags, tagging as: $COMMIT"
    TAG=$COMMIT
fi

# if this is on the master/dev branch and is not a PR, deploy it
# if [ $PR = "false" ] && [ $BRANCH = "development" -o $BRANCH = "master" -o $BRANCH = "staging" ];
if [ $BRANCH = "master" -o $PR = "feature/chris/deploy-to-elastic-beanstalk" ];
then
  aws ecr get-login --region eu-west-1 | bash

  docker tag liberiasisproject_sisproject:latest $DOCKER_IMAGE_REPO/$DOCKER_IMAGE_NAME:$TAG 
  docker push $DOCKER_IMAGE_REPO/$DOCKER_IMAGE_NAME:$TAG

  case "$BRANCH" in
    "master")
      envsubst < conf/Dockerrun.aws.json.tmpl > conf/Dockerrun.aws.json
      envsubst < conf/supervisor.sisproject.conf.tmpl > conf/supervisor.sisproject.conf

      zip -j conf/deploy.zip conf/Dockerrun.aws.json
      zip -j conf/deploy.zip conf/supervisor.sisproject.conf
      zip -j conf/deploy.zip conf/nginx.sisproject.conf
      zip -j conf/deploy.zip conf/nginx-users
      zip -j conf/deploy.zip conf/get_env_name.py
      zip -ur conf/deploy.zip .ebextensions/
      eb deploy liberia-sis-project-dev -l $TAG
    ;;
    *)
    echo "cannot find environment for $BRANCH"
  esac
fi
