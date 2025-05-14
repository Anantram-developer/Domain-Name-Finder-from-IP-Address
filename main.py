import socket

def reverse_dns_lookup(ip):
    try:
        domain = socket.gethostbyaddr(ip)
        return domain[0]  # Primary domain name
    except socket.herror:
        return "No domain name found for this IP"

# Example usage
ip_address = '8.8.8.8'
print("Domain:", reverse_dns_lookup(ip_address))
