package com.ofu.kafkaProducer.service;

import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class Producer {
    private static final String TOPIC = "test_topic1";
    @Autowired
    private KafkaTemplate<String,String> kafkaTemplate;

    public void sendMessage(String message){
        this.kafkaTemplate.send(TOPIC,0,null,"partiton 0");
        this.kafkaTemplate.send(TOPIC,1,null,"partiton 1");
        this.kafkaTemplate.send(TOPIC,2,null,"partiton 2");
    }

    @Bean
    public NewTopic createTopic(){

        return new NewTopic(TOPIC,3,(short) 1);
    }

}
