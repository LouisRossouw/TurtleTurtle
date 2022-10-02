import yaml



#            # Configs

def yaml_config(config_path):
    """ Open yaml configs """
    config = yaml.safe_load(open(config_path))
    return(config)