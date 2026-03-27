import json
import logging
import boto3
import system_managers_param_store as manage_credentials

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    action = event['crud_action']
    data_dict = event['data_dict']
    response = lambda_call_db_in_vpc(action, data_dict)
    return response

def lambda_call_db_in_vpc(action, data_dict):
    lambda_client = boto3.client('lambda')
    credential_dict = manage_credentials.fetch_db_credentials()
    r = lambda_client.invoke(
        FunctionName='lambda_private_rds_cost_optimization_in_vpc',
        InvocationType='RequestResponse',
        Payload=json.dumps({'action': action, 'user_table_fields': data_dict,
                            'credential': credential_dict}))
    return r

if __name__ == "__main__":
    # dev_file
    dev_file = "local_dev.py"
    try:
        with open(dev_file) as f:
            code = f.read()
            exec(code, globals())
    except FileNotFoundError:
        print(f'No {dev_file} file found. Skipping developer code.')