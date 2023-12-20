import logging


class Logger(object):
    def __init__(self, name=None, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s : %(message)s")

        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(self.formatter)
        self.streamHandler.setLevel(level)
        self.logger.addHandler(self.streamHandler)

    @classmethod
    def build(cls, name, level=logging.INFO):
        return Logger(name, level=level).logger


if __name__ == "__main__":
    logger = Logger().build(__name__)
    text = "Hello"
    logger.info("nihao:%s, %s" % (text, "hah"))
    logger.info("nihao:%s", text)
    sender = "11111"
    recipient_id = 22222
    json = "333333"
    logger.debug("sender:%s,recipient_id:%s,message:%s" % (sender, recipient_id, json))
