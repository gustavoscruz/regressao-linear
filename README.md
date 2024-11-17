Projeto de Regressão Linear: Análise da Taxa de Engajamento dos Influenciadores no Instagram
Objetivo

O objetivo deste projeto é implementar e avaliar o desempenho do algoritmo de Regressão Linear em um conjunto de dados real, visando inferir a taxa de engajamento dos principais influenciadores no Instagram. O projeto envolve as seguintes etapas:

    Análise exploratória dos dados.
    Implementação de diferentes modelos de Regressão Linear (com e sem regularização).
    Avaliação do desempenho utilizando métricas como R², MSE e MAE.
    Validação cruzada e otimização de hiperparâmetros.
    Documentação técnica do processo.

Descrição do Projeto

Este projeto utiliza dados de influenciadores do Instagram para prever a taxa de engajamento (ou influence_score) com base em variáveis como número de seguidores, posts, média de likes e outros fatores relacionados ao perfil de um influenciador. O modelo de Regressão Linear é implementado e avaliado utilizando diversas técnicas de pré-processamento, regularização e validação.
Objetivos Específicos:

    Análise Exploratória: Examinar as variáveis do conjunto de dados e identificar relações importantes para a previsão da taxa de engajamento.
    Implementação do Modelo de Regressão Linear: Testar diferentes versões do modelo (com e sem regularização).
    Otimização e Ajustes: Ajustar hiperparâmetros como a taxa de aprendizado, número de épocas, e aplicar técnicas de regularização (Lasso e Ridge).
    Avaliação de Desempenho: Calcular métricas de performance e validar o modelo com dados não vistos (validação cruzada).
    Documentação: Elaborar um relatório técnico detalhando todas as etapas do projeto, incluindo análises, ajustes e resultados.

Tecnologias Utilizadas

    Linguagem: Python
    Bibliotecas:
        Pandas
        NumPy
        Seaborn
        Matplotlib
        Scikit-learn

Conjunto de Dados

O conjunto de dados utilizado contém informações sobre influenciadores do Instagram e suas métricas de engajamento, como número de seguidores, média de likes, número de posts, etc. A variável dependente, ou target, é o influence_score, que é uma medida da taxa de engajamento de cada influenciador.

Como Rodar o Projeto

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Instale as dependências:

Certifique-se de ter as bibliotecas necessárias instaladas em seu ambiente Python. Se necessário, crie um ambiente virtual e instale as dependências com o seguinte comando:
pip install -r requirements.txt

Preparação dos Dados:

O arquivo de dados top_insta_influencers_data.csv deve estar na mesma pasta do script ou você deve ajustar o caminho no código para garantir o acesso correto ao arquivo.

Executando o Script:

Após configurar o ambiente e os dados, execute o script Python para rodar o modelo de Regressão Linear e obter os resultados:
python regressao_linear.py


Etapas do Projeto
1. Definição e Preparação do Problema

    Acesso ao Conjunto de Dados: O conjunto de dados foi acessado e limpo, removendo valores ausentes e convertendo variáveis para formatos numéricos adequados.
    Análise Exploratória: Analisamos a correlação entre as variáveis e destacamos as mais relevantes para a previsão da taxa de engajamento.

2. Implementação do Algoritmo de Regressão Linear

    Utilizamos o algoritmo de Regressão Linear do Scikit-learn, além de variantes com regularização (Lasso e Ridge).
    O modelo foi treinado com diferentes combinações de variáveis independentes.

3. Otimização e Ajustes

    Aplicamos técnicas de normalização para melhorar a convergência do modelo.
    Utilizamos o gradiente descendente para otimizar a função de custo, ajustando a taxa de aprendizado e o número de iterações.
    Técnicas de regularização (Lasso e Ridge) foram aplicadas para evitar o overfitting e melhorar a generalização do modelo.

4. Análise e Visualização dos Resultados

    Avaliamos o desempenho do modelo com as métricas: R², MSE (erro quadrático médio) e MAE (erro absoluto médio).
    Visualizamos as previsões versus os valores reais, comparando a performance dos diferentes modelos.

5. Validação Cruzada

    Implementamos validação cruzada (k-fold) para garantir que o modelo generalize bem para dados não vistos.

Resultados

    A Regressão Linear tradicional, o modelo Ridge e o modelo Lasso foram comparados em termos de desempenho, e as métricas foram apresentadas.
    O modelo de Gradiente Descendente (SGD) também foi testado e comparado com as demais abordagens.

Relatório Técnico

O relatório técnico, com todos os detalhes sobre o processo de análise, implementação, otimização, ajustes de parâmetros e resultados obtidos, está disponível no repositório em formato PDF. Para acessá-lo, basta clicar no link abaixo:

Relatório Técnico - Implementação e Análise do Algoritmo de Regressão Linear
Conclusão

Este projeto proporciona uma análise detalhada sobre o uso da Regressão Linear para prever a taxa de engajamento dos influenciadores no Instagram, incluindo a implementação de técnicas de regularização e validação cruzada para garantir a eficácia do modelo. A comparação dos diferentes algoritmos mostrou que a regularização pode melhorar a generalização do modelo.
Contribuições

Contribuições para o projeto são bem-vindas! Se você tiver sugestões de melhorias ou identificar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.
Referências

    Scikit-learn Documentation
    Pandas Documentation
    Matplotlib Documentation
    Seaborn Documentation
