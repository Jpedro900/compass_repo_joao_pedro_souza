# SQL - DATABASE

Neste curso aprenderei sobre como criar e manusear tabelas em um banco de dados através da linguagem SQL, desde seus princípios básicos até partes mais avançadas.

Todo o curso seguirá o banco de dados cujo diagrama está representado abaixo:

![diagrama-de-classes](diagrama-de-classes.PNG)

## COMANDOS BÁSICOS

###SELECT
Serve para selecionar colunas de uma tabela.

~~~SQL
SELECT <coluna_1>,<coluna_2>,...
FROM <nome_da_tabela>
~~~

### DISTINCT
Serve para remover linhas duplicadas e mostrar apenas linhas distintas de uma tabela. 
Muito usado na etada de **exploração das bases**.

~~~SQL
SELECT DISTINCT <coluna_1>,<coluna_2>,...
FROM <nome_da_tabela>
~~~

### WHERE
Serve para filtrar as linhas de uma tabela de acordo um um condição criada.

~~~SQL
SELECT <coluna_1>,<coluna_2>,...
FROM <nome da tabela>
WHERE <condição> = <resultado_esperado>
~~~

### ORDER BY
Serve para ordenar a seleção de dados de acordo com uma regra 
