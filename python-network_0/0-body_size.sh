#!/bin/bash
#send a request to a URL and display the size of the body of the response
curl -sI "$1" | grep -i "Content-Length" | cut -d ":" -f 2
