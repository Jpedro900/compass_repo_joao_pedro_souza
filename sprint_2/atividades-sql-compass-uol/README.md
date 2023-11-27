# DESAFIOS COMPASS UOL SQL
*todos os desafios dessa seção seguirão o diagrama entidade-relacionamento abaixo*
![diagrama-entidade-relacionamento](https://github.com/Jpedro900/compass_repo_joao_pedro_souza/assets/127545539/229f11b4-2920-4850-8e9c-05019d5f7af8)

## DESAFIO 1
Apresente a query para listar **todos** os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.
Atenção às colunas esperadas no resultado final: *cod, titulo, autor, editora, valor, publicacao, edicao, idioma*

~~~SQL
SELECT cod,titulo ,autor ,editora ,valor ,publicacao ,editora ,idioma 
FROM livro
WHERE publicacao > '2014-01-01'
ORDER BY cod 
~~~

## DESAFIO 2
