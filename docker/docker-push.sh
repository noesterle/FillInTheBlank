#!/bin/bash

LATEST=""
VERSION_NUM=""
ID=""
HELP=""
VERBOSE=3

while getopts "ln:i:hv" arg; do
	case $arg in
		l) LATEST=1;;
		n) VERSION_NUM=$OPTARG;;
		i) ID=$OPTARG;;
		h) HELP=1;;
		v) VERBOSE=6;;
	esac
done

Help()
{
   # Display Help
   echo "Tags and pushes versioned and/or latest Docker images based on input."
   echo
   echo "Syntax: docker-push.sh -i <image id> [-l] [-n <version_number>] [-h] [-v]"
   echo "options:"
   echo "i     Docker Image ID of the image to tag and push."
   echo "h     Print this Help."
   echo "l     Push the Docker Image to Dockerhub with the 'latest' tag."
   echo "n     Push the Docker Image to Dockerhub with a version number tag."
   echo "v     Verbose mode."
   echo
}

if [[ $HELP ]]; then
	Help
	exit 0
fi

# https://stackoverflow.com/a/33597663
declare -A LOG_LEVELS
# https://en.wikipedia.org/wiki/Syslog#Severity_level
LOG_LEVELS=([0]="emerg" [1]="alert" [2]="crit" [3]="err" [4]="warning" [5]="notice" [6]="info" [7]="debug")
log() {
  local LEVEL=${1}
  shift
  if [[ ${VERBOSE} -ge ${LEVEL} ]]; then
    echo "[${LOG_LEVELS[$LEVEL]}]" "$@"
  fi
}

if [[ ! $ID ]]; then
	log 3 "An image ID is required"
	OLD_VERBOSE=$VERBOSE
	VERBOSE=6
	log 6 "example: bash docker-push.sh -i e88"
	VERBOSE=$OLD_VERBOSE
	exit 1
fi

USERNAME="noesterle"
REPO_NAME="fillintheblank"

if [[ ! $VERSION_NUM && ! $LATEST  ]]; then
	OLD_VERBOSE=$VERBOSE
	VERBOSE=6
	log 6 "Add -n <version_number> to tag and push an image with that version."
	log 6 "Add -l to tag and push an image with the 'latest' tag."
	log 6 "Both -l and -n <version_number> can be used in the same command."
	VERBOSE=$OLD_VERBOSE
fi

if [[ $VERSION_NUM ]]; then
	log 6 "Tagginging image $ID to $USERNAME/$REPO_NAME:$VERSION_NUM"
	docker tag $ID $USERNAME"/"$REPO_NAME:$VERSION_NUM
	log 6 "Pushing image $ID to $USERNAME/$REPO_NAME:$VERSION_NUM"
	docker push $USERNAME"/"$REPO_NAME:$VERSION_NUM
fi

if [[ $LATEST ]]; then
	log 6 "Tagginging image $ID to $USERNAME/$REPO_NAME:latest"
	docker tag $ID $USERNAME"/"$REPO_NAME:latest
	log 6 "Pushing image $ID to $USERNAME/$REPO_NAME:latest"
	docker push $USERNAME"/"$REPO_NAME:latest
fi

