#!/usr/bin/env python3.8

def getBert(input):
    string = input.lower().split("bert")
    print(string)
    if len(string)%2 == 0:
        return "''"
    else:
        return "".join(reversed(string[(int(len(string)/2))])) ##returns joined list as string which is reversed - string returned is the middle element

print(getBert("bertCLivebert"))
print(getBert("xxbertfridgebertyy"))
print(getBert("asfasBertllupbERt"))
print(getBert("xxbertyhello"))
print(getBert("xxbeRTyy"))