# Host dockerizado de baixo custo para desenvolvimento e pequenas empresas.

Configurações de host de baixo custo com soluções Open Souce, dokerizado, contendo mensageria, banco de dados, servidor web, proxy reverso, certificados de segurança  e configurações de domínio.


**Este projeto fornece configurações de infraestrutura de baixo custo e flexível baseada em containers Docker, adequada para hospedar aplicações modernas. Ele inclui configurações otimizadas para gerenciamento com Portainer, serviços de mensageria com Apache Kafka, banco de dados relacional PostgreSQL, proxy reverso NGINX, orquestração de tráfego com Traefik e integração com Cloudflare para segurança e performance e serviço de domínios.

### Motivação

A crescente demanda por soluções escaláveis e resilientes requer infraestruturas que sejam simples de implementar e gerenciar. Este repositório tem como objetivo fornecer um ponto de partida funcional para a configuração de um ambiente que prioriza automação, escalabilidade e facilidade de gerenciamento.

### Uso Pretendido

Este repositório é ideal para:

* Desenvolvedores que desejam uma infraestrutura padronizada para começar projetos.
* Ponto de partida para pequenas empresas que buscam iniciar suas operações já em ambiente moderno e escalável.
* Times que necessitam de um ambiente integrado para testar aplicações com mensageria e bancos de dados.

### Principais componentes do ambiente

### Gerenciamento de contêineres:

* ### Docker e Docker Compose: Todos os serviços são configurados e orquestrados usando o Docker e Docker Compose, permitindo replicação rápida do ambiente em diferentes máquinas.
* ### Portainer: Ferramenta para gerenciamento visual de contêineres Docker, simplificando operações de infraestrutura.

### Proxy reverso e balanceamento de carga:

* ### Traefik: Proxy reverso e balanceador de carga dinâmico com suporte nativo para integrações Docker e certificados SSL via Cloudflare ou próprios com Letsencrypt.

### Mensageria:

* ### Apache Kafka: Plataforma de streaming distribuído para mensageria e processamento de eventos em tempo real.
* ### UI for Apache Kafka: Interface gráfica para gerenciamento e monitoramento dos tópicos e mensagens no Kafka.

### Banco de dados relacional:

* ### PostgreSQL: Banco de dados relacional robusto, escalável e de código aberto.
* ### PgAdmin 4: Ferramenta web para gerenciamento e administração do PostgreSQL.

### Segurança e DNS:

* ### Cloudflare: Plataforma de serviços de segurança, desempenho e gerenciamento de DNS, incluindo provisionamento automático de certificados SSL.

### Servidor Web

* ### NGINX: Servidor Web leve e amplamente usado no mercado para provimento de páginas e aplicações de Internet.

### Benefícios

* Modularidade: Cada serviço é isolado em seu próprio container, permitindo manutenção e atualizações sem impacto geral.
* Escalabilidade: Configurações adaptáveis para ambientes locais e em nuvem, como DigitalOcean ou AWS.
* Segurança: Certificados TLS gerenciados automaticamente pelo Traefik em conjunto com a proteção oferecida pela Cloudflare.
* Observabilidade: Portainer oferece uma visão clara do estado e desempenho dos containers.

A seguir, detalhamos as configurações de cada componente e instruções para implantação.

**
