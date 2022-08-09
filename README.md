# Docker E-mail com Workers

Aplicação envia e-mails com frontend Nginx com página HTML simples, backend em python enfileirar os requests para envio e salva as mensagens em um banco de dados postgres.

1. Criado banco de dados em postgres
2. Efetuado mapeamento dos arquivos locais para os serviços.
3. Criado app para enfileirar os e-mails
4. Configurado a única forma de recebimento de request é pelo frontend no index.HTML
5. Segmentado as redes para comunicação entre os serviços.
6. Setado a orquestração dos serviços para a inicialização correta.
7. Configurado Redis para organizar e consumir a fila de e-mails a serem enviados.
8. Escalado os serviços de envio de e-mail do Redis de forma suprir a necessidade com uma imagem personalizada.
9. Set variáveis de ambiente no docker-compose para serviço 'app' e 'worker'.
10. Criado o arquivo 'docker-compose.override' com as variáveis de ambiente corretas para iniciar os serviços.

Execução da Aplicação:
Premissa: ter docker instalado.

1. Executar docker em modo deamon '-d' e '--scale nome_serviço quantidade_serviços' nome_serviço referente ao criado no docker_compose.yml

``` docker compose up -d --scale worker=3 ```

2. Executar para testar o banco 

``` docker compose exec db psql -U postgres -f /scripts/check.sql ```




Verificar a execução de todos os serviços.

``` docker compose logs -f -t ```

Verificar o banco de dados com as mensagens salvar

``` docker compose exec db psql -U postgres -d email_sender -c 'select * from emails' ```

Encerrar a execução dos serviços.

``` docker compose down ```
