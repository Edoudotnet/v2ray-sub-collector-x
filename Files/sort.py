import requests
import os
import base64

# Function to generate base64 encoded header text for each protocol
def generate_header_text(protocol_name):
    titles = {
        'vmess': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3x2bWVzcw==",
        'vless': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3x2bGVzcw==",
        'trojan': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3x0cm9qYW4=",
        'ss': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3xzcw==",
        'ssr': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3xzc3I=",
        'tuic': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3x0dWlj",
        'hy2': "w5DOm8mM4oKt4ZGOzp7wkJKh8JCSoXzwk4SC8JOGg3xoeTI="
    }
    base_text = """#profile-title: base64:{base64_title}
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#profile-web: https://github.com/Edoudotnet

"""
    return base_text.format(base64_title=titles.get(protocol_name, ""))

protocols = {
    'vmess': 'Emad_vmess.txt',
    'vless': 'Emad_vless.txt',
    'trojan': 'Emad_trojan.txt',
    'ss': 'Emad_ss.txt',
    'ssr': 'Emad_ssr.txt',
    'tuic': 'Emad_tuic.txt',
    'hy2': 'Emad_hysteria2.txt'
}

ptt = os.path.abspath(os.path.join(os.getcwd(), '..'))
splitted_path = os.path.join(ptt, 'Sort-By-Protocol')

# Ensure the directory exists
os.makedirs(splitted_path, exist_ok=True)

protocol_data = {protocol: generate_header_text(protocol) for protocol in protocols}

# Fetching the configuration data
response = requests.get("https://raw.githubusercontent.com/Edoudotnet/V2ray-Sub-Collector-x/main/All_Emad_Sub.txt").text

# Processing and grouping configurations
for config in response.splitlines():
    for protocol in protocols.keys():
        if config.startswith(protocol):
            protocol_data[protocol] += config + "\n"
            break

# Encoding and writing the data to files
for protocol, data in protocol_data.items():
    file_path = os.path.join(splitted_path, protocols[protocol])
    encoded_data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    with open(file_path, "w") as file:
        file.write(encoded_data)
