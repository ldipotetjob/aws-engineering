# Access private RDS from Lambda without NAT Gateway or VPC endpoint costs

## Problem

When a Lambda function is deployed inside a VPC (e.g., to access a private RDS instance),
it loses direct access to public AWS services such as SSM Parameter Store or Secrets Manager.

To access these services, you typically need:

1. A NAT Gateway
2. A VPC Endpoint

Although VPC endpoints are more cost-effective than a NAT Gateway, they are not free and can still introduce additional 
cost and operational overhead. 

## Solution

This pattern avoids both NAT Gateway and VPC endpoint costs by splitting responsibilities
between two Lambda functions:

- A **public Lambda (outside VPC)** retrieves configuration (e.g., from Parameter Store)
- A **private Lambda (inside VPC)** handles database access

### Flow:

1. Public Lambda retrieves secrets/configuration from Parameter Store
2. Public Lambda invokes private Lambda
3. Private Lambda accesses RDS using the provided configuration

Public Lambda (no VPC)
↓
Parameter Store (public endpoint)
↓
Public Lambda
↓ invoke
Private Lambda (inside VPC)
↓
Private RDS

## Architecture

@see: lambda-private-rds-cost-optimization.png 

## Benefits

* No NAT Gateway cost
* No VPC endpoint cost
* Keeps RDS private
* Simple network configuration

## Trade-offs

* More complexity (2 lambdas instead of 1)
* added latency becauseLambda-to-Lambda invocation 

## When to use this pattern

### Use this approach when:

* Lambda must access a private RDS instance
* You want to avoid NAT Gateway costs
* You want to avoid managing VPC endpoints

### When NOT to use

Avoid this approach when:

* Simplicity is more important than cost
* You already rely heavily on VPC endpoints
* Security constraints forbid passing secrets between services

