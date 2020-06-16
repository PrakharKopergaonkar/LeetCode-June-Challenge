#Question 16: Validate IP Address

class Solution:
    def validIPAddress(self, IP: str) -> str:
       
        if("." in IP):
            ipv4 = IP.split(".")
            if(len(ipv4)!=4):
                return "Neither"
            for i in ipv4:
                try:
                    if(len(i)==0 ):
                        return "Neither"
                    elif(i[0]=="0" and len(i)!=1):
                        return "Neither"
                    l = int(i)
                    if(l>=256 or l<0):
                        return "Neither"
                    elif(l==0 and i[0]=="-"):
                        return "Neither"
                except ValueError:
                    return "Neither"
            return "IPv4"
        
        elif(":" in IP):
            ipv6 = IP.split(":")
            if(len(ipv6)!=8):
                return "Neither"
            for i in ipv6:
                if(i == ""):
                    return "Neither"
                elif(len(i)>4):
                    return "Neither"
                else:
                    for j in i:
                        try:
                            a = int(j)
                        except:
                            j1 = j.lower()
                            if(ord(j1)<97 or ord(j1)>102):
                                return "Neither"
                        
            return "IPv6"
        else:
            return "Neither"
    