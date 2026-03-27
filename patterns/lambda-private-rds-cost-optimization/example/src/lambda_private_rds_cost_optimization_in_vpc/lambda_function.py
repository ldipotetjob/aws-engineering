import logging
import db
import http

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    # not implemented handle exception
    # all dictionary key access by key-based access to force exception in case of key error
    action = event['crud_action']
    credential_db = event["credential"]
    db_hostname = credential_db['db_hostname']
    db_name = credential_db['db_name']
    db_password = credential_db['db_password']
    db_username = credential_db['db_username']
    user_table_fields = event["user_table_fields"]

    r = lambda_db(action, db_hostname, db_name, db_password, db_username, user_table_fields)
    return r

def lambda_db(action, db_hostname, db_name, db_password, db_username, user_columns):
    response = {'statusCode': "NO_STATUS"}
    match action:
        case "add":
            user_object = (db.
                              User(user_columns['user_id'],
                                            user_columns['user_name'],
                                            user_columns['sex_male'])
                              )
            logger.info(f"Adding User: {user_object}")
            response = db.UserRepository(db_hostname, db_username, db_password, 5432, db_name).add(user_object)

        case "delete":
            user_object = (db.
                           User(user_columns['user_id'],
                                user_columns['user_name'],
                                user_columns['sex_male'])
                           )
            logger.info(f"Delete User: {user_object}")
            response = db.UserRepository(db_hostname, db_username, db_password, 5432, db_name).delete(user_object)
        case "edit":

           # can be modified both (username and is_male) or one of the fields
           # columns_to_update = {"username": "any_value", "is_male": boolean_value}
           columns_to_update = user_columns['columns_to_update']
           logger.info(f"Edit/update User: {user_columns['user_id']}")
           response = (db.UserRepository(db_hostname, db_username, db_password, 5432, db_name).
                      edit(user_columns['user_id'], columns_to_update))
        case _:
            # rise error
            pass
    return response

# for test from IDE
if __name__ == "__main__":
    # dev_file
    dev_file = "local_dev.py"
    try:
        with open(dev_file) as f:
            code = f.read()
            exec(code, globals())
    except FileNotFoundError:
        print(f'No {dev_file} file found. Skipping developer code.')