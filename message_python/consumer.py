from confluent_kafka import Consumer, KafkaException

# Configuração do Consumer
conf = {
    'bootstrap.servers': '[ip do host]:9092',  # Endereço do Kafka Broker
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Criar o Consumer
consumer = Consumer(conf)

# Assinar o tópico
topic = 'meu-topico'
consumer.subscribe([topic])

# Consumir mensagens
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"Fim da partição {msg.partition()} do tópico {msg.topic()}")
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Mensagem recebida
            print(f"Mensagem recebida: chave={msg.key().decode('utf-8')}, valor={msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    # Fechar o consumer
    consumer.close()