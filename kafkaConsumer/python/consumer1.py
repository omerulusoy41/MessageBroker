from kafka import KafkaConsumer

# Kafka broker(s) configuration
bootstrap_servers = 'localhost:9092'

# Kafka topic to consume messages from
topic_name = 'test_topic1'

# Create a KafkaConsumer instance
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    group_id='deneme',  # Change the group_id to a unique name for your application
    auto_offset_reset='latest',  # Start consuming from the earliest available message in the topic
    enable_auto_commit=True      # Disable auto-commit to have more control over message consumption
)

try:
    
    # Continuously poll for new messages
    for message in consumer:
        i = 1
        # The messages are in raw bytes. Decode them assuming they are encoded in UTF-8.
        message_value = message.value.decode('utf-8')
        print(f"{i}. producer push message: {message_value}")
        print("-----------------")
        # You can process the message here or take any appropriate action.
        i += 1
        # If you want to commit the offset manually after processing the message,
        # uncomment the following line.
        consumer.commit()
   
except KeyboardInterrupt:
    # Close the consumer on keyboard interrupt (Ctrl+C)
    consumer.close()
