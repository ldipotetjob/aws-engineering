AWS Lambda Directory structure pattern below:

```md
your-lambda-project/
├── packages/               # (Optional) Lambda dependencies (for Layers)    
│   ├── package_for-library-1  
│   └── package_for-library-n 
│ 
├── src/                     # Main source code for Lambda functions
│   ├── lambda_function_name_1/  
│   │      ├── lambda_function.py # Entry point for Lambda Function  (for Python)
│   │      ├── lambda_function_utility_file_1.py # utility function_1 for Lambda Function
│   │      └── lambda_function_utility_file_n.py # utility function_n for Lambda Function
│   │
│   ├── lambda_function_name_n/
│   │      ├── lambda_function.py # Entry point for Lambda Function  (for Python)
│   │      ├── lambda_function_utility_file_1.py # utility function_1 for Lambda Function
│   │      └── lambda_function_utility_file_n.py # utility function_n for Lambda Function
│   ├── standard_utils-1.py  # (Optional) Helper module for all lambda functions (for Python)
│   │
│   └── standard_utils-n.py  # (Optional) Helper module for all lambda functions (for Python)
│ 
├── tests/                   # Unit tests
│   └── test_handler.py
│ 
├── requirements.txt         # Python dependencies
│ 
├── resources/ 
│   └──  template.yaml       # AWS SAM template (or serverless.yml for Serverless Framework)
├── README.md               # Project documentation
├── makefile                # Build/deploy automation
└── .gitignore              # Git ignore rules
```
