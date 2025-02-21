import jinja2


def get_ami():
    print("Select AMI:")
    print("1. Ubuntu (ami-0dee1ac7107ae9f8c)")
    print("2. Amazon Linux (ami-0f1a6835595fb9246)")
    choice = input("Enter 1 for Ubuntu or 2 for Amazon Linux: ")
    
    if choice == "1":
        return "ami-ubuntu-x"  
    elif choice == "2":
        return "ami-linux-x"  
    else:
        print("Invalid choice. Defaulting to Ubuntu.")
        return "ami-ubuntu-x"  


def get_instance_type():
    print("Select Instance Type:")
    print("1. t3.small")
    print("2. t3.medium")
    choice = input("Enter 1 for t3.small or 2 for t3.medium: ")
    
    if choice == "1":
        return "t3.small"
    elif choice == "2":
        return "t3.medium"
    else:
        print("Invalid choice. Defaulting to t3.small.")
        return "t3.small" 


def get_region_and_zone():
    print("Select Region (default to us-east-1 if invalid):")
    region = input("Enter the region (e.g., us-east-1): ").strip()
    
    if region != "us-east-1":
        print("Invalid region. Defaulting to us-east-1.")
        region = "us-east-1"
    
    print("Select Availability Zone (e.g., us-east-1a, us-east-1b):")
    zone = input("Enter the availability zone: ").strip()
    
    return region, zone


def get_load_balancer_name():
    lb_name = input("Enter custom Load Balancer name: ").strip()
    return lb_name

def get_user_input():
    ami = get_ami()
    instance_type = get_instance_type()
    region, zone = get_region_and_zone()
    lb_name = get_load_balancer_name()
    

    user_selections = {
        'ami': ami,
        'instance_type': instance_type,
        'region': region,
        'zone': zone,
        'load_balancer_name': lb_name
    }
    

    return user_selections


def render_template(user_selections):
    template = """
    AMI: {{ ami }}
    Instance Type: {{ instance_type }}
    Region: {{ region }}
    Availability Zone: {{ zone }}
    Load Balancer Name: {{ load_balancer_name }}
    """
    

    jinja_env = jinja2.Environment()
    template = jinja_env.from_string(template)
    

    rendered_output = template.render(user_selections)
    
    print("\nRendered Output:")
    print(rendered_output)


user_selections = get_user_input()
render_template(user_selections)
