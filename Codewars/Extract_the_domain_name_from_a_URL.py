# Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string.

# For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

#Solution

# Method 1) Using regex. Here we are first finding the protocol and subdomain then, extracrting the name.
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

# Method 2) Using string replace. 
"""We are replacing the protocol name and subdomain wih null i.e. in other words we are removing that part. So what remains is the name with the rest.
For extracting the name we can use string slicing upto the next '.' after which there is top level domain."""
def domain_name(url):
    url=url.replace("https://",'')
    url=url.replace("http://",'')
    url=url.replace("www.",'')
    return url[0:url.find('.')]
