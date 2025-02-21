import boto3
import json


region_name = 'us-east-1' 
ec2_client = boto3.client('ec2', region_name=region_name)
elb_client = boto3.client('elbv2', region_name=region_name)

def fetch_instance_details(instance_id):
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        
        instance_state = instance['State']['Name']
        public_ip = instance.get('PublicIpAddress', 'N/A')  
        
        return {
            'instance_id': instance_id,
            'instance_state': instance_state,
            'public_ip': public_ip
        }
    except Exception as e:
        print(f"Error fetching instance details: {e}")
        return None

def fetch_alb_details(load_balancer_name):
    try:
        response = elb_client.describe_load_balancers(Names=[load_balancer_name])
        alb = response['LoadBalancers'][0]
        
        alb_dns = alb['DNSName']
        
        return {
            'load_balancer_dns': alb_dns
        }
    except Exception as e:
        print(f"Error fetching ALB details: {e}")
        return None

def save_to_json(data, filename='aws_validation.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def main():

    instance_id = "i-0123456789abcdef0"  
    load_balancer_name = "my-application-lb"  
    
    
    instance_details = fetch_instance_details(instance_id)
    if not instance_details:
        return
    
    
    alb_details = fetch_alb_details(load_balancer_name)
    if not alb_details:
        return
    
    
    validation_data = {
        **instance_details,
        **alb_details
    }
    
    
    save_to_json(validation_data)

if __name__ == "__main__":
    main()