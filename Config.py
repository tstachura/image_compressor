import yaml


class Config:
    class __Config:
        def __init__(self):
            with open("config.yml", 'r') as yml_file:
                config_file = yaml.load(yml_file, Loader=yaml.FullLoader)
            self.compressorConfig = CompressorConfig(config_file['compressorConfig'])
            self.imageHandlerConfig = ImageHandlerConfig(config_file['imageHandlerConfig'])

    instance = None

    def __init__(self):
        if not Config.instance:
            Config.instance = Config.__Config()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class ImageHandlerConfig:
    def __init__(self, raw):
        self.imageLocation = raw['image_location']
        self.block_width = raw['block_width']
        self.block_height = raw['block_height']


class CompressorConfig:
    def __init__(self, raw):
        self.bits_per_codevector = raw['bits_per_codevector']
        self.epochs = raw['epochs']
        self.initial_learning_rate = raw['initial_learning_rate']
