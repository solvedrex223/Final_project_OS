import sys

string = sys.path[0]
string = string.split("/")
while string[len(string) - 1] != "web_server":
    string.pop()
for i in range(len(string) - 1):
    string[i]+= "/"
r_sys = "".join(string)
sys.path.insert(1, r_sys)