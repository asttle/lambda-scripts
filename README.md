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
![unused-ebs-volumes](https://github.com/asttle/lambda-scripts/assets/64640283/50e287c0-a63c-49cd-b130-d69bc67944ed)

## 2. Spot interruption handling notification
### Purpose - Intimate developers of potential unavailability of nodes 
- This lambda will help developers know through their google chats or slack channels when a node which is of spot capacity type is interrupted and when new spot node is allocated. This will also help time when particular services will be unavailable. 
