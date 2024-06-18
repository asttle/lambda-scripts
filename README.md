# Useful lambda scripts

## 1. Unused EBS volumes
### Purpose - Cost optimisation
- This lambda will help until unused ebs volumes associated with your EC2 instances for more than 15 days. This will help us reduce cost.
### Steps:
- Create a lambda function
- Attach the iam policy in the folder to default IAM role created for lambda function.
- install dependencies from requirements.txt
- Compress the source code
- Upload the lambda function as zip
- Deploy the lambda function
- Create a test event and test the lambda function

  
![unused-ebs-volumes (1)](https://github.com/asttle/lambda-scripts/assets/64640283/cde6d9ee-38e5-4122-93d6-f9c2f4eb04ac)


## 2. Spot interruption handling notification in EKS cluster
### Purpose - Intimate developers of potential unavailability of nodes 
- This lambda will help developers know through their google chats or slack channels when a node which is of spot capacity type is interrupted and when new spot node is allocated in EKS cluster which uses Karpenter. This will also help denote time when particular services will be unavailable.

This architecture involves various components AWS fault injection service, Eventbridge, SNS topic apart from lambda. We only focus on lambda function feel free to explore and configure other services through AWS console.Attachinf necessary permissions and source and target for FIS with experiment templates and invoking experiments, Eventbridge rules with permissions source as ec2 spot instance interruption and allocation event patterns and destination and SNS topic, creation of SNS topic and lambda trigger source as SNS topic. I ghave given hints. Please explore and configure the rest. 

### Steps:
1. Create Lambda
2. Attach default amazon EC2 read access poolicy to default IAM role created for lambda function.
3. Start the FIS experiment
4. This will invoke spot interruption and eventbridge rule will capture and dispatch as SNS topic
5. SNS topic will trigger a lambda
6. Lambda will initimate user through webhook in appropriate chat or channel.

If you have placed cluster autoscaler using default cluster autoscaler provided by EKS or tools like Karpenter a new spot instance will be alocated based on availability. This can also be captured as part of eventbridge rule



![spot-interruption-lambda](https://github.com/asttle/lambda-scripts/assets/64640283/7c8a7a0e-4948-496e-b6ad-fa854be433c7)

