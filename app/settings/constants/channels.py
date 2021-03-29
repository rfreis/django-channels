from ..utils import *


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(get_env_var("REDIS_HOSTNAME"), get_env_var("REDIS_PORT"))],
        },
    },
}
