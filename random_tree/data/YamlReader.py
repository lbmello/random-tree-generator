"""Modulo YamlReader."""

import yaml


class YamlReader:
    """ Le o arquivo config.yaml."""

    """
        Requisito: 
            PyYaml > 5.3.

        Formato YAML:
        - basic:
            path: string
            levels: int
            size: int
            debug: boolean
        """

    config_yaml = open('../../config.yaml', 'r')
    config_file = yaml.load(config_yaml, Loader=yaml.FullLoader)

    # TODO: Criar multiplas entradas via YAML
    config = config_file[0]
    config = config['basic']

    path = config['path']
    levels = config['levels']
    size = config['size']
    debug = config['debug']
