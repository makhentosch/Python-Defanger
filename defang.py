def defang_ip(ip):
    defanged_ip = ""
    for charec in ip:
        if charec == '.':
            defanged_ip += '[.]'
        elif charec == ':':
        	defanged_ip += '[:]'
        else:
            defanged_ip += charec
    return defanged_ip

def defang_ip_addresses(ip_addresses):
    defanged_ips = [defang_ip(ip) for ip in ip_addresses]
    return defanged_ips


input_ip_addresses = input('[*]Enter the IP addresses: ')
input_ip_addresses = input_ip_addresses.split(' ')
defanged_ips = defang_ip_addresses(input_ip_addresses)

for i in defanged_ips:
	print(i) 


