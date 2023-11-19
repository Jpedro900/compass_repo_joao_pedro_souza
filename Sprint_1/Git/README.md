# Versionamento de código com Git

*Para esse curso, criei um repositório de teste chamada **teste_repo** o qual pode ser clonado pelo link abaixo para evitar a poluição desde repositório com movimentações desnecessárias*
`https://github.com/Jpedro900/teste_repo.git`

Apesar de já ter usado essa ferramente de versionamente anteriormente, nunca me aprofundei tanto assim em Git. Nesse curso entendi porque as empresas de tecnologia adotam tanto essa ferramenta para fazer o versionamento de seus programas.

O primeiro passo do curso foi aprender o que é versionamente de código, que basicamente consiste em contruir diferentes versões do mesmo para que assim se posssa testar novas funcionalidades de um código, sem que este esteja no código principal que estará em execução online.

Já o Git permite que esse versionamento seja feito online, facilitando assim que diferentes programadores tenham um acesso mais fácil e rápido ao código, facilitando assim a troca de ideias e otimizando o trabalho sob o mesmo.

Seguindo no curso aprendemos sobre as principais nomeclaturas do Git, como por exemplo:

* `REPOSITORIO` - Onde o código é armazenado;
* `BRANCHES` - Ramificações do nosso código fonte, usadas para que possamos trbalhar em diferentes versões do mesmo;
* `STASHS` - Pontos de salvamento de código, usados quando se quer excluir uma parte do código , porém talvez recuperá-la futuramente;
* `TAGS` - Pontos de salvamento de código, usados para quando relamente queremos salvar um progresso feito no código.

Nesse mesmo módulo também aprendi a como iniciar e configurar um repositório novo no Git, através de uma série de comandos mostrados a seguir;

* `git init` - Inicializa o repositório atual;
* `git add README.md` - Adiciona um arquivo README.md no repositório atual;
* `git commit -m "first commit"` - Cria a primeira commit do repositório, utilizando a tag -m para enviar a mensagem "first commit";
* `git branch -M main` - Cria a branch main, a branch principal do repositório;
* `git remote add origin <LINK>` - Adiciona o ponto de origem remoto do nosso repositório através do link do mesmo;
* `push -u origin main` - Envia os arquivos para a origem do projeto.

Após isso fui ensinado a usar a função `git remote` para fazer o gerenciamento da origem do projeto, ou seja, esocolher um repositorio pra ser o repositorio remoto do projeto ou para alterar o mesmo.

Ao trabalhar com submódulos, que nos permite ter 2 ou mais projetos ao mesmo tempo, praticamente, percebi ser bastante útil para o caso de querer criar diversos projetos dentro do prjeto principal. Para a criação do mesmo, após criar um repositório, usamos o comando `git submodule add <LINK DO REPOSITÓRIO><NOME DO SUBMÓDULO>` para adicioná-lo ao projeto atual como um submódulo, e para a visualização de todos os submódulos criados usamos o comando `git submodule`.

Para atualizar um submódulo usamos o comando `git push --resurse-submodules=on-demand`, o que fará a atualização apenas do submódulo onde estivermos.

As próximas seções foram mais focadas em partes mais avançadas e espefícias do Git como a utilização do `git show` para sabermos o que há de diferente em outros branchs ou tags em comparação com a branch main. Outro comando também utilizado para comparação de branchs é o `git diff`, que é utilizado para exibir as diferenças da branch em relação ao remoto ou para comparação de duas branchs específicas. Também aprendi sobre o `git shortlog` que exibe um relatório resumido do projeto, onde os commit são unidos pelo nome de seus autores, para assim termos uma noção de quais commits foram enviados ao repositório.

Nessa próxima seção foram mostrados comandos de limpeza e organização de repositório, para que assim possamos garantir uma organização melhor sob os commmits.

Os comandos mostrados foram:

* `git clean` - Para rastrear e apagar arquivos que não estão sendo trackeados pelo repositório;
* `git gc` - Para apagar arquivos que não são julgados como necesários para o funcionamento da aplicação(Como um garbage collector);
* `git fsck` - Para verificar se há arquivos com possíveis corrupções;
* `git reflog` - Para mapear TODOS os passos no repositório, incluindo mudanças de branchs feitas;
* `git archive --format.zip --output master_files.zip master` - Para fazer uma cópia local em formato `.zip` de nosso repositório.

A seguir foram ensinados bons costumes quanto a criação de commits com certos padrões, começando mostrando como commits sem sentido podem atrapalhar o andamento do projeto e como evitá-los. Tambem aprendemos a como "excluir" esses commits desnecessários, mesclando-os a outros commits mais relevantes através do comando `git rebase <atual> <funcionalidade> -i`. Após esse comando podemos escolher quais commits irei excluir(`squash`) e quais renomear(`reword`), caso necesário.

Recomendação de padronização de boas mensagens de commit:

* Separar o **assunto** do corpo da mensagem;
* Assunto com no **máximo 50 caracteres**;
* Assunto com **letra inicial maiúscula**;
* Corpo com no **máximo 72 caracteres**;
* Explicar o **por que e como** do commit, e não como o código foi inscrito.

A seguir, aprendi sobre como o GitHub funciona e como usar sua interface para criação e admnistração de repositórios. Começando com a criação dele, na qual optei pela adição de um arquivo *.gitignore* no padrão *node* para ignorar a inserção de arquivos desnecessários ou particulares ao repositório e um arquivo *LICENSE* no padrão *MIT* que irá mostrar para outros usuários onde eles podem ou não mexer no código de nossa aplicação, como mostrado na imagem abaixo:

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/bf1c58e6-a48c-4be0-b447-589eee245317)

Na aba Code(Imagem abaixo) podemos executar várias funções importantes para o repositório, como visualizar os arquivos do repositório, alternar e criar branches e tags, adicionar um novo arquivo ou diretório, ir para um arquivo específico, conseguir o link para clonar o repositório, entre outros.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/6ab84872-4982-4455-b223-fb683b14827a)

Na aba Issues podemos criar tarefas ou reportarmos possíveis bugs do projeto, organizados como um projeto Jira, o que o torna muito interessante para a organização do que se deve fazer/corrigir no reposiório.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/75d62f08-9619-4745-b988-8bf2f1f46b24)

A aba Pull Requests permite que os colaboradores do projeto enviem códigos para resolver uma issue ou adicionar novas funcionalidades do sistema. O objetivo dessa aba é fazer com que um código passe por uma avaliação antes de ser inserida na *branch main* ou voltar para modificações.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/a0a16579-50ae-48c4-b6d4-e0ffa3921622)

Na aba Actions podemos criar automatizações do deploy com integração em outros serviços, o que também inclui CI/CD(Continuous Integration/Continuous Development), ou seja, para criar uma rotina de atualização da master e diversos outros processos. Essas automatizações são geralmente criadas por DevOps ou gerentes de projeto.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/4fc20b0f-31dd-4f6f-9f53-5eef77979719)

A seguir foi ensinado o básico da criação de projetos no GitHub pela aba Projetcs, onde podemos criar um novo projeto e utilizar um quadro de tarefas e formato Kanban, dispensando assim a necessidade do uso de plataformas como o TRELLO e a centralização do gerenciamento das atividades pelo GitHub.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/9aa1cc9b-0616-40c7-b53e-f8ad2d2c6458)

A aba Wiki é a onde podemos criar a documentação do projeto de forma mais detalhada, falando melhor acerca de funcionalidades, bugs conhecidos e não solucionados, etc. A ideia é criar um repositório de conhecimento do projeto, quase como uma biblioteca para que possamos entender mais detalhadamente como funciona nossa aplicação.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/6806bc4f-4fba-45fa-ae76-af4669f033a9)

Foi falado um pouco sobre a aba Insights, embora nós progrmadores não temos a necessidade de olhar muito ela. Mas nela podemos ter informações mais detalhadas do projeto como: *contribuidores, commits, forks, etc.* Ela é uma aba muito utilizada para entender como está o andamento do projeto e sua evolução desde o início.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/df94ccb3-9330-4363-baca-3aa54e51945b)

A aba Settings é onde conseguimos fazer as configurações do reporsitório, como alterar o nome do mesmo, adicionar/remover features, adicionar ou remover colaboradores, etc. Também é a aba onde podemos deletar o repositório.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/b2036df6-6f82-4af9-b9ec-2ddf93ae23f6)

Falando um pouco sobre Gists, aprendi que são pequenos blocos de código que podem ser hospedados no GitHub também, eles também servem para armazenar uma solução que achamos interessante para algum pblima e não pqueremos perde-la. O link do Gist pode ser compartilhado. Se for pensar num todo, o gist pode ser considerado um repositório também porém com apenas um arquivo que seria uma solução para algum problema surgido em um projeto.

Para finalizar, o curso me ensinou algumas formas de formatação de um arquivo Markdown. Abaixo mostrarei algumas das utilidades dessa lingagem de marcação de texto.












