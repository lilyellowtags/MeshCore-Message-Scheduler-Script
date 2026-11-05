# MeshCore-Message-Scheduler-Script
MeshCore Message Scheduler Script README

This is a fairly janky way of automating messages through 
MeshCore-CLI (meshcli). In these four easy steps, we'll create a
script to run in MeshCore-CLI, then run it in MeshCore-CLI.

You'll need to install python3 and MeshCore-CLI. If you haven't
installed MeshCore-CLI, you'll also probably need to install
pipx. It's as easy as typing these commands into your Ubuntu 
terminal:

"
sudo apt install python3
sudo apt install pipx
sudo pipx install meshcore-cli
"

1.
 Create a file called "messages.txt" in the same folder
as generate.py.

For each message you wish to send, create a new line in the file.

For example: 

"
Test 1
Test 2
Final Test
"

Each line will be soon converted to a message in Step 2.

2.
 Open generate.py. I use the command "nano generate.py" on
my Ubuntu machine.

This is the script that you'll run with Python. 

Choose your desired channel number (If you use get_channels on 
meshcore-cli you can see all the channel numbers listed on your 
node.)

Choose your desired delay length in seconds. I hope I don't need
to tell you that there are 60 seconds in a minute. Just write the
number (ie "4"), and don't type something like "4 seconds".

Save and exit. If you're using nano, use CTRL+O, hit yes, and then
CTRL+X.

3. 
 Run the python script called generate.py. You can use this in CLI:
"python3 generate.py"
(If you're using the Ubuntu command line)

Wait for it to generate. Once it's finished, you can check the file
"mscript-01" to make sure it looks right. You can use 
"nano mscript-01" if you're using the command line.

It should look something like this:

"
chan 2 "Test 1"
sleep 60
chan 2 "Test 2"
sleep 60
chan 2 "Final Test"
"

4. 
 Open meshcore-cli and run the script from inside its CLI program. 

Because I use a USB port, I use the phrase "meshcli -S",
and it opens a little screen where I can click on my node. 

If you're using Bluetooth, don't use the "-S" flag and it should just 
use your computer's internal Bluetooh transciever to automatically 
scan for currently disconnected nodes and let you sign in from there.

If you're using the web protocol, good luck I have no idea how to use
that one.

Once you're in meshcore-cli, run the command "script mscript-01"

Ta da! Your scripted messages should start transmitting.

If you have a second node, watch it to make sure the messages are
correctly sending out!

Created for anyone to use by @lilyellowtags
