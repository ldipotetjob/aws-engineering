# Lambda Private RDS Cost Optimization - Example Deployment
This example assumes existing infrastructure and focuses only on the application and networking pattern.

This example focuses on architecture and cost optimization patterns, not infrastructure provisioning and targets engineers familiar 
with AWS networking and Lambda internals.
It demonstrates how a Lambda function can access a private RDS instance without introducing additional networking costs such as NAT Gateway or VPC Interface Endpoints.

The pattern uses a **public Lambda as a wrapper** to invoke a **VPC-isolated Lambda**, which then connects securely to a private RDS database.

## Prerequisites

- AWS Account
- AWS CLI configured
- Python 3.11+
- Iam policy that allows to create/update lambda functions

## Assumptions

To keep the example focused on the pattern, the following resources must already exist:

### Lambda functions
Two AWS Lambda empty functions (runtime >= Python 3.11) must already exist:
- lambda_private_rds_cost_optimization_in_vpc
- lambda_private_rds_cost_optimization_not_in_vpc

### Networking

- `lambda_private_rds_cost_optimization_in_vpc`:
    - Deployed inside a VPC
    - Attached to private subnets
    - Security group allows access to RDS

- `lambda_private_rds_cost_optimization_not_in_vpc`:
    - Must NOT be attached to a VPC

### Database

- A PostgresSQL RDS instance must already exist in `${AWS_REGION}`
- Must be reachable from the VPC Lambda

### Lambda Layer

- A `psycopg2` layer must be available  
  Reference: https://github.com/kvssankar/aws-lambda-psycopg2

##  Components

### `lambda_private_rds_cost_optimization_in_vpc`
- Runs inside a VPC
- Connects directly to RDS
- Executes SQL queries

### `lambda_private_rds_cost_optimization_not_in_vpc`
- Runs outside the VPC (public Lambda)
- Acts as a wrapper / entry point
- Invokes the VPC Lambda

### `local_dev.py`
- Local testing script
- Used to simulate Lambda logic outside AWS

## Execution Flow

1. Client invokes the public Lambda
2. Public Lambda invokes the private Lambda
3. Private Lambda connects to RDS
4. Query result is returned back through the chain

##  Configuration


### AWS Credentials

Export credentials in your terminal:

```bash
export AWS_ACCESS_KEY_ID=${token_access_key}
export AWS_SECRET_ACCESS_KEY=${token_secret_key}
```

## Deploy/Update lambda functions 

```bash
make all HANDLER=<lambda_name> 
```
Where <lambda_name> is one of:

lambda_private_rds_cost_optimization_in_vpc
lambda_private_rds_cost_optimization_not_in_vpc

## IAM Policies 

Required IAM policies are provided in this repository.

They allow:

* Lambda-to-Lambda invocation
* Access to AWS Systems Manager Parameter Store

## Database Requirements

This example assumes an existing PostgresSQL table:

```sql
CREATE TABLE users (
userid SERIAL PRIMARY KEY,
username TEXT,
is_male boolean,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

## Architecture

This example implements the pattern described here:
../README.md

## Test 

Use the provided test events:

* event_add.json
* event_update.json
