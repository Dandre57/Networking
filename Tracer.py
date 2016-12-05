from tld import get_tld
import os

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

"""
Method that runs tracert command
"""
def trace(domain_name):
    rt = "tracert " + domain_name
    os.system(rt)
    
"""
Main method
"""
def main():
    input = raw_input("Input the url you wish to use: ")
    
    temp = get_domain_name(input)
    trace(temp)

# Runs the program    
main()
