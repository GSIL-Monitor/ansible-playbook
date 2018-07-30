# Useage:
#
#   {{ hostname | hostname_to_be_split }}
# 

def split_hostname(hostname):
    """ hostname split with '-'
    bje-qtt-op-manager-test  --> managertest
    """
    return "".join(hostname.split("-")[-2:])

class FilterModule(object):
    def filters(self):
        return {'split_hostname': split_hostname}