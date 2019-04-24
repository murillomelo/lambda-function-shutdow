import boto3


def lambda_handler(event, context):
    region = 'sa-east-1'

    resource = boto3.resource('ec2')
    client = boto3.client('ec2', region_name=region)

    for instance in resource.instances.filter(Filters=[{'Name': 'tag:Shutdown', 'Values': ['True']}]):
        resultado = instance.id
        client.start_instances(InstanceIds=[str(resultado)])
        print('Start Instance: ' + str(resultado))
