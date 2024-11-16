# Análise e Modelagem de Influência no Instagram - Regressão Linear

## Descrição do Projeto

Este projeto visa desenvolver um modelo preditivo para estimar a taxa de engajamento dos principais influenciadores do Instagram, utilizando algoritmos de **Regressão Linear** e outras técnicas de machine learning, como **Gradiente Descendente**, **Ridge** e **Lasso**. O foco está na análise exploratória dos dados, no desenvolvimento do modelo preditivo e na avaliação do desempenho utilizando métricas como **MSE**, **RMSE**, **R²** e **MAE**.

## Objetivo

O objetivo é prever a variável **"influence_score"** (pontuação de influência) com base em variáveis como número de seguidores, número médio de curtidas, e outros atributos relacionados ao comportamento dos influenciadores no Instagram. Para isso, aplicamos diversos métodos de regressão e otimização, incluindo a **normalização** e a **seleção de variáveis** mais relevantes.

## Base de Dados

O conjunto de dados utilizado neste projeto contém informações sobre influenciadores do Instagram, como o número de seguidores, curtidas médias, postagens, e outros dados relacionados ao seu engajamento na plataforma. A base de dados está disponível no arquivo `top_insta_influencers_data.csv`.

### Descrição das Colunas

- `followers`: Número de seguidores do influenciador.
- `avg_likes`: Número médio de curtidas por postagem.
- `posts`: Número total de postagens feitas pelo influenciador.
- `total_likes`: Número total de curtidas recebidas pelo influenciador.
- `country`: País de origem do influenciador.
- `influence_score`: A variável alvo, que representa a taxa de engajamento do influenciador (pontuação de influência).

## Instruções para Replicar o Projeto

Para replicar este projeto, siga os passos abaixo:

### Requisitos

- **Python 3.x**
- Bibliotecas: `pandas`, `numpy`, `seaborn`, `matplotlib`, `scikit-learn`

Você pode instalar as dependências utilizando o `pip`:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn

# Análise de Modelos de Regressão

Este script realiza uma análise comparativa entre diferentes modelos de regressão, incluindo Regressão Linear, Ridge, Lasso e Gradiente Descendente (SGD). O processo envolve carregamento, pré-processamento dos dados, implementação dos modelos, avaliação de desempenho e validação cruzada.

## Etapas do Script

O script realiza as seguintes etapas:

1. **Carregamento e Pré-processamento dos Dados**  
   Carrega os dados, trata valores ausentes e prepara os dados para análise.

2. **Limpeza de Dados e Conversão de Variáveis Categóricas**  
   Converte variáveis categóricas para variáveis numéricas, removendo inconsistências nos dados.

3. **Análise Exploratória e Visualização da Correlação entre Variáveis**  
   Gera gráficos e explora as correlações entre as variáveis do conjunto de dados.

4. **Implementação dos Modelos de Regressão**  
   Modelos implementados:
   - **Regressão Linear** (Mínimos Quadrados)
   - **Regressão Ridge** (Regularização L2)
   - **Regressão Lasso** (Regularização L1)
   - **Gradiente Descendente (SGD)**

5. **Avaliação de Desempenho**  
   Avaliação dos modelos com as seguintes métricas:
   - **MSE** (Erro Quadrático Médio)
   - **RMSE** (Raiz do Erro Quadrático Médio)
   - **R²** (Coeficiente de Determinação)
   - **MAE** (Erro Absoluto Médio)

6. **Validação Cruzada (k-fold)**  
   Validação cruzada foi aplicada para testar a robustez dos modelos e comparar o desempenho entre eles.

## Visualize os Resultados

O código gera gráficos e visualizações para comparar o desempenho dos modelos e exibir as previsões contra os valores reais.

## Resultados

O desempenho dos modelos foi avaliado com base nas seguintes métricas:

### Regressão Linear (Mínimos Quadrados)
- **Mean Squared Error (MSE)**: [valor]
- **Root Mean Squared Error (RMSE)**: [valor]
- **R²**: [valor]
- **Mean Absolute Error (MAE)**: [valor]

### Regressão Ridge (Regularização L2)
- **Mean Squared Error (MSE)**: [valor]
- **Root Mean Squared Error (RMSE)**: [valor]
- **R²**: [valor]
- **Mean Absolute Error (MAE)**: [valor]

### Regressão Lasso (Regularização L1)
- **Mean Squared Error (MSE)**: [valor]
- **Root Mean Squared Error (RMSE)**: [valor]
- **R²**: [valor]
- **Mean Absolute Error (MAE)**: [valor]

### Gradiente Descendente (SGD)
- **Mean Squared Error (MSE)**: [valor]
- **Root Mean Squared Error (RMSE)**: [valor]
- **R²**: [valor]
- **Mean Absolute Error (MAE)**: [valor]

Além disso, a validação cruzada foi aplicada para cada modelo, e a comparação dos resultados foi feita utilizando a **Mean Squared Error (MSE)**.

## Conclusões

- O modelo de **Regressão Linear** apresentou bons resultados em termos de precisão, com um R² de [valor], indicando que ele consegue explicar uma boa parte da variação nos dados.
- A utilização de técnicas de **regularização** como **Ridge** e **Lasso** ajudou a evitar overfitting, com resultados comparáveis à regressão linear, mas com melhor desempenho em alguns casos.
- O **Gradiente Descendente (SGD)** mostrou-se eficaz, mas exige um ajuste mais fino dos hiperparâmetros para otimizar o desempenho.

## Referências

- [Documentação do Scikit-learn](https://scikit-learn.org/)
- [Documentação do Pandas](https://pandas.pydata.org/)
- [Documentação do Numpy](https://numpy.org/)

## Autores

- Gustavo Cruz
