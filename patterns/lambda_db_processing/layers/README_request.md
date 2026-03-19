## How to add layers to a Python lambda function to use the Requests module: 

```md
root_project
├── layers
│    └──request_layer 
        └── python
```

1. Move to **layers** folder(ref. structure above)

```shell
## have been tested 3.8/3.9/3.10/3.11
## this sample is running with 3.12 
 
version-slim=3.12 
docker run --name piplauncher --rm -ti \
--mount src="$(pwd)",target=/data,type=bind python:$version-slim \
pip install requests -t /data/request_layer/python
```

2. Generated dependencies after install psycopg2-binary in your upload_lambda_directory 

```md
├── ......
└── layers
    ├── request_layer
        ├── python
            ├── bin
            ├── certifi
            ├── certifi-2024.8.30.dist-info
            ├── charset_normalizer
            ├── charset_normalizer-3.4.0.dist-info
            ├── idna
            ├── idna-3.10.dist-info
            ├── requests           
            ├── requests-2.32.3.dist-info
            ├── urllib3
            └── urllib3-2.2.3.dist-info
 ```

3. The next step is to create the layer zipped files, requests-module.zip in our example:

```shell
cd request_layer
zip -r requests-module.zip.zip python
```

The previous Layer can be upoladed to aws lambda layer by aws cli:

1. [Aws cli lambda layer](https://docs.aws.amazon.com/cli/latest/reference/lambda/publish-layer-version.html)
2. Aws console lambda service
