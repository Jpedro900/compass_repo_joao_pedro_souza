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
FROM <nome_da_tabela>
WHERE <condição> = <resultado_esperado>
~~~

### ORDER BY
Serve para ordenar a seleção de dados de acordo com uma regra definida pelo usuário, usando ASC para a ordem crescente e DESC para a ordem decrescente. 

~~~SQL
SELECT <coluna_1>,<coluna_2>,...
FROM <nome_da_tabela>
ORDER BY <coluna_1>(ASC)(DESC)
~~~

### LIMIT
Serve para limitar o número de linhas de cada consulta em *n* linhas. É muito utilizado na etapa de **exploração dos dados**.

~~~SQL
SELECT <coluna_1>,<coluna_2>,...
FROM <nome_da_tabela>
LIMIT n
~~~

## OPERADORES

### OPERADORES ARITMÉTICOS:
Servem para executar operações matemáticas e são muito utilizados para criar colunas calculadas.

* `+ : Adição`
* `- : Subtração`
* `* : Multiplicação`
* `/ : Divisão`
* `^ : Exponencial`
* `% : Módulo`
* `|| : Soma de strings`

### OPERADORES DE COMPARAÇÃO
Servem para comparar dois valores, retornando TRUE ou FALSE. São muito utilizados em conjunto a função WHERE para filtrar linhas de uma seleção.

* `=	: Igual à`
* `>	: Maior que`
* `<	: Menor que`
* `>=	: Maior ou igual que`
* `<=	: Menor ou igual que`
* `<>	: Diferente de`

### OPERADORES LÓGICOS
Servem para unir expressões simples em uma composta.

* `AND : TRUE se todos as condições separadas por AND forem TRUE`
* `OR : TRUE se alguma condição separada por OR for TRUE`
* `NOT : TRUE se a condição mencionada anteriormente não for TRUE`
* `BETWEEN : TRUE se o operando estiver dentro do intervalo comparativo`
* `IN : TRUE se o operando for igual a algum item de uma lista`
* `LIKE : TRUE se o operando corresponder a um padrão determinado`
* `ILIKE : Igual ao LIKE mas desconsidera letras maiúsculas e minúsculas`
* `IS NULL : TRUE se a condição for igual a NULL`

## FUNÇÕES AGREGADAS
Essas funções são usadas para executar operações aritméticas nos registros de uma coluna:

### COUNT()
Serve para contar as linhas de uma coluna.

~~~SQL
SELECT COUNT(<coluna_1>)
FROM <nome_da_tabela>
~~~

### SUM()
Serve para somar todos os valores de uma coluna.
~~~SQL
SELECT SUM(<coluna_1>)
FROM <nome_da_tabela>
~~~

### MIN()
Serve para exibir o valor mínimo encontrado em uma coluna.

~~~SQL
SELECT MIN(<coluna_1>)
FROM <nome_da_tabela>
~~~

### MAX()
Serve para exibir o valor máximo encontrado em uma coluna.

~~~SQL
SELECT MAX(<coluna_1>)
FROM <nome_da_tabela>
~~~

### AVG()
Serve para exibir o a média de uma coluna.

~~~SQL
SELECT AVG(<coluna_1>)
FROM <nome_da_tabela>
~~~

### GROUP BY
Serve para agrupar registros semelhantes de uma coluna. Normalmente utilizado em conjunto com as **funções agregadas**.

~~~SQL
SELECT coluna_1, COUNT(<coluna_2>)
FROM <nome_da_tabela>
GROUP BY coluna_1
~~~

### HAVING
Serve para filtrar as linhas de uma seleção por uma coluna agrupada, parecido com a função WHERE. Porém a função WHERE não pode ser usada com um coluna agrupada.

~~~SQL
SELECT COUNT(<coluna_1>)
FROM <nome_da_tabela>
HAVING COUNT(*) > 100
~~~

## JOINS
