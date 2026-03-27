from dataclasses import dataclass

import psycopg2
import logging
import http

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='[%(levelname)s] %(module)s.%(funcName)s %(message)s')

@dataclass
class User:
    user_id: str
    user_name: str
    sex_male: bool

@dataclass
class Connections:
    db_hostname: str
    db_username: str
    db_password: str
    db_port: int
    db_name: str

    def get_connection(self):
        conn = psycopg2.connect(host=self.db_hostname, user=self.db_username,
                                password=self.db_password, port=self.db_port, dbname=self.db_name)
        return conn

def get_any_query(query, connection):
    # ref: https://www.psycopg.org/docs/usage.html#with-statement
    with connection.cursor() as cur:
        cur.execute(query)
        # (list of tuples) ref: https://www.psycopg.org/docs/cursor.html#cursor.fetchall
        query_result=cur.fetchall()
    return query_result

class UserRepository(Connections):

    def add(self, usr: User):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO user (userid, username, is_male) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """,  (usr.user_id, usr.user_name, usr.sex_male))
                logger.info(f'[f.UserRepository.add] register added. userid: {usr.user_id}, user_name:{usr.user_name}')
            conn.commit()
        return {
            'statusCode': http.HTTPStatus.OK,
            'message': {
                'userid': usr.user_id,
                'username': usr.user_name
            }
        }

    def delete(self, usr: User):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                DELETE FROM user WHERE userid = %s """,
                            usr.user_id)
                record_modified = cur.rowcount
            conn.commit()

        if record_modified > 0:
            logger.info(
                f'[f.UserRepository.delete] register deleted. userid: {usr.user_id}')
            response = {'statusCode': http.HTTPStatus.NO_CONTENT}
        else:
            response = {'statusCode': http.HTTPStatus.NOT_FOUND,
                        'message': {'errorCode': "REQUEST_NOT_FOUND",
                                    'userid': usr.user_id
                                    }
                        }
        return response

    def edit(self, user_id: str, updates: dict):
        # https://docs.python.org/3/library/stdtypes.html#str.join
        allowed_columns = ['username', 'is_male']  # adjust as needed

        for column_name in updates.keys():
            if column_name not in allowed_columns:
                raise ValueError(f"Invalid column name: {column_name}")

        # Build SET clause dynamically, e.g., "col1 = %s, col2 = %s"
        set_clause = ", ".join([f"{col} = %s" for col in updates.keys()])
        edited_fields = ", ".join([f"{col}"for col in updates.keys()])
        values = list(updates.values())

        conn = self.get_connection()
        with conn.cursor() as cur:
            query = f"""
            UPDATE User
            SET {set_clause}
            WHERE userid = %s
            """
            cur.execute(query, (*values, user_id))
            records_modified = cur.rowcount
            logger.info(
                f'[f.UserRepository.edit] register modified:  {records_modified}. userid: {user_id} ')
            conn.commit()

        if records_modified == 1:
            r = {
            'statusCode': http.HTTPStatus.OK,
            'message': {'userid': user_id,
                        'edited_fields': edited_fields}
            }
        else:
            r = {'statusCode': http.HTTPStatus.INTERNAL_SERVER_ERROR,
                        'message': {'errorCode': "INTERNAL_SERVER_ERROR",
                                    'errorMessage': f"The operation failed trying to edit the following fields: {edited_fields},try MANUALLY",
                                    'userid': user_id
                                    }
                        }

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