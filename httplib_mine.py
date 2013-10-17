import httplib
httpconn = httplib.HTTPConnection("www-130.ibm.com")
httpconn.request("GET", "/developerworks/index.html")

resp = httpconn.getresponse()

if resp.reason == "OK":
    resp_data = resp.read()
    print resp_data
httpconn.close()
