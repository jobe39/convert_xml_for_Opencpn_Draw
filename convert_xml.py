#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree



def main():
    dom = etree.parse("Import.gpx")

    opencpnNS = 'http://www.opencpn.org'
    xsiNS = 'http://www.w3.org/2001/XMLSchema-instance'
    NSMAP = {"xsi" : xsiNS,
             "opencpn" : opencpnNS}

    drawTree = etree.Element("OCPNDraw", version="0.1", creator="OpenCPN", nsmap = NSMAP)


    path = None
    foundFirstEntry = False
    odPoint = None
    pCount = 1
    
    for tag in dom.iter():
        if not len(tag):
            if tag.tag.endswith("name"):
                pCount = 1
                path = etree.SubElement(drawTree, "{%s}path" % opencpnNS)
                otype = etree.SubElement(path, "{%s}type" % opencpnNS)
                otype.text = "Boundary"
                name = etree.Element("name")
                path.append(name)
                name.text = tag.text
                foundFirstEntry = True
            if tag.tag.endswith("desc") and foundFirstEntry:
                desc = etree.Element("desc")
                path.append(desc)
                desc.text = (tag.text)
                etree.SubElement(path, "{%s}viz" % opencpnNS).text = "1"
                etree.SubElement(path, "{%s}active" % opencpnNS).text = "1"
                etree.SubElement(path, "{%s}style" % opencpnNS, active_colour="rgb(255, 0, 0)", active_fillcolour="rgb(255, 0, 0)",
                                 inactive_colour="rgb(192, 192, 192)", inactive_fillcolour="rgb(192, 192, 192)", width="2", style="100",
                                 fill_transparency="175", inclusion_boundary_size="15")
                etree.SubElement(path, "{%s}boundary_type" % opencpnNS).text = "None"
                etree.SubElement(path, "{%s}boundary_show_point_icons" % opencpnNS).text = "1"
                
            if tag.tag.endswith("rtept"):
                #if not odPoint:
                #print "FIRST OdPoint"
                odPoint = etree.SubElement(path, "{%s}ODPoint" % opencpnNS, lat = tag.attrib["lat"], lon = tag.attrib["lon"])
                etree.SubElement(odPoint, "{%s}type" % opencpnNS).text = "Boundary Point"
                pTime = etree.Element("time")
                pTime.text = "2018-04-26T16:11:23Z"
                odPoint.append(pTime)
                pName = etree.Element("name")
                pName.text="%03d" %pCount
                odPoint.append(pName)
                pCount += 1
                etree.SubElement(odPoint, "{%s}boundary_type" % opencpnNS).text = "Exclusion"
                pSym = etree.Element("sym")
                pSym.text = "Anchorage"
                odPoint.append(pSym)
                etree.SubElement(odPoint, "{%s}viz" % opencpnNS).text = "1"
                etree.SubElement(odPoint, "{%s}viz_name" % opencpnNS).text = "0"
                etree.SubElement(odPoint, "{%s}auto_name" % opencpnNS).text = "1"
                etree.SubElement(odPoint, "{%s}arrival_radius" % opencpnNS).text = "0.000"
                etree.SubElement(odPoint, "{%s}ODPoint_range_rings" % opencpnNS, visible="false", number="0", step="1",
                                 units="0", colour="#0000FE", width="2", line_style="100")


    #print(etree.tostring(drawTree, pretty_print = True, xml_declaration = True))
    with open('./Output.gpx', 'wb') as f:
        f.write(etree.tostring(drawTree, pretty_print = True, xml_declaration = True))

main()
