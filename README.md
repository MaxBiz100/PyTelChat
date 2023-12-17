# PyTelChat
Simple Python-based telnet chat server. Quite buggy and defintly insecure. Please read the ENTIRE readme before usage!
## What is PyTelChat
PyTelChat is a very basic telnet chat server that is 100% python. It is easy to set up and host, and joining is also very easy more detail below.
## Setting up and configuring PyTelChat
You will need at least Python 3, and have a computer to run it on (tested on only Linux and MacOS). Setting up requires you to download the files, and in the "server.py" file, replace 5212 (the port number on line 34) with a desired port number. THIS MUST BE CHANGED EVERY TIME THE SERVER IS TERMINATED! CLIENTS WILL NOT BE ABLE TO CONNECT IF IT IS NOT CHANGED EVERY TIME! This will be fixed in a later update. No other config is required
## Connecting to server
Connecting to the server can only be done with the command telnet. Just type telnet (server IP) (port number). With the brackets replaced with the respictive things. PuTTY does NOT work and may crash the server.
## Post all issues on the issue tracker
