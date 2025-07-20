# Algoritmos Avançados
Este repositório reúne estudos, implementações e anotações sobre Algoritmos e Estruturas de Dados Avançados. O objetivo é aprofundar o conhecimento em temas fundamentais sobre programação.

## Estrutura de Dados: Trie (Árvore Prefixada)

Uma das estruturas de dados implementadas neste repositório é a **Trie**, também conhecida como **árvore prefixada**. Ela é ideal para operações de **autocomplete**, **busca por prefixo** e **verificação de palavras**.

### Aplicação prática

Neste projeto, a Trie foi utilizada para criar uma funcionalidade de **autocompletar nomes de produtos em uma aplicação Django**.  
Em vez de realizar buscas no banco de dados com `LIKE` ou `icontains`, que podem ser ineficientes em grandes volumes de dados, a Trie permite buscas rápidas em memória com **complexidade proporcional ao tamanho do prefixo**, e não ao tamanho da base de dados.

### Funcionamento

- Cada nó da Trie representa um caractere.
- As palavras são inseridas caractere por caractere.
- Ao final de cada inserção, o nó é marcado como fim de palavra.
- A busca por prefixo percorre apenas os nós necessários e retorna sugestões limitadas de forma ordenada.

### Vantagens

- **Eficiência**: Evita consultas pesadas no banco.
- **Escalabilidade para autocomplete**: Excelente performance para sistemas que exigem resposta em tempo real.
- **Organização clara**: Separação entre lógica de busca e persistência de dados.
