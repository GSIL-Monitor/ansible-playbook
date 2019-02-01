# Useage:
#
#   {{ hostname | hostname_to_be_split }}
# 

import os

def split_hostname(hostname):
    """ hostname split with '-'
    bje-xxy-op-dev-test  --> devtest
    """
    return "".join(hostname.split("-")[-2:])

def ip_to_hostname(ip):
    """
    192.168.1.1 --> 192-168-1-1
    """
    return ip.replace(".", "-")

def basename_loc(path):
    """
    /path/to/file --> file
    """
    return os.path.basename(path)

def dirname_loc(path):
    """
    /path/to/file --> /path/to
    """
    return os.path.dirname(path)

def filename_loc(path):
    multi_suffix_name = ["tar"]
    base_name = basename_loc(path)

    tmp_list = base_name.split(".")

    if len(tmp_list) > 2:
        if tmp_list[-2] in multi_suffix_name:
            return ".".join(tmp_list[:-2])
        return ".".join(tmp_list[:-1])

    elif len(tmp_list) == 2:
        return tmp_list[0]

    else:
        return base_name

def suffixname_loc(paht):
    base_name = basename_loc(path)
    file_name = filename_loc(base_name)
    return base_name.replace(file_name, "")


def split_inx(str_list, separator, inx):
    """
    split a str to list by separator and return the index of item

    etcd-v3.2.24-linux-amd64.tar.gz -- (-, 0) --> etcd 
    """
    tmp_list = str_list.split(separator)
    return tmp_list[inx]

def filter_host_with_var(host_vars, var):
    res = []
    for host, vars in host_vars.items():
    	if var in vars:
    		res.append(host)
    return res

def get_kubeadm_join_cmd(host_vars, var):
    for host, vars in host_vars.items():
    	if var in vars:
    		return vars[var].get('stdout')

class FilterModule(object):
    def filters(self):
        return {'split_hostname': split_hostname,
                'ip_to_hostname': ip_to_hostname,
                'basename_loc': basename_loc,
                'dirname_loc': dirname_loc,
                'filename_loc': filename_loc,
                'suffixname_loc': suffixname_loc,
                'split_inx': split_inx,
                'filter_host_with_var': filter_host_with_var,
                'get_kubeadm_join_cmd': get_kubeadm_join_cmd
        		}
