from publish import PublishManager
from consumer import ConsumerManager

# TODO: test the publish and comment consume message
print("publish message")
data_send = {"id": 1, "name": "John Doe", "email": "jhon@mrcode.com", "param": "test"}

publish = PublishManager()
publish.basic_publish(data_send)
print("data published successfully!")

# TODO: test the consume and comment publish message
# print("waiting for consuming message...")
# consumer = ConsumerManager()
# consumer.start()
# print("message consumed successfully!")
