# Avaliação de Risco para Concessão de Crédito

---

## 1. Objetivo do Projeto

Este projeto tem como objetivo criar um modelo baseado em Redes Neurais para realizar avaliação de risco na concessão de crédito para pessoa física. O modelo prevê a probabilidade de inadimplência do cliente, auxiliando na decisão de aprovação ou rejeição do crédito.

---

## Instalando Dependências

- Instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```
- Observação: É recomendado usar Python 3.10 ou inferior, pois o TensorFlow 2.19.0 pode apresentar problemas em versões superiores.

## 2. Como Executar o Notebook de Treinamento do Modelo

O notebook responsável pela criação e treinamento do modelo utiliza as seguintes bibliotecas:

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import classification_report
```

### Passos principais:

1. Carregar e limpar o dataset.
2. Separar as variáveis independentes (X) e o alvo (y).
3. Pré-processar os dados com técnicas como escalonamento e codificação.
4. Selecionar as 7 principais features para o modelo.
5. Treinar a rede neural com as features selecionadas.
6. Salvar o modelo treinado, o pré-processador e as features selecionadas para uso posterior.

---

## 3. Como Executar o MVP com Django

Este MVP oferece uma interface administrativa para cadastrar clientes e realizar a análise de risco utilizando o modelo treinado.

### Configuração

- A principio, caso você tenha clonado esse repositório você não precisa alterar nada. Caso, tenha algum problema certifique que os caminhos estão corretos, com as instruções abaixo.

- Defina a variável `ML_MODELS_PATH` no arquivo `settings.py` para apontar para a pasta onde estão os arquivos do modelo:

  - `modelo_top7.keras`
  - `preprocessor.gz`
  - `top_features_idx.npy`

- Criar um superuser no Django, para acessar o painel Admin:
```bash
python manage.py createsuperuser
```
- Por fim, executar o servidor:
```bash
python manage.py runserver
```

### Principais dependências usadas

- Django==5.2.1
- TensorFlow==2.19.0
- scikit-learn==1.6.1
- pandas==2.2.3
- numpy==2.1.3
- joblib==1.5.0
- h5py==3.13.0

*(Para a lista completa, veja o arquivo `requirements.txt` ou execute `pip list` na sua venv.)*

### Executando o servidor

Para iniciar o servidor Django:

```bash
python manage.py runserver
```

Depois, acesse o painel administrativo via `/admin`, selecione os clientes desejados e use a ação **"Analisar risco de crédito"** para realizar a previsão.

---

## Dependências instaladas (resumo do pip list)

```
absl-py==2.2.2
asgiref==3.8.1
Django==5.2.1
joblib==1.5.0
numpy==2.1.3
pandas==2.2.3
scikit-learn==1.6.1
tensorflow==2.19.0
h5py==3.13.0
# e outras conforme o ambiente virtual
```

---

## Contato

Para dúvidas ou sugestões, envie um e-mail para [dossantospereira90@gmail.com](mailto:dossantospereira90@gmail.com)


