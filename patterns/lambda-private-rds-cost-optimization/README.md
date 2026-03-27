## How to access a public Lambda function without compromising security or high costs

This example demonstrates a Lambda function accessing a private RDS instance
without incurring NAT Gateway costs or VPC endpoint costs.


### Problem:
A common use case for using Secret Manager with Lambda includes:

* Storing database credentials that your function uses to connect to Amazon RDS or other databases

Parameter Store can be used freely by Lambda functions that are not attached to a VPC. However, when a Lambda function is deployed within a VPC (e.g., to access an RDS instance in a private subnet), it cannot access SSM Parameter Store by default.
Since it lives outside of the VPC and uses a public endpoint, accessing it from a Lambda function requires additional network configuration:

1. VPC endpoint
2. NAT Gateway

Although VPC endpoints are more cost-effective than a NAT Gateway, they are not free and can become a nightmare depending on their use.

### Solution:
Here we present a totally free solution (neither option 1 nor 2) that is secure at the same time:

Lambda_function_outside_of_VPC => access to parameter store => Lambda_function_outside_of_VPC(parameter_from_parameter_store) => Lambda_function_in_VPC 

### Architecture: 

* ref: architecture-access-public-lambda.jpeg