""" 

## TCP congestion control

This experiment shows the basic behavior of TCP congestion control. You'll see the classic "sawtooth" pattern in a TCP flow's congestion window, and you'll see how a TCP flow responds to congestion indicators.

It should take about 1 hour to run this experiment.

Instructions for running the experiment are at: https://witestlab.poly.edu/blog/tcp-congestion-control-basics/ """

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node romeo
node_romeo = request.XenVM('romeo')
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_romeo.Site('Site 1')
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface0 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.10.1.100','255.255.255.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_juliet.Site('Site 1')
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface1 = node_juliet.addInterface('interface-3', pg.IPv4Address('10.10.2.100','255.255.255.0'))

# Node router
node_router = request.XenVM('router')
node_router.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_router.Site('Site 1')
node_router.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface2 = node_router.addInterface('interface-0', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface3 = node_router.addInterface('interface-2', pg.IPv4Address('10.10.2.1','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.Site('undefined')
link_0.addInterface(iface2)
link_0.addInterface(iface0)

# Link link-1
link_1 = request.Link('link-1')
link_1.Site('undefined')
link_1.addInterface(iface3)
link_1.addInterface(iface1)


# Print the generated rspec
pc.printRequestRSpec(request)

