from python_terraform import Terraform
import os

def run_terraform():
  
    tf = Terraform(working_dir=os.getcwd())
    
   
    print("Running terraform init...")
    return_code, stdout, stderr = tf.init()
    if return_code != 0:
        print("Error during terraform init:")
        print(stderr)
        return
   
    print("Running terraform plan...")
    return_code, stdout, stderr = tf.plan()
    if return_code != 0:
        print("Error during terraform plan:")
        print(stderr)
        return
    
    
    print("Running terraform apply...")
    return_code, stdout, stderr = tf.apply(skip_plan=True, capture_output=True)
    if return_code != 0:
        print("Error during terraform apply:")
        print(stderr)
        return
    

    outputs = tf.output()
    instance_id = outputs['instance_id']['value']
    lb_dns_name = outputs['lb_dns_name']['value']
    
    print("\nTerraform Outputs:")
    print(f"Instance ID: {instance_id}")
    print(f"Load Balancer DNS Name: {lb_dns_name}")

if __name__ == "__main__":
    run_terraform()