## Lambda accessing private RDS can incur NAT Gateway or VPC Endpoint cost

This example demonstrates a Lambda function accessing a private RDS instance
without incurring in NAT Gateway or VPC Endpoint costs.

### Prerequisites

To make  easy this example we assume that :
1. a psycopg2-layer is installed for python veesion >= 3.11 ref in this repo: psycopg2-layer
2. two lambda function skeleton(${Function_name}) with runtime >= 3.11 exist in your AWS Lambda in your ${AWS_REGION}
3. a postgres database exists in your ${AWS_REGION}

### Details:

**lambda_private_rds_cost_optimization_in_vpc**: lambda function in VPC that can access to RDS \
**lambda_private_rds_cost_optimization_not_in_vpc**: lambda function in public network(Non VPC) that 
acts as a wrapper to invoke lambda_private_rds_cost_optimization_in_vpc 

**local_dev.py:** local file where you can add your script to test in local

ref psycopg2-layer: https://github.com/kvssankar/aws-lambda-psycopg2