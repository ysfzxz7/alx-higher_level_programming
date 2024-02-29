#!/bin/bash
#this script to know all the http options that a serve accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d " "
