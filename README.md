Handles proxies with both IP addresses and hostnames, including those in the format `ip:port`

Performing the request using the constructed proxy URL, saving the working proxies to the result.txt file, and printing the total count. Please ensure that you replace 'your_login' and 'your_password' with your actual authentication credentials, and that the proxies.txt file is in the same directory as the script.

Split the proxy by : to extract the IP address part. If the proxy contains : (indicating a ip:port format), we extract the IP address using proxy.split(':')[0]. If the proxy doesn't contain :, it is treated as a hostname, and we resolve it to obtain the corresponding IP address.
