import sys
output=""
with open("file.txt") as f:
    for line in f:
        if not line.isspace():
            output+=line
            
f= open("output.txt","w")
f.write(output)
