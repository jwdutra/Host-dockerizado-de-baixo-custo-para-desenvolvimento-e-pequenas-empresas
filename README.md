# Host dockerizado de baixo custo para desenvolvedores e pequenas empresas.

Configurações de host de baixo custo com soluções Open Souce, dokerizado, contendo mensageria, banco de dados, servidor web, proxy reverso, certificados de segurança  e configurações de domínio.

Este projeto fornece configurações de infraestrutura de baixo custo e flexível baseada em containers Docker, adequada para hospedar aplicações modernas. Ele inclui configurações otimizadas para gerenciamento com Portainer, serviços de mensageria com Apache Kafka, banco de dados relacional PostgreSQL, Servidor web  NGINX, orquestração de tráfego e provimento de SSL com Traefik e integração com Cloudflare para segurança, performance e serviço de domínios.

### Motivação

A crescente demanda por soluções escaláveis e resilientes requer infraestruturas que sejam simples de implementar e gerenciar. Este repositório tem como objetivo fornecer um ponto de partida funcional para a configuração de um ambiente que prioriza automação, escalabilidade e facilidade de gerenciamento.

### Uso Pretendido

Este repositório é ideal para:

* Desenvolvedores que desejam uma infraestrutura padronizada para começar projetos.
* Ponto de partida para pequenas empresas que buscam iniciar suas operações já em ambiente moderno e escalável.
* Times que necessitam de um ambiente integrado para testar aplicações com mensageria e bancos de dados.

### Principais componentes do ambiente

#### Gerenciamento de contêineres:

* Docker e Docker Compose: Todos os serviços são configurados e orquestrados usando o Docker e Docker Compose, permitindo replicação rápida do ambiente em diferentes máquinas.
* Portainer: Ferramenta para gerenciamento visual de contêineres Docker, simplificando operações de infraestrutura.

#### Proxy reverso e balanceamento de carga:

* Traefik: Proxy reverso e balanceador de carga dinâmico com suporte nativo para integrações Docker e certificados SSL via Cloudflare ou próprios com Letsencrypt.

#### Mensageria:

* Apache Kafka: Plataforma de streaming distribuído para mensageria e processamento de eventos em tempo real.
* UI for Apache Kafka: Interface gráfica para gerenciamento e monitoramento dos tópicos e mensagens no Kafka.

#### Banco de dados relacional:

* PostgreSQL: Banco de dados relacional robusto, escalável e de código aberto.
* PgAdmin 4: Ferramenta web para gerenciamento e administração do PostgreSQL.

#### Segurança e DNS:

* Cloudflare: Plataforma de serviços de segurança, desempenho e gerenciamento de DNS, incluindo provisionamento automático de certificados SSL.

#### Servidor Web

* NGINX: Servidor Web leve e amplamente usado no mercado para provimento de páginas e aplicações de Internet.

#### Gerenciamento de dados não estruturados

* MinIO: MinIO é uma plataforma de armazenamento de objetos de alta performance, compatível com o protocolo S3 da Amazon, projetada para armazenar grandes volumes de dados não estruturados.Servidor Web leve e amplamente usado no mercado para provimento de páginas e aplicações de Internet

### Benefícios

* Modularidade: Cada serviço é isolado em seu próprio container, permitindo manutenção e atualizações sem impacto geral.
* Escalabilidade: Configurações adaptáveis para ambientes locais e em nuvem, como DigitalOcean ou AWS.
* Segurança: Certificados TLS gerenciados automaticamente pelo Traefik em conjunto com a proteção oferecida pela Cloudflare.
* Observabilidade: Portainer oferece uma visão clara do estado e desempenho dos containers.

### Implementação

#### Qual host contratar?

Para efeito de desenvolvimento, alguns recursos deste ambiente podem ser configurados localmente. É possível ter um ambiente Docker na própria máquina com vários recursos, porém, alguns outros, como criptografia e serviço de domínio só se consegue em ambientes remotos com serviços ligados à Internet.

A vantagem de se ter um host na Internet é que se aproxima muito de um ambiente profissional, sendo possível já disponibilizar aplicações em ambiente real. A intenção é que, desenvolvedores trabalhem o código localmente e depois subam a aplicação para o host, já disponibilizando na Internet.

Serviços em nuvem em ambientes profissionais como AWS, GCP, Azure e até mesmo Digitalocean, disponibilizam máquinas bem baratas, porém podem se tornar caros  para iniciar com recursos necessários para um ambiente como este, que demanda mais poder de máquina como memória, CPU e espaço em disco.

Uma solução seria investir um pouco mais nos recursos, tornando os valores inviáveis, ou partir para outra solução barata no mercado, que são os VPSs.

Apesar de não ser o ideal, permite que tudo seja instalado e funcione muito bem, tanto para desenvolvedores quanto para empresas pequenas que estão iniciando, e o fato de estar dockerizado e modularizado e com possível clusterização, permite que seja migrado facilmente para um ambiente mais robusto e profissional.

Todos os serviços foram implantados em um VPS de baixo custo, ficando bem satisfatório e barato.

* Núcleos de CPU: 2
* Memória: 8 GB
* Espaço em disco: 100 GB
* Largura de banda: 8 TB

O consumo dos recursos (apenas instalação) ficou muito satisfatório, sobrando ainda bastante para as operações.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXez87GNjf1mOAIDbo0pJhfu8px0iElq9LGrofhLvVX9__6Hc2hvUdlKiLyBuj7glUdS9XgF9yheMd3Hiy306g3AfyHHcSsgZ_1Sn9fddwRPWeOyXdz2mI61-92MrBc1csA2At_2Vw?key=NZsbhft-UgpfY2ZKTYnezWgM)

#### Implantação dos serviços

O objetivo não é ensinar detalhadamente os conceitos e pormenores de cada recurso, mas sim, partindo do pressuposto que já se tenha noção dos mesmos ou que se busque obtê-los, procura-se mostrar os meios de configurá-los e instalá-los em um ambiente dockerizado.

Procure estudar sobre os recursos acessando os links que estão presentes no documento.

#### O VPS e o SO.

Aopós pesquisas na Internet sobre os vários serviços de VPS disponíveis.

Foi usado na implementação um VPS Hostinger (não é propaganda), sendo um dos que tem melhor custo/benefício, e com menor latência, por ter servidores no Brasil.

[https://www.hostinger.com.br/servidor-vps](https://www.hostinger.com.br/servidor-vps)

Opte por, pelo menos, um KVM2 e instale um SO Linux

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc4L40EGzNiXzH3ayYZefCFIKDa3nDJPlcC33fud92uqmHwCc6DfCfkATdABGKgGJBt6HgsIKWFogmCnJ0WAXQ9W_pRO9a3ndkYDCy_MWcZ_oKXh3BK3OTf7RQiB4Ic3HGZsf2e?key=NZsbhft-UgpfY2ZKTYnezWgM)

Instale o Docker e Docker compose.

[https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)

Instale o Docker e Docker Compose como orientado nos links.

#### Portainer

[https://www.portainer.io/](https://www.portainer.io/)

[https://www.portainer.io/get-started](https://www.portainer.io/get-started)

[https://docs.portainer.io/start/install-ce/server/swarm/linux](https://docs.portainer.io/start/install-ce/server/swarm/linux)

Contém versão paga (BE - Business Edition) e a grátis (CE - Community Edition) com alguns recursos a menos. Existe ainda uma outra opção que é a “3 Nodes Free”, que é a BE grátis com suporte até 3 nós.

Todas as versões atendem ao que se propõe o documento.

Alguns conceitos importantes e básicos sobre ambientes docker que são necessários saber:

* Imagens
* Containers
* Stacks
* Networks
* Volumes

Existem alguns conceitos e ferramentas de orquestração que serão importantes no futuro que compensa estudar sobre, porém não são essenciais para um início de ambiente, principalmente para desenvolvimento.

* Kubernets
* Swarm
* Rancher

O repositório contém vários arquivos de configuração (.yml) para a instalação dos recursos.

Opte por instalar os arquivos como stack dentro do portainer, pois assim será mais fácil fazer qualquer alteração se necessário.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPqb8GMG5DPR9EkPzed1VgC6VoU5w9CtNkdjlV-ER3utnD19iykHAVCoydk0OQK27IVDNlp-Z07o6Oe48W7UqLMo7SZTjl2wNBUGUZMbfrK3ztJleAQ6JbcaUCxxZBKd0mrhSG0w?key=NZsbhft-UgpfY2ZKTYnezWgM)

#### Clourflare

[https://www.cloudflare.com/pt-br/](https://www.cloudflare.com/pt-br/)

Este recurso não será instalado no servidor, mas sim configurado externamente para prover acesso aos recursos como em um ambiente profissional.

Quando você contrata um VPS, o acesso aos seus recursos são feitos através do IP  disponibilizado, porém, caso queira fazer o acesso por um nome de domínio, será preciso configurar um DNS, para assim acessar os recursos do servidor por algo como “[www.seudominio.com.br](http://www.seudominio.com.br)”. Este conceito daria um artigo extenso, portando vou apenas direcionar sobre o que fazer para que busque o conhecimento.

Para ter um domínio configurado:

* Registre um domínio [https://registro.br/](https://registro.br/)
* Faça o cadastro no Cloudeflare. [https://dash.cloudflare.com/sign-up?pt=f](https://dash.cloudflare.com/sign-up?pt=f)
* Registre os nameservers do Cloudeflare no registro.br

Com isto, você estará a caminho de ter um acesso aos recursos do seu host por um nome.

Os próximos passos serão instalar os recursos no host e fazer os registros no CloudFlare.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfOFBcrd33N4N1c5-cYYIvM-YA2Jqjdt_fQnxoF61HBi4nRauq574wFHNS6Y3Ym8uDlB3K_xs8f4JgbDY3u1cPKtdZ1s1AdqxmeAXFfzmjJhDrSWlKzPUz0TcUyvBu09Gv1wuBpCA?key=NZsbhft-UgpfY2ZKTYnezWgM)

#### Traefik

[https://doc.traefik.io/traefik/](https://doc.traefik.io/traefik/)

Traefik é um proxy de aplicativo de código aberto que torna a publicação de seus serviços uma experiência fácil e divertida. Ele recebe solicitações em nome do seu sistema e identifica quais componentes são responsáveis por tratá-las e as encaminha com segurança.

Dentro da nossa estrutura ele propicia que, serviços que estejam dentro de containers sejam expostos através de um nome configurado no DNS. Ainda conta com a facilidade de disponibilizar um certificado gratuito (https://letsencrypt.org/pt-br/) para o serviço de maneira fácil sem toda aquela configuração manual e complicada para usá-lo.

Na pasta “traefik” do repositório contém o arquivo de configuração da stack.

Juntamente é instalado um dashboard, onde alguns recursos podem ser monitorados.

É importante que a porta deste dashboard seja bloqueada no firewall e liberada apenas para seu IP, permitindo que só você o acesse.

Pesquise sobre firewall e bloqueios por IP.

Para saber o seu número de IP, consulte o site  [https://meuip.com.br/](https://meuip.com.br/)

Todos os fornecedores de host (VPS ou outro) contém este recursos de segurança.

O arquivo de configuração vem todo comentado, mas é altamente recomendável que expanda os conhecimentos sobre cada recurso para otimizações e evoluções futuras.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf85c5O88mlvxi5kv6uKzeyJHhKMC-5c1lJz5zgzcx5BxcydwteK4NKkgidIK6TBl9KOittb7aVq4ajv6L3KJzHvbtZdET3nGGFoTybgF1iD0BF2i0cD31fO2OcnzfVB75XR6sefg?key=NZsbhft-UgpfY2ZKTYnezWgM)

Todos os serviços que forem acessados através do Traefik precisam ser configurados para subir o container  e assim ser acessado por ele.

Como exemplo, temos uma configuração de servidor web.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfj1T3nD3Ip6fGs8EvxU9BI9v8GhqqUklIEVL4c8JdamNsIL6dhUh6aqbeu9Q7LLAuQG9vMoJ58B_4OpIYxWCy0eHt7mpELjPLLNZ-IRR2Tn8ub3pDJtS_wzUz4ys4K9yamRLYQUg?key=NZsbhft-UgpfY2ZKTYnezWgM)

#### Kafka

Mensageria refere-se ao uso de sistemas ou plataformas que permitem a troca de mensagens entre diferentes componentes de software, sistemas ou serviços. Esses sistemas atuam como mediadores, garantindo que as mensagens sejam entregues com eficiência, mesmo em casos de falhas temporárias nos sistemas de origem ou destino.

Soluções como RabbitMQ, Apache Kafka, AWS SQS, e Redis Streams são exemplos populares que oferecem recursos de mensageria para diferentes casos de uso. Para empresas, isso representa maior eficiência operacional e para os desenvolvedores, um ambiente mais organizado e resiliente.

É bom que desenvolvedores também estejam atentos e estudem esta tecnologia, pois muitas das soluções a tem como base, principalmente desenvolvimento de microsserviços.

Aqui implementamos uma solução baseada em Apache Kafka distribuída pela Confluent.

É amplamente escalável e usada no mercado.

O arquivo compose está na pasta “kafka” do repositório com os comentários.

Já conta com a configuração de acesso por IP e por nome, contendo as configurações necessárias do Traefik.

Para saber mais das configurações acesse:

[https://docs.confluent.io/platform/current/installation/docker/config-reference.html](https://docs.confluent.io/platform/current/installation/docker/config-reference.html)

[https://github.com/confluentinc/cp-docker-images/tree/5.3.3-post/examples](https://github.com/confluentinc/cp-docker-images/tree/5.3.3-post/examples)

[https://docs.confluent.io/platform/current/get-started/platform-quickstart.html](https://docs.confluent.io/platform/current/get-started/platform-quickstart.html)

Além do serviço de mensageria, são disponibilizadas configurações de aplicações que visam monitorar e simular mensagens.

* Control center, também da Confluente.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXffTHtflEEaSi2wL5XkebjTN0-LUvqYshnCpyGbCwbmlzdq_JNGDRD5mz44tE3T5ACysPfMJCECxqVNyHdsSUC_hg1JswkPR4OuZbqbMeOONMAeHwz0SsAez3Rtcb5fY2f5_KIHrA?key=NZsbhft-UgpfY2ZKTYnezWgM)

* UI for Apache Kafka

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfXtYLCoV7JlBSRcmbrkOrfN88eWWsedmB6NzRkuxtVsCSc_oJwpONZKPUSjHV8mbmeiEO2pcSyJoO6ssZ7C-FvUXxRxCj2TcKJsVxRZK9vwPlF5-kkVT8sGsUKubZcru1AgF2dtw?key=NZsbhft-UgpfY2ZKTYnezWgM)

Além destas aplicações instaladas no docker-compose, existem no repositório duas pequenas aplicações em Python, para demonstrar a produção e consumo de mensagens no serviço.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdwkY8v3QEd30CB0KXC5XTjxUoR9-98oO2KArH4rTPK5efcu_gvF3rl_BpUR7-A66DDXS9xhmnZfOCP6CvXTDvG7zAx4JW_X4oIHkkkt6n81vc7mat4LdpLaD3o6BNLxyDmgkYSLg?key=NZsbhft-UgpfY2ZKTYnezWgM)

#### Banco de dados PostgreSQL

[https://www.postgresql.org/](https://www.postgresql.org/)

[https://www.pgadmin.org/](https://www.pgadmin.org/)

Outro recurso que não pode faltar tanto para conhecimento dos desenvolvedores quanto para empresas são sistemas de gerenciamento de banco de dados.

No repositório contém um docker-compose para a instalação de um servidor de banco de dados PostgreSQL.

Também neste arquivo há uma aplicação que permite gerenciar o banco visualmente. Já com configuração de Traefik acessível por um nome configurado no CloudFlare.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSdt2iz3uLjz0ZYZ5V9YJfl9QDcV6OIEh4wgzZOJOH6Z83SqtHeL9oTyMesbhKoMlFdbCmXnOaTtcH-Zzq4UHlg8snJC6HGG-v5Xj4lmbgV8-rSabcXB-bV440MDV_fvR2jx2-Lw?key=NZsbhft-UgpfY2ZKTYnezWgM)

#### Servidor Web NgInx

https://nginx.org/

Servidor Web, já com configuração de nome e domínio, também com HTTPS configurado no Traefik. Lembrando é preciso  configurar um nome no Cloudflare.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeDjteHxHOd8o_Oi2bJwk56b3L2bmwSNOY6bXTqkLMztpjJu46J4qFIlK0mWJUYko-mpjOhalaHMJtyR97XGlrD_uoeEjFrmsVPzIc1theE1Cz2O-vqhtuxUEyuZRj_AmilV6pM0Q?key=NZsbhft-UgpfY2ZKTYnezWgM)



#### MinIO

https://min.io/https://nginx.org

Minio Aistor foi projetado para permitir que as empresas consolidem todos os seus dados em um espaço para nome de nuvem privada única. Arquitetado usando os mesmos princípios que os hiperescaladores, Aistor oferece desempenho em escala por uma fração do custo em comparação com a nuvem pública.

É uma plataforma de armazenamento de objetos de alta performance, compatível com o protocolo S3 da Amazon, projetada para armazenar grandes volumes de dados não estruturados.



Assim terminam as informações sobre esta configuração.
