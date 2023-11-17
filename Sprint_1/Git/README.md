# Versionamento de código com Git

Apesar de já ter usado essa ferramente de versionamente anteriormente, nunca me aprofundei tanto assim em Git. Nesse curso entendi porque as empresas de tecnologia adotam tanto essa ferramenta para fazer o versionamento de seus programas.

O primeiro passo do curso foi aprender o que é versionamente de código, que basicamente consiste em contruir diferentes versões do mesmo para que assim se posssa testar novas funcionalidades de um código, sem que este esteja no código principal que estará em execução online.

Já o Git permite que esse versionamento seja feito online, facilitando assim que diferentes programadores tenham um acesso mais fácil e rápido ao código, facilitando assim a troca de ideias e otimizando o trabalho sob o mesmo.

Seguindo no curso aprendemos sobre as principais nomeclaturas do Git, como por exemplo:

* `REPOSITORIO` - Onde o código é armazenado;
* `BRANCHES` - Ramificações do nosso código fonte, usadas para que possamos trbalhar em diferentes versões do mesmo;
* `STASHS` - Pontos de salvamento de código, usados quando se quer excluir uma parte do código , porém talvez recuperá-la futuramente;
* `TAGS` - Pontos de salvamento de código, usados para quando relamente queremos salvar um progresso feito no código.

Nesse mesmo módulo também aprendi a como iniciar e configurar um repositório novo no Git, através de uma série de comandos mostrados a seguir;

* `git init` - Inicializa o repositório atual
* `git add README.md` - Adiciona um arquivo README.md no repositório atual
* `git commit -m "first commit"` - Cria a primeira commit do repositório, utilizando a tag -m para enviar a mensagem "first commit"
* `git branch -M main` - Cria a branch main, a branch principal do repositório
* `git remote add origin <LINK>` - Adiciona o ponto de origem remoto do nosso repositório através do link do mesmo
* `push -u origin main` - Envia os arquivos para a origem do projeto



