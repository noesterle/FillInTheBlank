echo $2
if [[ $# -ne 1 ]]; then
	echo "Requires one arguement, the tag or id of the image to run"
	echo "example: bash docker-run.sh e88"
	exit 1
fi

docker run -d -p 8080:8080 -t $1
