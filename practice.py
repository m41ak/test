#fire wall simulator
import random 
def gen_randomip():
    #in the practice code theres a docstring and its basically a documentation for the function
    """generates random ip address"""
    return f"123.456.1.{random.randint(0, 20)}"
#we have the ip address and we set the range for the int address which is (0, 20)
#f stands for literal string
#the following function has parameters the ip and  the rules
def check_firewall_rules(ip, rules):
    """checks if ip address allowed or blocked"""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

    
    

def main():
    #firewall rules dictionary and what to do with them
    #the dictionary contains ip address, value and action 
    firewall_rules = {
        "123.456.1.5" : "block",
        "123.456.1.9" : "block",
        "123.456.1.11" : "block",
        "123.456.1.18" : "block",
        "123.456.1.10" : "block",
        "123.456.1.4" : "block",

    }
#simulate network traffic b making a random address generator 
#first we need to make generate random ip function at the top
#second is we need a function that helps determine the action
if _ in range(12):
    ip_address = gen_randomip()
    action = check_firewall_rules(ip_address, firewall_rules)
    random_number = random.randint(0, 9999)
    print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")





if __name__ ==  "__main__": 
    main()