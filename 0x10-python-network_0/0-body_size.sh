#!/bin/bash
# Script that shows content-length from an HTTP request header
curl -Is $1 | grep 'Content-Length' | cut -d " " -f 2
