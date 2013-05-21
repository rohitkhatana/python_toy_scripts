from xml.dom import minidom
xml="""<HostipLookupResultSet xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.1" xsi:noNamespaceSchemaLocation="http://www.hostip.info/api/hostip-1.0.1.xsd">
<gml:description>This is the Hostip Lookup Service</gml:description>
<gml:name>hostip</gml:name>
<gml:boundedBy>
<gml:Null>inapplicable</gml:Null>
</gml:boundedBy>
<gml:featureMember>
<Hostip>
<ip>203.199.146.114</ip>
<gml:name>Pune</gml:name>
<countryName>INDIA</countryName>
<countryAbbrev>IN</countryAbbrev>
<!--  Co-ordinates are available as lng,lat  -->
<ipLocation>
<gml:pointProperty>
<gml:Point srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
<gml:coordinates>73.8667,18.5333</gml:coordinates>
</gml:Point>
</gml:pointProperty>
</ipLocation>
</Hostip>
</gml:featureMember>
</HostipLookupResultSet>"""
def coordinates(xml):
    c = minidom.parseString(xml)
    co = c.getElementsByTagName("gml:coordinates")
    if co:
        coordinate = co[0].childNodes[0].nodeValue
        if coordinate:
            st = coordinate.split(",")
            logitude = st[1]
            lattitude = st[0]
            t  = (logitude,lattitude)
            return t


print coordinates(xml)
        
    
