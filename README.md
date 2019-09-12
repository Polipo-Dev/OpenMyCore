# OpenMyCore
A project that desires to port existing Clover configurations to OpenCore.

## How does it work?
1. We scan the Clover config.plist, and turn it to a Python dict object.
2. We add all the drivers and kexts into OpenCore setup.
3. We assemble an OpenCore config based on the data from Clover, as well as the drivers and kexts.
4. We compile the freshly created OpenCore into a config.plist into the OC folder.
5. **YOU**, the user, arrange the correct positions for your kexts (make sure that Lilu is loaded before WhateverGreen is, for example).

## How do I use it?
TODO.

## As a developer, how can I help this project?
You can fork the project and create pull requests to master.
Make sure to `git pull --rebase` before doing so.

## Well, why won't my existing Clover configuration work with OpenCore already?!
OpenCore has differences in its fundamental handling of kexts, drivers, as well as a completely different config.plist.

This project is only a boilerplate for getting a "working" OpenCore configuration based on your existing Clover configuration.

## Current project milestones:
- [x] PList Parser/Encoder
  - [x] Parse PList into Python dict
  - [x] Encode Python dict into PList
- [ ] Generate a bootable OpenCore folder structure
- [ ] Copy all files from Clover to OpenCore
- [ ] Generate proper (mostly ready) OpenCore Config
- [ ] Boot!
