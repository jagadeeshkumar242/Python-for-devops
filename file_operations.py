def update_config_details(file_path, key, value):
    with open(file_path, "r") as xyz:
        lines = xyz.readlines()
    with open(file_path, "w") as xyz:
        for line in lines:
            if key in line:
                xyz.write(key + "=" + value + "\n")
            else:
                xyz.write(line)

update_config_details("server.conf", "MAX_CONNECTIONS", "200")

=================================================================
server.conf
==================================================================

# Server Configuration File

# Network Settings
PORT = 8080
MAX_CONNECTIONS=200
TIMEOUT = 30

# Security Settings
SSL_ENABLED = true
SSL_CERT = /path/to/certificate.pem

# Logging Settings
LOG_LEVEL = INFO
LOG_FILE = /var/log/server.log

# Other Settings
ENABLE_FEATURE_X = true
