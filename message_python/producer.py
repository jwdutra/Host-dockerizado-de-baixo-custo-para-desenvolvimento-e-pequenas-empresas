from confluent_kafka import Producer
import time

# Configuração do Producer
conf = {
    'bootstrap.servers': '[ip ou nome do host]:9092',  # Endereço do Kafka Broker
    'client.id': 'python-producer'
}

# Criar o Producer
producer = Producer(conf)

# Função de callback para confirmação de entrega
def delivery_report(err, msg):
    """ Callback para confirmação de entrega """
    if err is not None:
        print(f"Erro ao entregar mensagem: {err}")
    else:
        print(f"Mensagem entregue no tópico {msg.topic()} [partição {msg.partition()}]")

# Tópico para enviar mensagens
topic = 'meu-topico'

# Enviando mensagens
try:
    for i in range(10):  # Envia 10 mensagens como exemplo
        key = f"chave-{i+1}"
        message = f"Mensagem {i+1}"
        producer.produce(topic, key=key.encode('utf-8'), value=message.encode('utf-8'), callback=delivery_report)
        producer.flush()  # Garante que a mensagem foi enviada para o broker
        time.sleep(0.5)  # Espera meio segundo antes de enviar a próxima mensagem
    print("Mensagens enviadas com sucesso!")
except Exception as e:
    print(f"Erro ao enviar mensagens: {e}")
