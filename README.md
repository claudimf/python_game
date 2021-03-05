# Python Game

👋 Olá, Seja Bem-vindo(a) ao 'Python Game'.

# Projeto 'Python Game' do curso [Python 3 parte 1: Introdução à nova versão da linguagem](https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem)

# Aulas

<details>
    <summary>Introdução e Instalação do Python 3</summary>
    <ul>
        <li>Introdução</li>
        <li>Instalando o Python no Windows</li>
        <li>Instalando em outras plataformas</li>
        <li>Usar o Python sem instalá-lo</li>
        <li>Função print e variáveis</li>
        <li>Imprimindo uma mensagem na tela</li>
        <li>Personalizando a saída</li>
        <li>Imprimindo datas</li>
        <li>Tipagem do Python</li>
        <li>Qual o tipo da variável?</li>
        <li>Tipagem de variáveis</li>
        <li>Para saber mais: Snake_Case</li>
    <ul>
</details>

<details>
    <summary>Lidando com a entrada do usuário</summary>
    <ul>
        <li>Instalando e conhecendo o PyCharm</li>
        <li>Mão na massa: Primeiro projeto com PyCharm</li>
        <li>Comparando variáveis</li>
        <li>Impossível acertar o número</li>
        <li>Onde foi que ela errou?</li>
        <li>Comparação estranha</li>
        <li>O resultado da soma é...</li>
        <li>E o resultado agora?</li>
        <li>Diferenças entre o Python 2 e o Python 3</li>
        <li>Python 2 vs Python 3 - #1</li>
        <li>Python 2 vs Python 3 - #2</li>
        <li>Para saber mais: JavaScript vs Python</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>Testando valores</summary>
    <ul>
        <li>A condição elif</li>
        <li>Faixa Etária</li>
        <li>Faixa Etária - Variáveis</li>
        <li>If..else. e nada funciona!</li>
        <li>Mão na massa: Dando dicas</li>
        <li>Qual é o tipo?</li>
        <li>Para saber mais: if sem ou com parênteses?</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>A sequência do jogo</summary>
    <ul>
        <li>O laço com while</li>
        <li>Resultado do programa</li>
        <li>if e while</li>
        <li>Formatação de strings</li>
        <li>Testando formatação</li>
        <li>Mão na massa: Usando while</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>Iterando de maneira diferente</summary>
    <ul>
        <li>O laço com for</li>
        <li>De while para for</li>
        <li>De while para for #2</li>
        <li>Encerrando a interação e o loop</li>
        <li>break e continue</li>
        <li>while com break</li>
        <li>for com continue</li>
        <li>Mão na massa: Usando for</li>
        <li>Para saber mais: Formatação de strings</li>
        <li>Adaptando o Padrão Americano</li>
        <li>O resultado da interpolação</li>
        <li>Interpolação - Python 2 vs Python 3</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>Gerando números aleatórios</summary>
    <ul>
        <li>Gerando e arredondando um número aleatório</li>
        <li>Importar módulo</li>
        <li>Definindo um intervalo para a geração de números aleatórios</li>
        <li>O menor e o maior</li>
        <li>Múltiplos aleatórios</li>
        <li>O grande sorteio</li>
        <li>Mão na massa: Número secreto aleátorio</li>
        <li>Para saber mais: Pseudo-Random</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>Nível e Pontuação</summary>
    <ul>
        <li>Adicionando níveis ao jogo</li>
        <li>Definindo uma pontuação para o usuário</li>
        <li>Funções built-in</li>
        <li>Dividindo pontos</li>
        <li>Mão na massa: Níveis e Pontuação</li>
        <li>Para saber mais: arredondar no Python 2 e no Python 3</li>
        <li>Para saber mais: Divisão de float e integer</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>Organizando ainda melhor o nosso código</summary>
    <ul>
        <li>Importando arquivos dentro de outros</li>
        <li>Criando funções para os nossos jogos</li>
        <li>Declarando funções</li>
        <li>Importação de módulo</li>
        <li>Importação de módulo, mas um pouco diferente</li>
        <li>Diferenciando um arquivo executado de um importado</li>
        <li>Um módulo pode se chamar automaticamente?</li>
        <li>Mão na massa: Modularizando o jogo</li>
        <li>Download do jogo</li>
        <li>Arquivos do projeto atual</li>
    <ul>
</details>

<details>
    <summary>Comparando Python com C</summary>
    <ul>
        <li>Python vs C</li>
        <li>Interpretado vs Compilado</li>
        <li>Python é interpretado ou compilado?</li>
        <li>Download e considerações finais</li>
    <ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Exemplos de formatação de strings](https://docs.python.org/3/library/string.html#formatexamples)