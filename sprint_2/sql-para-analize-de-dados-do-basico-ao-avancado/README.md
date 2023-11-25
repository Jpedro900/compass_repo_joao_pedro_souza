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
Joins são comandos em SQL que fazem dessa uma linguagem tão poderosa, conseguindo relacionar múltiplas tabelas de maneira fácil e rápida.

### LEFT JOIN
Com o *left join*, pegamos todos os dados da tabela a esquerda e relacionamos eles apenas aos dados da tabela a direita que deem match com eles, sendo a tabela a esquerda a primeira a ser declarada na busca.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/f5bd982b-5177-4906-a23c-b868711fabdf)

~~~SQL
SELECT t1.<coluna_1>,t2.<coluna_2>
FROM <nome_da_tabela> as t1
LEFT JOIN <nome_da_tabela> as t2
      ON t1.<coluna_1> = t2.<coluna_2>
~~~

### RIGHT JOIN
O *right join* funciona de maneira semelhante ao *left join* porém vamos pegar todos os dados da tabela a direita e apenas os dados que deram match da tabela a esquerda.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/ff57933b-afb2-429a-aca9-c07085e7b410)

~~~SQL
SELECT t1.<coluna_1>,t2.<coluna_2>
FROM <nome_da_tabela> as t1
RIGHT JOIN <nome_da_tabela> as t2
      ON t1.<coluna_1> = t2.<coluna_2>
~~~

### INNER JOIN
Com o *inner join*, pegamos todos os dados que deem match entre as duas tabelas.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/06660983-c6d5-4c4d-8cc3-17860c08bd26)

~~~SQL
SELECT t1.<coluna_1>,t2.<coluna_2>
FROM <nome_da_tabela> as t1
INNER JOIN <nome_da_tabela> as t2
      ON t1.<coluna_1> = t2.<coluna_2>
~~~

### FULL JOIN
Com o *full join*, pegamos todos os dados das duas tabelas.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/b4f5805a-914d-499a-95b9-4fad01547c63)

~~~SQL
SELECT t1.<coluna_1>,t2.<coluna_2>
FROM <nome_da_tabela> as t1
FULL JOIN <nome_da_tabela> as t2
      ON t1.<coluna_1> = t2.<coluna_2>
~~~

## UNIONS
Serve, basicamente, para colar uma tabela sobre outra, desde que ambas tenham o memso número de colunas e que essas tenham o mesmo tipo de dados.

### UNION ALL
Cola a tabela_2 na tabela_1 sem excluir lnhas duplicadas.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/0dba475a-72e7-4bd7-aeb9-242e95eb87e9)

~~~SLQ
SELECT * FROM <tabela_1>
UNION ALL
SELECT * FROM <tabela_2>
~~~

### UNION 
Cola a tabela_2 na tabela_1 excluindo linhas dupicadas.

![image](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/27ff619b-e2ce-4860-953d-7c17ac95ff86)

~~~SLQ
SELECT * FROM <tabela_1>
UNION ALL
SELECT * FROM <tabela_2>
~~~

## SUBQUERIES
Servem para consultar dados de outras consultas. As subqueries são baiscamente 4:

* `Subquerie no WHERE`
* `Subquerie no WITH`
* `Subquerie no FROM`
* `Subquerie no SELECT`

## TRATAMENTO DE DADOS 
### CONVERSÃO DE UNIDADES
Para converter unidades em SQL usamos dois operadores

* `:: - Usado na maioria dos casos`
* `CAST - Usado quando o primeiro operador não funcionar`

#### LISTA DE UNIDADES GERAIS

* `int : Valor inteiro`
* `numeric : Valor numerico preciso`
* `float : Valor numerico quebrado (com várias casas decimais)`
* `money : Valor em moeda`
* `date : Valor em data`
* `timestamp : Valor em data e hora`
* `text : Valor em texto`

#### LISTA DE UNIDADES DE DATA

* `day : Retorna o dia do mês. Vai de 1 à 31`
* `month : Retorna o mês do ano. Vai de 1 à 12`
* `week : Retorna a semana do ano. Vai de 1 à 53`
* `year : Retorna o ano da data`
* `dow : sigla para "day of week". Vai de 0 (domingo) e vai a 6 (sábado)`

~~~SQL
SELECT '2021-10-01'::date - '2021-02-01'::date
~~~
Converte os valores de texto para data e mostra quantos dias há entre as duas datas apresentadas

### TRATAMENTO DE DADOS GERAL
#### CASE WHEN
Serve para executar funções específicas de acordo com uma condição determinada.

~~~SQL
SELECT <nome_da_coluna>,
  CASE
    WHEN <condição_1> then '<texto_mostrado>'
    WHEN <condição_2> then '<texto_mostrado>'
    .
    .
    .
    END AS <nome_da_nova_coluna>
FROM <nome_da_tabela>
~~~

#### COALESCE
Serve para fazer o tratamento de dados nulos

~~~SQL
SELECT *,
  COALESCE(<nome_da_coluna_1>,<nome_da_coluna_1>,<nome_da_coluna_1>)
FROM <nome_da_tabela>
~~~

### TRATAMENTO DE TEXTO

* `LOWER() : Reescreve todo o texto em letras minúsculas`
* `UPPER() : Reescreve todo o texto em letras maiúsculas`
* `TRIM() : Deleta espaços das extremidades de um texto`
* `REPLACE() : Subistitui uma string por outra`

### TRATAMENTO DE DATA E HORA

* `INTERVAL : Utilizado para somar datas na unidade desejada`
~~~SQL
SELECT CURRENT_DATE + INTERVAL '10 weeks' //Soma 10 semanas a data atual
SELECT CURRENT_DATE + INTERVAL '10 months' //Soma 10 meses a data atual
SELECT CURRENT_DATE + INTERVAL '10 hours' //Soma 10 horas a data atual
~~~
* `DATE_TRUNC : Mostra unidade requerida de cada data da coluna selecionada`
~~~SQL
SELECT
  DATE_TRUNC('month', <nome_da_coluna>) //Mostra mês de cada data da coluna selecionada
FROM <nome_da_tabela>
~~~
* `EXTRACT : Mostra a unidade requerida da data selecionado`
~~~SQL
SELECT
  EXTRACT('dow' from '2022-01-30'::date) //Mostra o dia da semana do data selecionado
FROM <nome_da_tabela>
~~~
* `DATEDIFF : Calcula a diferença entre duas datas na unidade requerida (NÃO PODE SER USADO NO POSTGRE)`
~~~SQL
SELECT
  DATEDIFF('weeks','2018-06-01',current_date)
FROM <nome_da_tabela>
~~~

+

