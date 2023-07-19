package com.ofu.kafkaProducer.service;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class Consumer {

    @KafkaListener(topics = "test_topic",groupId = "deneme")
    public void consumeMessage(String message){
        System.out.println(message);
    }
}
