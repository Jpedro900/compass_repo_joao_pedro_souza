# DESAFIOS COMPASS UOL SQL

## CASO DE ESTUDO BIBLIOTECA
*todos os desafios dessa seção seguirão o diagrama entidade-relacionamento abaixo*
![diagrama-entidade-relacionamento](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/229f11b4-2920-4850-8e9c-05019d5f7af8)

## DESAFIO 1
Apresente a query para listar todos os livros publicados após 2014. 
Ordenar pela coluna cod, em ordem crescente, as linhas.
Atenção às colunas esperadas no resultado final: *cod, titulo, autor, editora, valor, publicacao, edicao, idioma*.

~~~SQL
SELECT cod,titulo ,autor ,editora ,valor ,publicacao ,editora ,idioma 
FROM livro
WHERE publicacao > '2014-01-01'
ORDER BY cod 
~~~

## DESAFIO 2
Apresente a query para listar os 10 livros mais caros. 
Ordenar as linhas pela coluna valor, em ordem decrescente.
Atenção às colunas esperadas no resultado final: *titulo, valor*.

~~~SQL
SELECT titulo,valor
from livro
order by valor DESC
LIMIT 10
~~~

## DESAFIO 3
Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
O resultado deve conter apenas as colunas *quantidade, nome, estado e cidade*. 
Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

~~~SQL
with dados as(
	SELECT
  		en.estado,
  		en.cidade,
  		ed.codeditora
  	from endereco as en
  	left join editora as ed
  	on en.codendereco = ed.endereco
)
SELECT
	count(l.editora) as quantidade,
    ed2.nome,
    d2.cidade,
    d2.estado
from livro as l
LEFT join editora as ed2
ON l.editora = ed2.codeditora
LEFT join dados as d2
on l.editora = d2.codeditora
group by l.editora
ORDER by l.editora DESC
~~~

## DESAFIO 4
Apresente a query para listar a quantidade de livros publicada por cada autor.
Ordenar as linhas pela coluna *nome (autor), em ordem crescente*.
Além desta, apresentar as colunas *codautor, nascimento e quantidade (total de livros de sua autoria)*.

~~~SQL
SELECT 
	a.nome,
    a.codautor,
    a.nascimento,
    count(l.titulo) as quantidade
from autor as a
left join livro as l
on a.codautor = l.autor
GROUP by a.nome
ORDER by a.nome
~~~

## DESAFIO 5
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna *nome, em ordem crescente*.
Não podem haver nomes repetidos em seu retorno.

~~~SQL
WITH naosul as( 
SELECT
	ed.codeditora as codeditora,
	ed.endereco as endereco,
	en.estado as estado,
	en.cidade as cidade
FROM editora as ed
left join endereco as en
	on ed.endereco = en.codendereco
where en.estado NOT IN ('RIO GRANDE DO SUL','SANTA CATARINA','PARANÁ')
)
SELECT DISTINCT 
	autor.nome
FROM livro as li
left join naosul
on li.editora = naosul.codeditora
LEFT JOIN autor
on li.autor = autor.codautor 
WHERE naosul.codeditora is not NULL 
ORDER BY autor.nome 
~~~

## DESAFIO 6
Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas *codautor, nome, quantidade_publicacoes*.

~~~SQL
SELECT
	a.codautor ,
	a.nome ,
	COUNT(l.titulo) as quantidade_publicacoes
FROM livro as l
left join autor as a
	on l.autor = a.codautor 
GROUP BY a.nome 
ORDER by COUNT(l.titulo) DESC
LIMIT 1
~~~

## DESAFIO 7
Apresente a query para listar o nome dos autores com nenhuma publicação.
Apresentá-los em ordem crescente.

~~~SQL
SELECT 
	a.nome
FROM autor as a
left join livro as l
	on a.codautor = l.autor 
where l.publicacao is NULL
~~~

## CASO DE ESTUDO LOJA

## DESAFIO 8
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.
As colunas presentes no resultado devem ser, portanto, *cdvdd e nmvdd*.

~~~SQL
SELECT 
	tbvendedor.cdvdd,
	tbvendedor.nmvdd
FROM tbvendas
left join tbvendedor
	on tbvendas.cdvdd = tbvendedor.cdvdd 
WHERE status = 'Concluído'
GROUP BY tbvendedor.cdvdd
ORDER by COUNT(status) DESC 
LIMIT 1
~~~

## DESAFIO 9
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
As colunas presentes no resultado devem ser *cdpro e nmpro*.


~~~SQL
with mais_vendido as(
	SELECT 
		cdpro,
		nmpro,
		count(*) as numero_de_vendas
	from tbvendas
	WHERE status = 'Concluído'
	and dtven BETWEEN '2014-02-03' and '2018-02-02'
	GROUP BY nmpro
	ORDER BY numero_de_vendas desc
	LIMIT 1
)
SELECT 
    cdpro,
	nmpro
FROM mais_vendido
~~~

## DESAFIO 10
A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado.
O percentual de comissão de cada vendedor está armazenado na coluna *perccomissao*, tabela *tbvendedor*. 
Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
As colunas presentes no resultado devem ser *vendedor, valor_total_vendas e comissao*. 
O valor de comissão deve ser apresentado em *ordem decrescente arredondado na segunda casa decimal*.

~~~SQL
with vendastotais as(
SELECT
	vendedor.nmvdd as vendedor,
	SUM(vendas.vrunt*vendas.qtd) as valor_total_vendas
FROM tbvendas as vendas
left join tbvendedor as vendedor
	on vendas.cdvdd = vendedor.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendedor.nmvdd
)
SELECT 
	vendedor,
	valor_total_vendas,
	ROUND((valor_total_vendas*vendedor.perccomissao)/100,2) as comissao
FROM vendastotais
left join tbvendedor as vendedor
	on vendastotais.vendedor = vendedor.nmvdd 
ORDER BY comissao DESC with mais_vendido as(
	SELECT 
		cdpro,
		nmpro,
		count(*) as numero_de_vendas
	from tbvendas
	WHERE status = 'Concluído'
	and dtven BETWEEN '2014-02-03' and '2018-02-02'
	GROUP BY nmpro
	ORDER BY numero_de_vendas desc
	LIMIT 1
)
SELECT 
    cdpro,
	nmpro
FROM mais_vendido
~~~

## DESAFIO 11
Apresente a query para listar o código e nome cliente com maior gasto na loja.
As colunas presentes no resultado devem ser *cdcli, nmcli e gasto*, esta última representando o *somatório das vendas (concluídas) atribuídas ao cliente*.

~~~SQL
SELECT
	cdcli,
	nmcli,
	SUM(qtd*vrunt) as gasto 
FROM tbvendas as vendas
WHERE status = 'Concluído'
GROUP BY cdcli 
ORDER BY gasto DESC 
LIMIT 1
~~~

## DESAFIO 12
Apresente a query para listar *código, nome e data de nascimento* dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero).
As colunas presentes no resultado devem ser *cddep, nmdep, dtnasc e valor_total_vendas*.

~~~SQL
SELECT
	dep.cddep,
    dep.nmdep,
    dep.dtnasc,
    SUM(tbvendas.qtd*tbvendas.vrunt) as valor_total_vendas
FROM tbvendas
LEFT join tbdependente as dep
	on tbvendas.cdvdd = dep.cdvdd
where dep.cddep is not null
and tbvendas.status = 'Concluído'
group by tbvendas.cdvdd, dep.cddep
ORDER by valor_total_vendas 
LIMIT 1
~~~

## DESAFIO 13
Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).
As colunas presentes no resultado devem ser *cdpro, nmcanalvendas, nmpro e quantidade_vendas*.

~~~SQL
SELECT 
	cdpro,
	nmcanalvendas,
	nmpro,
	SUM(qtd) as quantidade_vendas 
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdpro, nmcanalvendas 
ORDER BY quantidade_vendas
~~~

## DESAFIO 14
Apresente a query para listar o gasto médio por estado da federação. 
As colunas presentes no resultado devem ser *estado e gastomedio*. 
Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
Observação: Apenas vendas com status concluído.

~~~SQL
SELECT 
	estado,
    round(avg(qtd*vrunt),2) as gastomedio
FROM tbvendas
WHERE status = 'Concluído'
and pais = 'Brasil'
GROUP by estado
ORDER BY gastomedio desc
~~~

## DESAFIO 15
Apresente a query para listar os códigos das vendas identificadas como deletadas. 
Apresente o resultado em ordem crescente.

~~~SQL
SELECT 
	cdven
FROM tbvendas
where deletado = '1'
ORDER BY cdven
~~~

## DESAFIO 16
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação.
As colunas presentes no resultado devem ser *estado e nmprod e quantidade_media*. 
Considere arredondar o valor da coluna quantidade_media na quarta casa decimal.
Ordene os resultados pelo estado (1º) e nome do produto (2º).
Obs: Somente vendas concluídas.

~~~SQL
SELECT 
	estado,
    nmpro,
    round(avg(qtd),4) as quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
and pais = 'Brasil'
GROUP by estado,nmpro
ORDER BY estado,nmpro
~~~
