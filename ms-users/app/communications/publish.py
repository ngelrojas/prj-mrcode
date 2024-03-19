import json
from channels import ChannelManager


class PublishManager:

    def basic_publish(self, data_send):
        channel = ChannelManager()
        json_data = json.dumps(data_send)
        return channel.get_basic_publish(json_data=json_data)
