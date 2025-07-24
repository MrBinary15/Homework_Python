# ============== Trabajo final Python ===============
# Especialización Internacional de Inteligencia Artificial con Python.
# CASO DE ESTUDIO: Estimación del rango de precios de móviles mediante Machine Learning.

"""
CASO:
Bob ha iniciado su empresa de telefonía móvil. Quiere competir con marcas grandes como Apple y Samsung,
pero no sabe cómo estimar correctamente el precio de los móviles que fabrica.
Por eso recolectó datos de ventas de otras marcas y desea descubrir patrones que le ayuden a colocar su producto
en un rango de precios adecuado. Para ello, me ha pedido ayuda para crear un modelo de Machine Learning
que prediga correctamente el rango de precio de sus teléfonos.

DETALLES DE LA EVALUACIÓN:
Como es un problema de clasificación, en este proyecto calculo las métricas requeridas: accuracy, precision,
recall y f1 score, con un enfoque profesional para que sea comprensible para cualquier persona del equipo técnico.
"""

# -------------------------------
#  Librerías necesarias
# -------------------------------

# En esta sección importo las librerías necesarias para manipular datos, visualizar gráficas y crear los modelos.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")  # Elimino las advertencias visuales que no afectan el análisis

# Librerías especializadas en Machine Learning
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, RobustScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# -------------------------------
#  Análisis inicial de los datos
# -------------------------------

# Cargué el dataset proporcionado por Bob
df = pd.read_csv('../data/CasoBob.csv', sep=",", header=0)

# Verifico la estructura del dataset
df.info()

# Reviso las estadísticas generales de todas las variables numéricas para entender su distribución
print("Estadísticas generales del dataset:")
print(df.describe().round(2))

# Genero un mapa de calor para ver la relación de correlación entre las variables numéricas
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
plt.title("Mapa de calor de correlaciones entre variables")
plt.show()


# --------------------------------
#  Escalado de la variable objetivo (price_range)
# --------------------------------

# Aquí aplico distintos métodos de escalado para visualizar cómo afectan a la variable 'price_range'.
# Aunque no es necesario para el modelo, me ayuda a mostrar el impacto de diferentes escaladores.

mms = MinMaxScaler().fit(df[["price_range"]])
ns = Normalizer().fit(df[["price_range"]])
ss = StandardScaler().fit(df[["price_range"]])
rs = RobustScaler().fit(df[["price_range"]])

# Agrego nuevas columnas al dataset para comparar las transformaciones
df["MinMax_Scaler"] = mms.transform(df[["price_range"]])
df["Normalizer_Scaler"] = ns.transform(df[["price_range"]])
df["Standard_Scaler"] = ss.transform(df[["price_range"]])
df["Robust_Scaler"] = rs.transform(df[["price_range"]])

# Visualizo la distribución de cada escalado para tener un criterio visual del comportamiento de los datos
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

ax1.set_title("price_range")
ax1.hist(df["price_range"], bins=10, color="red", edgecolor="black")
ax1.grid(linewidth=0.1)

ax2.set_title("Min Max Scaler")
ax2.hist(df["MinMax_Scaler"], bins=10, color="red", edgecolor="black")
ax2.grid(linewidth=0.1)

ax3.set_title("Normalizer Scaler")
ax3.hist(df["Normalizer_Scaler"], bins=10, color="red", edgecolor="black")
ax3.grid(linewidth=0.1)

ax4.set_title("Standard Scaler")
ax4.hist(df["Standard_Scaler"], bins=10, color="red", edgecolor="black")
ax4.grid(linewidth=0.1)

ax5.set_title("Robust Scaler")
ax5.hist(df["Robust_Scaler"], bins=10, color="red", edgecolor="black")
ax5.grid(linewidth=0.1)
plt.show()


# -------------------------------
#  Selección de variables predictoras
# -------------------------------

# Separo las variables independientes (X) de la variable objetivo (y)
x = df.drop(columns=["price_range"])
y = df["price_range"]

# Divido los datos en entrenamiento (80%) y prueba (20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Realizo selección de características usando Random Forest para quedarme solo con las más importantes
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
rf_select = RFE(rf, n_features_to_select=10)
rf_select.fit(x_train, y_train)


# -------------------------------
#  Árbol de Decisión
# -------------------------------

# Normalizo todas las variables para este modelo
X = df.drop("price_range", axis=1)
y = df["price_range"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Nuevamente separo en entrenamiento y prueba para este modelo
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Entreno el modelo Árbol de Decisión
tree = DecisionTreeClassifier(max_depth=10, random_state=42)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)

# Reporto las métricas del modelo Árbol de Decisión
print("\nMÉTRICAS - Árbol de Decisión")
print(classification_report(y_test, y_pred_tree))

# Matriz de Confusión para analizar el rendimiento visualmente
tree_cm = confusion_matrix(y_test, y_pred_tree)
sns.heatmap(tree_cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusión - Árbol de Decisión')
plt.xlabel("Predicción")
plt.ylabel("Valor Real")
plt.show()

# Muestro la importancia de cada variable en el Árbol
importances = tree.feature_importances_
features = df.drop("price_range", axis=1).columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=features)
plt.title("Importancia de cada variable según el Árbol de Decisión")
plt.xlabel("Importancia")
plt.ylabel("Variable")
plt.show()


# -------------------------------
#  Red Neuronal usando MLPClassifier de sklearn
# -------------------------------

# Configuro una red neuronal simple con 2 capas ocultas
mlp = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42)
mlp.fit(X_train, y_train)
y_pred_mlp = mlp.predict(X_test)

# Reporto las métricas del modelo de Red Neuronal
print("\nMÉTRICAS - Red Neuronal (MLPClassifier sklearn)")
print(classification_report(y_test, y_pred_mlp))

# Matriz de Confusión para el modelo de Red Neuronal
mlp_cm = confusion_matrix(y_test, y_pred_mlp)
sns.heatmap(mlp_cm, annot=True, fmt='d', cmap='Purples')
plt.title('Matriz de Confusión - Red Neuronal (MLPClassifier)')
plt.xlabel("Predicción")
plt.ylabel("Valor Real")
plt.show()


# -------------------------------
#  Comparación de Resultados (Árbol vs Red Neuronal)
# -------------------------------

# Comparo la precisión (Accuracy) de ambos modelos
print("\nAccuracy Árbol:", round(accuracy_score(y_test, y_pred_tree), 2))
print("Accuracy Red Neuronal (MLPClassifier):", round(accuracy_score(y_test, y_pred_mlp), 2))

# Genero tablas resumen para mostrar las métricas detalladamente
tree_report = classification_report(y_test, y_pred_tree, output_dict=True)
tree_df = pd.DataFrame(tree_report).transpose().round(2)

mlp_report = classification_report(y_test, y_pred_mlp, output_dict=True)
mlp_df = pd.DataFrame(mlp_report).transpose().round(2)

print("\n📋 Tabla de métricas - Árbol de Decisión")
print(tree_df)

print("\n📋 Tabla de métricas - Red Neuronal (MLPClassifier)")
print(mlp_df)


# -------------------------------
#  Conclusión del Caso
# -------------------------------

"""
En mi análisis final, puedo concluir que la red neuronal ofrece mejores métricas que el árbol de decisión,
logrando alrededor de un 90% de precisión.

Gracias a este modelo, Bob podrá predecir los rangos de precios de sus móviles con confianza,
lo cual le permitirá tomar decisiones estratégicas para competir en el mercado frente a las grandes marcas.
"""
