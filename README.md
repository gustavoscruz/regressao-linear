# Projeto de Regressão Linear: Análise da Taxa de Engajamento dos Influenciadores no Instagram

## Objetivo

O objetivo deste projeto é implementar e avaliar o desempenho do algoritmo de **Regressão Linear** em um conjunto de dados real, visando inferir a **taxa de engajamento** dos principais influenciadores no Instagram. O projeto envolve as seguintes etapas:

- Análise exploratória dos dados.
- Implementação de diferentes modelos de Regressão Linear (com e sem regularização).
- Avaliação do desempenho utilizando métricas como R², MSE e MAE.
- Validação cruzada e otimização de hiperparâmetros.
- Documentação técnica do processo.

## Descrição do Projeto

Este projeto utiliza dados de influenciadores do Instagram para prever a **taxa de engajamento** (ou **influence_score**) com base em variáveis como número de seguidores, posts, média de likes e outros fatores relacionados ao perfil de um influenciador. A variável dependente, ou target, é o **influence_score**, que é uma medida da taxa de engajamento de cada influenciador.

> **Nota**: O link para acessar o conjunto de dados está disponível na seção "Instruções para o Desenvolvimento do Projeto".

### Objetivos Específicos:

1. **Análise Exploratória**: Examinar as variáveis do conjunto de dados e identificar relações importantes para a previsão da taxa de engajamento.
2. **Implementação do Modelo de Regressão Linear**: Testar diferentes versões do modelo (com e sem regularização).
3. **Otimização e Ajustes**: Ajustar hiperparâmetros como a taxa de aprendizado, número de épocas, e aplicar técnicas de regularização (Lasso e Ridge).
4. **Avaliação de Desempenho**: Calcular métricas de performance e validar o modelo com dados não vistos (validação cruzada).
5. **Documentação**: Elaborar um relatório técnico detalhando todas as etapas do projeto, incluindo análises, ajustes e resultados.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - Pandas
  - NumPy
  - Seaborn
  - Matplotlib
  - Scikit-learn

## Conjunto de Dados

O conjunto de dados utilizado contém informações sobre influenciadores do Instagram e suas métricas de engajamento, como número de seguidores, média de likes, número de posts, etc. A variável dependente, ou target, é o **influence_score**, que é uma medida da taxa de engajamento de cada influenciador.

> **Nota**: O link para acessar o conjunto de dados está disponível na seção "Instruções para o Desenvolvimento do Projeto".

## Como Rodar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone # Projeto de Regressão Linear: Análise da Taxa de Engajamento dos Influenciadores no Instagram

## Objetivo

O objetivo deste projeto é implementar e avaliar o desempenho do algoritmo de **Regressão Linear** em um conjunto de dados real, visando inferir a **taxa de engajamento** dos principais influenciadores no Instagram. O projeto envolve as seguintes etapas:

- Análise exploratória dos dados.
- Implementação de diferentes modelos de Regressão Linear (com e sem regularização).
- Avaliação do desempenho utilizando métricas como R², MSE e MAE.
- Validação cruzada e otimização de hiperparâmetros.
- Documentação técnica do processo.

## Descrição do Projeto

Este projeto utiliza dados de influenciadores do Instagram para prever a **taxa de engajamento** (ou **influence_score**) com base em variáveis como número de seguidores, posts, média de likes e outros fatores relacionados ao perfil de um influenciador. A variável dependente, ou target, é o **influence_score**, que é uma medida da taxa de engajamento de cada influenciador.

> **Nota**: O link para acessar o conjunto de dados está disponível na seção "Instruções para o Desenvolvimento do Projeto".

### Objetivos Específicos:

1. **Análise Exploratória**: Examinar as variáveis do conjunto de dados e identificar relações importantes para a previsão da taxa de engajamento.
2. **Implementação do Modelo de Regressão Linear**: Testar diferentes versões do modelo (com e sem regularização).
3. **Otimização e Ajustes**: Ajustar hiperparâmetros como a taxa de aprendizado, número de épocas, e aplicar técnicas de regularização (Lasso e Ridge).
4. **Avaliação de Desempenho**: Calcular métricas de performance e validar o modelo com dados não vistos (validação cruzada).
5. **Documentação**: Elaborar um relatório técnico detalhando todas as etapas do projeto, incluindo análises, ajustes e resultados.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - Pandas
  - NumPy
  - Seaborn
  - Matplotlib
  - Scikit-learn

## Conjunto de Dados

O conjunto de dados utilizado contém informações sobre influenciadores do Instagram e suas métricas de engajamento, como número de seguidores, média de likes, número de posts, etc. A variável dependente, ou target, é o **influence_score**, que é uma medida da taxa de engajamento de cada influenciador.

> **Nota**: O link para acessar o conjunto de dados está disponível na seção "Instruções para o Desenvolvimento do Projeto".

## Como Rodar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git](https://github.com/gustavoscruz/regressao-linear
   cd regressao-linear

# Previsão de Taxa de Engajamento com Regressão Linear

Este projeto visa prever a taxa de engajamento de influenciadores no Instagram utilizando diferentes abordagens de Regressão Linear. A análise abrange desde a preparação dos dados até a avaliação e comparação de modelos com regularização (Lasso e Ridge) e otimização via Gradiente Descendente.

## Etapas do Projeto

### 1. Definição e Preparação do Problema
- **Acesso ao Conjunto de Dados**: O conjunto de dados foi acessado e limpo, removendo valores ausentes e convertendo variáveis para formatos numéricos adequados.
- **Análise Exploratória**: Analisamos a correlação entre as variáveis e destacamos as mais relevantes para a previsão da taxa de engajamento.

### 2. Implementação do Algoritmo de Regressão Linear
- Utilizamos o algoritmo de Regressão Linear do **Scikit-learn**, além de variantes com regularização:
  - **Lasso** (L1 Regularization)
  - **Ridge** (L2 Regularization)
- O modelo foi treinado com diferentes combinações de variáveis independentes.

### 3. Otimização e Ajustes
- **Normalização**: Aplicação de técnicas de normalização para melhorar a convergência do modelo.
- **Gradiente Descendente**: Utilização de gradiente descendente para otimizar a função de custo, ajustando a taxa de aprendizado e o número de iterações.
- **Regularização**: Técnicas de regularização (Lasso e Ridge) aplicadas para evitar o overfitting e melhorar a generalização do modelo.

### 4. Análise e Visualização dos Resultados
- **Métricas de Desempenho**: O desempenho do modelo foi avaliado usando as seguintes métricas:
  - **R²** (Coeficiente de Determinação)
  - **MSE** (Erro Quadrático Médio)
  - **MAE** (Erro Absoluto Médio)
- **Visualização**: Comparação entre as previsões e os valores reais, além de uma análise da performance dos diferentes modelos.

### 5. Validação Cruzada
- **Validação Cruzada (k-fold)**: Implementação de validação cruzada para garantir que o modelo generalize bem para dados não vistos.

## Resultados

- A **Regressão Linear tradicional**, o modelo **Ridge** e o modelo **Lasso** foram comparados em termos de desempenho, apresentando as métricas R², MSE e MAE.
- O **modelo de Gradiente Descendente (SGD)** também foi testado e comparado com as demais abordagens para otimização.

## Relatório Técnico

O relatório técnico, com todos os detalhes sobre o processo de análise, implementação, otimização, ajustes de parâmetros e resultados obtidos, está disponível no repositório em formato PDF. Para acessá-lo, basta clicar no link abaixo:

[Relatório Técnico - Implementação e Análise do Algoritmo de Regressão Linear](docs/relatorio.pdf)

## Conclusão

Este projeto proporciona uma análise detalhada sobre o uso da Regressão Linear para prever a taxa de engajamento dos influenciadores no Instagram. Incluindo a implementação de técnicas de regularização e validação cruzada para garantir a eficácia do modelo. A comparação dos diferentes algoritmos mostrou que a regularização pode melhorar a generalização do modelo e reduzir o risco de overfitting.

## Contribuições

Contribuições para o projeto são bem-vindas! Se você tiver sugestões de melhorias ou identificar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Referências

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

## Autores

- **Gustavo Cruz**
- **Vinícius Castro**
