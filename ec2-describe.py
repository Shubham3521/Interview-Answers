import boto3
AWS_REGION = "us-east-2"
instance_id = input("Please Enter Instance ID:- ")
meta_data = input("Please select one parameters from these :- instanceType'|'kernel'|'ramdisk'|'userData'|'disableApiTermination'|'instanceInitiatedShutdownBehavior'|'rootDeviceName'|'blockDeviceMapping'|'productCodes'|'sourceDestCheck'|'groupSet'|'ebsOptimized'|'sriovNetSupport'|'enaSupport'|'enclaveOptions'|'disableApiStop  :- ")
ec2 = boto3.client('ec2', region_name=AWS_REGION)
response = ec2.describe_instance_attribute(
    Attribute=meta_data,
    InstanceId=instance_id,
)
print(response)
