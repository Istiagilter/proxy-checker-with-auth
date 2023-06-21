import requests
import socket

def check_proxies():
    # Read the proxy list from the file
    with open('proxies.txt', 'r') as file:
        proxies = file.read().splitlines()

    # List to store the working proxies
    working_proxies = []

    # Set the login and password for authentication
    login = 'your_login'
    password = 'your_password'

    # Create the authentication string
    auth = requests.auth.HTTPBasicAuth(login, password)

    # Iterate through the proxies and check their availability
    for proxy in proxies:
        try:
            # Check if the proxy is specified as an IP address
            if ':' in proxy:
                ip_address = proxy.split(':')[0]
            else:
                # Resolve the hostname to get the IP address
                ip_address = socket.gethostbyname(proxy)

            proxy_url = f'http://{ip_address}'

            # Perform the request using the proxy
            response = requests.get('https://api.ipify.org', proxies={'http': proxy_url, 'https': proxy_url}, auth=auth, timeout=5)
            
            if response.ok:
                working_proxies.append(proxy)
        except (socket.gaierror, requests.exceptions.RequestException):
            pass

    # Save the working proxies to the result file
    with open('result.txt', 'w') as result_file:
        result_file.write('\n'.join(working_proxies))

    print(f"Total working proxies: {len(working_proxies)}")
    print("Working proxies saved to result.txt")

# Execute the check_proxies function
check_proxies()
