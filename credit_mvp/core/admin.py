from django.contrib import admin
from .models import Cliente
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import os
from django.conf import settings

model_path = os.path.join(settings.ML_MODELS_PATH, 'modelo_top7.keras')
preprocessor_path = os.path.join(settings.ML_MODELS_PATH, 'preprocessor.gz')
features_path = os.path.join(settings.ML_MODELS_PATH, 'top_features_idx.npy')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'score_risco', 'aprovado_previsto')
    actions = ['analisar_risco']

    def analisar_risco(self, request, queryset):
        # Carrega modelo, preprocessor e lista de features
        model = tf.keras.models.load_model(model_path)
        preprocessor = joblib.load(preprocessor_path)
        top_features_idx = np.load(features_path)


        for cliente in queryset:
            # Monta DataFrame com os dados do cliente
            df = pd.DataFrame([{
                'idade': cliente.idade,
                'salario_mensal': cliente.salario_mensal,
                'score_credito': cliente.score_credito,
                'tempo_emprego_anos': cliente.tempo_emprego_anos,
                'estado_civil': cliente.estado_civil,
                'possui_imovel': cliente.possui_imovel,
                'possui_veiculo': cliente.possui_veiculo,
                'qtd_cartoes_credito': cliente.qtd_cartoes_credito,
                'historico_inadimplencia': cliente.historico_inadimplencia,
                'valor_credito_solicitado': cliente.valor_credito_solicitado,
                'dividas_banco_A': cliente.dividas_banco_A,
                'dividas_banco_B': cliente.dividas_banco_B,
                'dividas_banco_C': cliente.dividas_banco_C,
                'dividas_totais': cliente.dividas_totais
            }])

            # Reorganiza colunas de acordo com as features salvas
            

            # Pré-processamento
            X_processed = preprocessor.transform(df)
            X_top7 = X_processed[:, top_features_idx]

            # Predição
            prob_aprovado = model.predict(X_top7)[0][0]
            score = (1 - prob_aprovado) * 1000
            aprovado = 1 if prob_aprovado > 0.5 else 0

            # Atualiza cliente
            cliente.score_risco = score
            cliente.aprovado_previsto = aprovado
            cliente.save()

        self.message_user(request, f"Análise realizada para {queryset.count()} cliente(s).")
    analisar_risco.short_description = "Analisar risco de crédito"