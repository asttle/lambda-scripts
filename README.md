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


## 2. Spot interruption handling notification
### Purpose - Intimate developers of potential unavailability of nodes 
- This lambda will help developers know through their google chats or slack channels when a node which is of spot capacity type is interrupted and when new spot node is allocated. This will also help time when particular services will be unavailable. 
