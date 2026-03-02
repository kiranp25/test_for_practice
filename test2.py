# The database hands you a List of banned IPs (O(n) slow lookups)
database_list = ["192.168.1.50", "10.0.0.5", "172.16.254.1"]

new_player_ip = "10.0.0.5"

# 1. Convert the list into a Set for O(1) lookups
banned_set = set(database_list)

# 2. Write the if-statement to check if the new_player_ip is inside the set
if new_player_ip in banned_set:
    print("Connection Blocked: IP is banned.")
else:
    print("Connection Allowed: Welcome to the game.")