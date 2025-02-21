task1: The script collects user inputs for AMI, instance type, region, availability zone,
 and Load Balancer name. It stores these inputs, uses Jinja2 to create a dynamic template, and prints the final configuration with the user's selections.

task2: This script uses Jinja2 to create a Terraform configuration file. 
It defines AMI and instance type options, sets default values for region, availability zone, and Load Balancer name, and maps them to a Terraform template. The template includes resources like an EC2 instance, Load Balancer, and VPC. 
The script renders the template with the provided values, prints the output, and saves it to a main.tf file for deployment.   

task3: This script automates Terraform commands using the python_terraform library. It first runs terraform init to set up the environment
, then terraform plan to preview changes, and finally terraform apply to deploy the infrastructure. If any step fails, it prints the error and stops. After successful deployment, 
it retrieves and displays the Terraform outputs, such as the EC2 instance ID and Load Balancer DNS name, to confirm the setup.  

task4: This script uses Boto3 to check AWS resources. It fetches details about an EC2 instance (state and public IP) and an Application Load Balancer (DNS name).
 If successful, it saves the data to a JSON file (aws_validation.json). If any step fails, it prints an error and stops. The script verifies that the EC2 instance and ALB are properly deployed.