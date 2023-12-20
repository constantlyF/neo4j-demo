import os

import yaml

from utils.logger import Logger

logger = Logger.build(__name__)
profile = os.environ.get('PROFILES_ACTIVE', 'dev')
logger.debug("============================>当前路径:%s", os.path.abspath('.'))
logger.debug("============================>当前环境:%s", profile)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(BASE_DIR, 'config_{}.yaml'.format(profile))
with open(config_file, 'r', encoding='utf-8') as yaml_file:
    config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    logger.debug("加载了配置文件:%s", config)

NEO4J_CONFIG = config['neo4j']
