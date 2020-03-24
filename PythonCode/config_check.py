"""
File:config_check.py
Performs configuration audit
"""
class ConfigCheck(object):
    """
    Performs configuration audit
    """
    def __init__(self,config_list):
        self._config_list=config_list
    def return_matched_configs(self,config):
        """
        Returns the configs that are matched with the standard config
        uses 2 parameters (1. config, 2.config_list)
        """
        for lines in self._config_list:
            if config==lines:
                return config
    def return_unmatched_configs(self,config):
        """
        Returns the configs that are not matching with the standard config
        uses 2 parameters(1.config, 2.config_list)
        """
        for stmt in self._config_list:
            print "{}!={}".format(config,stmt)
            if config==stmt:
                return config

if __name__=="__main__":
    config_list=["router bgp 123",
    "network 10.0.0.0",
    "network 172.128.0.0",
    "network 192.168.1.0"]
    device_config=["router bgp 123",
    "network 11.0.0.0",
    "network 172.128.0.0",
    "network 192.168.1.0"]
    cc=ConfigCheck(config_list)
    print filter(cc.return_matched_configs,device_config)
    cc=ConfigCheck(config_list)
    for lines in device_config:
        print cc.return_unmatched_configs(lines)