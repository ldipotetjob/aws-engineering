## How to add layers to a Python lambda function to connect with Postgres DB 

### Points to pay attention:

1. Python version
2. POSTGRES version
3. Environment (development/testing/production)

For environments like **development/testing** we have some guidance and a solution for **psycopg-binary**:

Directory structure pattern below:

```md
root_project
├── layers
│    └── psycopg2_layer 
        └── python
```

1. Move to **layers** folder(ref. structure above)

```shell
## have been tested 3.8/3.9/3.10/3.11
## this sample is running with 3.12 
 
version-slim=3.12 
docker run --name piplauncher --rm -ti \
--mount src="$(pwd)",target=/data,type=bind python:$version-slim \
pip install psycopg2-binary -t /data/psycopg2_layer/python
```

2. Generated dependencies after install psycopg2-binary in your upload_lambda_directory 

```md
├── ......
└── layers
    ├── psycopg2_layer
        ├── python
            ├── psycopg2
            ├── psycopg2_binary-2.9.10.dist-info
            └── psycopg2_binary.libs
 ```

3. The next step is to create the layer zipped files, psycopg2-module.zip in our example:

```shell
cd psycopg2_layer
zip -r psycopg2-module.zip python
```

The previous Layer can be upoladed to aws lambda layer by aws cli:

1. [Aws cli lambda layer](https://docs.aws.amazon.com/cli/latest/reference/lambda/publish-layer-version.html)
2. Aws console lambda service
