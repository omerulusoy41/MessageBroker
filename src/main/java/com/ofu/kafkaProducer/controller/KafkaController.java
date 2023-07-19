package com.ofu.kafkaProducer.controller;

import com.ofu.kafkaProducer.service.Producer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/kafka")
public class KafkaController {

    @Autowired
    public Producer producer;

    @GetMapping("/{msg}")
    public void sayHello(@PathVariable("msg") String msg){
        producer.sendMessage(msg);
    }
}
