from kafka import KafkaConsumer

# Kafka broker(s) configuration
bootstrap_servers = 'localhost:9092'

# Kafka topic to consume messages from
topic_name = 'test_topic'

# Create a KafkaConsumer instance
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    group_id='deneme',  # Change the group_id to a unique name for your application
    auto_offset_reset='earliest',  # Start consuming from the earliest available message in the topic
    enable_auto_commit=False      # Disable auto-commit to have more control over message consumption
)

try:
    # Continuously poll for new messages
    for message in consumer:
        # The messages are in raw bytes. Decode them assuming they are encoded in UTF-8.
        message_value = message.value.decode('utf-8')
        print(f"Received message: {message_value}")

        # You can process the message here or take any appropriate action.

        # If you want to commit the offset manually after processing the message,
        # uncomment the following line.
        # consumer.commit()

except KeyboardInterrupt:
    # Close the consumer on keyboard interrupt (Ctrl+C)
    consumer.close()
