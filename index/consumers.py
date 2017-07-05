from channels import Group


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("odds").add(message.reply_channel)


def ws_receive(message):
    Group("odds").add(message.reply_channel)


def ws_disconnect(message):
    Group("odds").discard(message.reply_channel)
