ROLE_ARN=$(ROLE)
ZIP_FILE=deployment-package.zip
REGION=$(AWS_REGION)

# keep in mind your security tokens export in your terminal:
# export AWS_ACCESS_KEY_ID=${token_access_key}
# export AWS_SECRET_ACCESS_KEY=${token_secret_key}

# @see: https://makefiletutorial.com/
# example of use(when just ONE makefile):  make all HANDLER=db_repository ROLE=arn:aws:iam::${ACCOUNT_ID}:role/execution-role
# example of use(when just +ONE makefile, specify the file): make all HANDLER=${MY_LAMBDA_FUNC_NAME}

FUNCTION_NAME=$(HANDLER)
all: help build deploy clean

help:
	echo "deploying " $(HANDLER)

build:
	mkdir -p deployment-package
	# cp -r src/$(HANDLER)/. deployment-package/
	rsync -av --exclude='__pycache__/' --exclude='venv/' --exclude="/local_dev.py" --exclude="/README.md" src/$(HANDLER)/ deployment-package/
	if [ -f requirements.txt ]; then pip install -r requirements.txt --target deployment-package/; fi
	cd deployment-package && zip -r9 ../$(ZIP_FILE) .

deploy:
	echo "Deploying lambda function:" $(HANDLER)
	aws lambda update-function-code --function-name $(FUNCTION_NAME) --zip-file fileb://$(ZIP_FILE) --region $(REGION)

clean:
	rm -rf deployment-package $(ZIP_FILE)
