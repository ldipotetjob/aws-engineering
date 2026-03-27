import os
import boto3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='[%(levelname)s] %(module)s.%(funcName)s %(message)s')

def get_parameter(param_name: str):
    ssm = boto3.client('ssm')
    response_single_key = ssm.get_parameter(
    Name=param_name,
    WithDecryption=True  # For SecureString parameters
    )
    return response_single_key['Parameter']['Value']

def fetch_db_credentials():
    if is_running_on_lambda_environment():
        ssm = boto3.client('ssm')
        # Retrieve a multiple parameters
        response_multiple_keys = ssm.get_parameters(
            Names=['/userdb-rds-credentials/postgres-db-ipaddress', '/userdb-rds-credentials/postgres-db-password',
                   '/userdb-rds-credentials/postgres-db-name'],
            WithDecryption=True
        )
        params_decrypted = {param['Name']: param['Value'] for param in response_multiple_keys['Parameters']}
        db_hostname = params_decrypted['/userdb-rds-credentials/postgres-db-ipaddress']
        db_name = params_decrypted['/userdb-rds-credentials/postgres-db-name']
        db_password = params_decrypted['/userdb-rds-credentials/postgres-db-password']
        # Retrieve a single parameter
        response_single_key = ssm.get_parameter(
            Name='/userdb-rds-credentials/postgres-user',
            WithDecryption=True  # For SecureString parameters
        )
        db_username = response_single_key['Parameter']['Value']
    else:
        db_hostname = os.getenv("DB_IPADDRESS", default="localhost")
        db_username = os.getenv("DB_USER", default="user")
        db_password = os.getenv("DB_PASS", default="user")
        db_name = os.getenv("DB_NAME", default="userb")

    credential_dict = {'db_hostname': db_hostname,
                       'db_username': db_username,
                       'db_password': db_password,
                       'db_name': db_name}
    return credential_dict

def is_running_on_lambda_environment():
    # Lambda var ref:
    # https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime
    return os.getenv('AWS_EXECUTION_ENV') is not None

if __name__ == "__main__":
    # dev_file
    dev_file = "local_dev.py"
    try:
        with open(dev_file) as f:
            code = f.read()
            exec(code, globals())
    except FileNotFoundError:
        print(f'No {dev_file} file found. Skipping developer code.')