import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.feature_selection import RFE

# Carregar os dados
data = pd.read_csv('top_insta_influencers_data.csv')

# Limpeza e Preprocessamento de Dados
print("Valores ausentes antes do preenchimento:")
print(data.isnull().sum())

# Preencher valores ausentes apenas nas colunas numéricas
data.select_dtypes(include=[np.number]).columns

# Verificar se ainda há valores ausentes
print("\nValores ausentes após o preenchimento:")
print(data.isnull().sum())

# Converter variáveis categóricas para números (codificação de 'country')
data['country'] = data['country'].astype('category').cat.codes

# Função para converter valores com 'k' e 'm' em números
def convert_to_numeric(value):
    if isinstance(value, str):
        if 'k' in value:
            return float(value.replace('k', '').replace('K', '').replace(',', '').strip()) * 1000
        elif 'm' in value:
            return float(value.replace('m', '').replace('M', '').replace(',', '').strip()) * 1e6
    return value

# Aplicar a conversão para os valores de 'followers' e 'avg_likes' (ou outras colunas relevantes)
data['followers'] = data['followers'].apply(convert_to_numeric)
data['avg_likes'] = data['avg_likes'].apply(convert_to_numeric)
data['posts'] = data['posts'].apply(convert_to_numeric)
data['total_likes'] = data['total_likes'].apply(convert_to_numeric)

# Garantir que todas as variáveis numéricas sejam convertidas corretamente
data = data.apply(pd.to_numeric, errors='ignore')

# Engenharia de Features: Log das variáveis (se necessário)
data['log_followers'] = np.log1p(data['followers'])
data['log_avg_likes'] = np.log1p(data['avg_likes'])

# Analisar correlação entre variáveis para seleção de recursos
corr_data = data.select_dtypes(include=[np.number]) 
corr_matrix = corr_data.corr() 
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Seleção de Features e target
# Removendo a coluna 'influence_score' que é o target, e 'country' que é categórica
X = data.drop(columns=['influence_score', 'country'], errors='ignore')  # Remove 'influence_score' (target) e 'country' (categórica)
y = data['influence_score']  # A variável target

# Verificar se há valores nulos em X
if X.isnull().sum().any():
    print("Existem valores ausentes em X. Preenchendo os valores ausentes...")
    X = X.fillna(X.mean())  # Preencher os valores ausentes com a média das colunas numéricas

# Certificar que X contém apenas variáveis numéricas
X_numeric = X.select_dtypes(include=[np.number])

# Verificar se X_numeric está vazio
if X_numeric.shape[1] == 0:
    print("Erro: Nenhuma coluna numérica encontrada em X. Verifique os dados!")
else:
    # Normalização das variáveis numéricas
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_numeric)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 1. Regressão Linear com Gradiente Descendente (SGD)
sgd = SGDRegressor(max_iter=1000, tol=1e-3, eta0=0.01, random_state=42)  # Gradient Descent
sgd.fit(X_train, y_train)
y_pred_sgd = sgd.predict(X_test)
mse_sgd = mean_squared_error(y_test, y_pred_sgd)
rmse_sgd = np.sqrt(mse_sgd)
r2_sgd = sgd.score(X_test, y_test)
mae_sgd = mean_absolute_error(y_test, y_pred_sgd)

print(f'Gradiente Descendente (SGD):')
print(f'Mean Squared Error: {mse_sgd}')
print(f'Root Mean Squared Error: {rmse_sgd}')
print(f'R²: {r2_sgd}')
print(f'Mean Absolute Error: {mae_sgd}')

# 2. Regressão Linear (mínimos quadrados)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(mse_lr)
r2_lr = lr.score(X_test, y_test)
mae_lr = mean_absolute_error(y_test, y_pred_lr)

print(f'Regressão Linear:')
print(f'Mean Squared Error: {mse_lr}')
print(f'Root Mean Squared Error: {rmse_lr}')
print(f'R²: {r2_lr}')
print(f'Mean Absolute Error: {mae_lr}')

# 3. Regressão Ridge (L2 Regularization)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
rmse_ridge = np.sqrt(mse_ridge)
r2_ridge = ridge.score(X_test, y_test)
mae_ridge = mean_absolute_error(y_test, y_pred_ridge)

print(f'Regressão Ridge:')
print(f'Mean Squared Error: {mse_ridge}')
print(f'Root Mean Squared Error: {rmse_ridge}')
print(f'R²: {r2_ridge}')
print(f'Mean Absolute Error: {mae_ridge}')

# 4. Regressão Lasso (L1 Regularization)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
rmse_lasso = np.sqrt(mse_lasso)
r2_lasso = lasso.score(X_test, y_test)
mae_lasso = mean_absolute_error(y_test, y_pred_lasso)

print(f'Regressão Lasso:')
print(f'Mean Squared Error: {mse_lasso}')
print(f'Root Mean Squared Error: {rmse_lasso}')
print(f'R²: {r2_lasso}')
print(f'Mean Absolute Error: {mae_lasso}')

# 5. Validação Cruzada (k-fold) para todos os modelos
cv_scores_sgd = cross_val_score(sgd, X_scaled, y, cv=5, scoring='neg_mean_squared_error')
cv_scores_lr = cross_val_score(lr, X_scaled, y, cv=5, scoring='neg_mean_squared_error')
cv_scores_ridge = cross_val_score(ridge, X_scaled, y, cv=5, scoring='neg_mean_squared_error')
cv_scores_lasso = cross_val_score(lasso, X_scaled, y, cv=5, scoring='neg_mean_squared_error')

print(f'\nValidação Cruzada (MSE) - SGD: {np.mean(cv_scores_sgd)}')
print(f'Validação Cruzada (MSE) - Regressão Linear: {np.mean(cv_scores_lr)}')
print(f'Validação Cruzada (MSE) - Ridge: {np.mean(cv_scores_ridge)}')
print(f'Validação Cruzada (MSE) - Lasso: {np.mean(cv_scores_lasso)}')

# Visualizar os resultados comparativos
models = ['SGD', 'Linear Regression', 'Ridge', 'Lasso']
mse_scores = [mse_sgd, mse_lr, mse_ridge, mse_lasso]

plt.figure(figsize=(10, 6))
sns.barplot(x=models, y=mse_scores)
plt.ylabel('Mean Squared Error')
plt.title('Comparação de Modelos')
plt.show()

# Visualização de Previsões vs Real para Regressão Linear
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_lr, color='blue', label='Predições', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Linha de Identidade')
plt.xlabel('Valor Real')
plt.ylabel('Valor Predito')
plt.title('Previsões vs Real (Regressão Linear)')
plt.legend()
plt.show()

# Interpretação dos Coeficientes (para o modelo de Regressão Linear)
print("\nCoeficientes da Regressão Linear:")
for feature, coef in zip(X.columns, lr.coef_):
    print(f'{feature}: {coef}')
