import channels

message = "hello from ms-users"
channels.channel.basic_publish(
    exchange="", routing_key="mr_code_response", body=message
)
