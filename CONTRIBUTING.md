# Contributing

Contribuições sempre serão bem-vindas, sejam pequenas ou grandes. Veja Abaixo como contribuir conosco.


## Código de Conduta

Antes de fazer qualquer contrubuição é necessario que você leia atentamente o nosso [código de conduta](./CODE_OF_CONDUCT.md), nele está descrito comportamentos apreciados e não tolerados em nossa comunidade.


## Tipos de Contribuição

### Resolvendo Issues

Issues são usadas para requisitar novas funcionalidades, mudanças ou resolução de problemas. Sinta-se livre para tirar duvidas e discutir novas ideias, tenha em mente que o tema sempre deve ter relação com o projeto.

## Como Contribuir?

### 1. Escolha uma *Issue*

O primeiro passo é escolher uma issue em que você deseja contribuir. É importante deixar claro que você está trabalhando nela, para que todos saibam o que está sendo feito e o que falta começar. Se quiser contribuir para algo que não é uma issue ou apenas recomendar que algo seja feito, sinta-se livre para abrir um nova issue (lembre-se de descrevê-la da melhor maneira possível).

### 2. Crie o seu *Fork*

O segundo passo é criar um fork do Margaret. Vá até o [repositório](https://github.com/OpenDevUFCG/Margaret) e aperte o botão *Fork* no canto superior direito da página. Quando o GitHub terminar de processar, copie o url do seu fork.

### 3. Clone o repositório

Com o fork criado, iremos clonar o repositorio. Este processo é feito através de terminal com o comando `git clone`

```sh
git clone <url do seu fork>
```
Agora existe um diretório Margaret no seu computador.

### 4. Produza conteúdo

Crie e mude o que quiser e achar útil para a issue que escolheu. 

### 5. Commite as modificações

Chegou o momento de dar commit na sua mudanças, ou seja, levar o que você fez até o repositório remoto.

Entre no repositório do Margaret:

```sh
cd Margaret
```
Adicione as mudaças `git add`. Isso adiciona tudo que foi feito de uma só vez.

```sh
git add . 
```

Dê commit nas mudaças usando `git commit`, o modificador `-m` server para adicionar uma mensagem de maneira direta pelo terminal.

```sh
git commit -m "<sua_mensagem_de_commit>"
```

Envie todos os comites para o repositório com `git push`.
```sh
git push origin master
```
Arrasou! Agora tudo que você fez ja está disponivel no seu fork online.

### 6. Crie uma PR

Com as modificações no seu fork, chegou o momento de mandá-las para o Margaret, para isso utilizamos o **Pull Request**.

Vá até a página do seu fork e clique no botão **New Pull Request**. A página exibida em sequêcia possui seus commits, clique no botão **Create Pull Request** e preencha os campos de texto. Agora só confirmar e esperar alguém da equipe revisar sua PR.


## Recomendações e Links Úteis

- Caso sinta difículdade em alguma parte do processo ou tenha dúvidas, não hesite em contatar os Maintainers do projeto.
- [Sobre OO em Python](https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython)
- [Guia iniciante sobre Open Source](https://dev.to/opendevufcg/contribuindo-para-projetos-open-source-com-github-3i76)
- Sobre Git e GitHub:
  - [Guia parte 1](https://medium.com/@Juliobguedes/entendendo-git-883464f379de)
  - [Guia parte 2](https://medium.com/@Juliobguedes/entendendo-git-branches-parte-2-3778f4258843)
  - [Para mais dúvidas](https://tableless.com.br/tudo-que-voce-queria-saber-sobre-git-e-github-mas-tinha-vergonha-de-perguntar/)
