import re
ip = "255.100.50.0"

IP_FORMAT = re.compile(r"^[0-9]+$.^[0-9]+$.^[0-9]+$.^[0-9]+$",re.IGNORECASE)


def func(ip):
    if len(ip) < 16 and IP_FORMAT.match(ip.replace(".","")):
        return ip.replace(".","[.]")
    return "Invalid IP"

print(func(ip))
