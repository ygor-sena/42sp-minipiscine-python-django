#!/bin/sh
curl -s $1 | grep body | cut -d '"' -f 2