
```shell
version=3.11 
docker run --name piplauncher --rm -ti \
--mount src="$(pwd)",target=/data,type=bind python:$version-slim \
pip install requests -t /data/requests_module_upload_directory
```
