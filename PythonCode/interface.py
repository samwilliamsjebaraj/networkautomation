class Interface:
    def __init__(self):
        self.ip_address=None
        self.inbound_acl=None
        self.outbound_acl=None
        self.vrf=None
    def get_values(self,ip,acl_inbound,acl_outbound,vrf):
        self.ip_address=ip
        self.inbound_acl=acl_inbound
        self.outbound_acl=acl_outbound
        self.vrf=vrf

class GigInterface(Interface):
    def __init__(self,intf_name):
        self.gig_interface_name=intf_name

class SerialInterface(Interface):
    def __init__(self,intf_name):
        self.serial_interface_name=intf_name


if __name__=="__main__":
    gi=GigInterface("Gig0/1")
    gi.inbound_acl="INBOUND_TEST_ACL"
    gi.outbound_acl="OUTBOUND_TEST_ACL"
    gi.ip_address="10.1.1.1"
    gi.vrf="TEST_VRF"
    print "INTERFACE:{} IP:{}, INBOUND ACL:{}, OUTBOUND ACL:{}, VRF:{}".format(gi.gig_interface_name,gi.ip_address,\
        gi.inbound_acl,gi.outbound_acl,gi.vrf)

    si=GigInterface("SERIAL0/1")
    si.inbound_acl="INBOUND_TEST_ACL"
    si.outbound_acl="OUTBOUND_TEST_ACL"
    si.ip_address="10.1.12.1"
    si.vrf="TEST_VRF"
    print "INTERFACE:{} IP:{}, INBOUND ACL:{}, OUTBOUND ACL:{}, VRF:{}".format(si.gig_interface_name,si.ip_address,\
        si.inbound_acl,si.outbound_acl,si.vrf)

        



