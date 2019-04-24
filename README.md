# Lambda function using python3.7

This lambda function just stop and start ec2 instances on aws.

# IAM Policy
Use lambda-function.json for grant lambda access to exec stop, start and describe on ec2 instances.

# Tag Instances 
Tag your instances with tag-key: Shutdown and value wih: True
