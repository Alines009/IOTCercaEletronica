# IOTcercaEletronica
 Aplicação IoT que possui a finalidade de monitorar se um veículo está distante da sua rota principal. Caso isso aconteça, o usuário é notificado através de uma mensagem  enviada por um bot no Telegram. 


**Pré-requisitos:**
 * Instalar o Python 3 e o pip;
 * Realize o download dos aplicativos Sensorstream IMU+GPS e Fake GPS no seu celular;
* Execute os seguintes comandos para a instalação dos pacotes:
     ** pip install Django
     ** pip install geopy
     ** pip install paho-mqtt
     ** pip install python-telegram-bot

**Para executar a aplicação:**
 * Após clonar o repositório, execute os seguintes comandos dentro do diretório que contém cada arquivo:
     py manage.py runserver - Inicia a aplicação Django;
     py main.py - Responsável pela coleta das informações enviadas pelo celular, cálculo das distâncias e envio dos dados para o Broker HIVEMQ;
     py consumerMQTT.py - Recebe as informações do broker HIVEMQ;
     py telegramBot.py - Inicia a execução do bot no Telegram.
 * Acesse a aplicação Django através da URL disponibilizada (A URL padrão é  http://127.0.0.1:8000/);
 * Selecione ordenadamente os locais por onde o seu veículo irá passar, incluindo o local de partida e chegada. Estes locais são chamados de checkpoints;
 * Clique no botão “Confirme seus checkpoints”;
 * Inicie uma conversa no Telegram com o bot NotificationBot (@GPSNotification_bot) inserindo o comando “/start”. Para iniciar o monitoramento do veículo, utilize o comando “/monitor”;
 * Abra o aplicativo  SensorstreamIMU+GPS e ative as opções “GPS Position” e “Include User-Checked Sensor Data in Stream” apresentadas na aba “Toggle Sensors”;
 * Em “Preferences”, insira o seu endereço IP, a porta 5556 e selecione a opção UDP Stream. Inicie a stream;
 * Caso a página http://127.0.0.1:8000/rastrear seja atualizada, será possível visualizar a localização atual do veículo;
 * Acesse o aplicativo Fake GPS e altere a sua localização para alguma área mais distante;
 * Aguarde a notificação do bot e acesse a página http://127.0.0.1:8000/rastrear.
