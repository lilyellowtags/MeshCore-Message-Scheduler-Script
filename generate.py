from pathlib import Path

# Use this script to generate a script that is run through MeshCore-CLI using "script mscript-01"
# You may need to look up the channel number using "get_channels"
# Change the delay to whatever you want, it's in seconds so multiply whatever minutes you want to wait by 60 or hours you want to wait by 3600
# Configuration
CHANNEL = 2       # Replace with the intended channel number
DELAY = 300       # 5 minutes

# Read messages
messages = [
    line.strip()
    for line in Path("messages.txt").read_text().splitlines()
    if line.strip()
]

# Generate MeshCore script
commands = []

for i, message in enumerate(messages):

    # Put quotation marks around each message
    commands.append(f'chan {CHANNEL} "{message}"')

    # Wait between messages, but not after the last one
    if i < len(messages) - 1:
        commands.append(f'sleep {DELAY}')

Path("mscript-01").write_text("\n".join(commands) + "\n")

print(f"Generated mscript-01 with {len(messages)} messages.")
print(f"Delay: {DELAY} seconds")
print("Run with: meshcli script mscript-01")
