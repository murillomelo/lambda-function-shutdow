# Lambda function using python3.7

This lambda function just stop and start ec2 instances on aws.

# IAM Policy
Use lambda-function.json for grant lambda access to exec stop, start and describe on ec2 instances.

# Tag Instances 
Tag your instances with tag-key: Shutdown and value wih: True

# Adjuste var region with region of your resources

# Schedule
schedule your functions in cloudwatch rules, example:
50 10 ? * MON-FRI * - This execution will take place at 10:50 on weekdays. with this method your resources will shutdown on weekend.
