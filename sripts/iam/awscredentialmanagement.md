
## Different ways to create credential provider in AWS

### Getting credentials from Environment Vars

#### Creating ENVIRONMENT VARIABLES 

```shell
export AWS_ACCESS_KEY=<paste your access key>
export AWS_SECRET_KEY=<paste your secret key>
```

#### Creating IAM CLIENT from ENV VARs

```python
import os

iam = boto3.client('iam',
                   aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                   aws_secret_access_key = os.environ.get('AWS_SECRET_KEY'),
                   region_name="eu-west-1")
```

=============================================================================
### Getting credentials from AWS Config File

Your configs file must reside in your local machine:</br>

1. ~/.aws/config 
2. ~/.aws/credentials

* File content

```
# file:
# ~/.aws/config

AWS Access Key ID [**************];
AWS Secret Access Key [************];
Default region name [my_region_name];
Default output format [Json]
```
 
```
# file:
# ~/.aws/credentials

[default]
aws_access_key_id=<your_access_key_id>;
aws_secret_access_key=<your_secret_access_key>;
```

#### Creating CLIENT from AWS config file from local machine 

```python

s3_client = boto3.client('s3',
aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
region_name=REGION_NAME
)

```


