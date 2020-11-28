import streamlit as st
import random
import string
import joblib
import os


# ''' Fazer a função gerar a senha ,vai gerar a senha com caracteres aleatorios'''

def gerador_senha(size):
    caracter = string.digits + string.ascii_letters + string.punctuation
    gerar_senha = "".join(random.choice(caracter) for x in range(size))
    return gerar_senha


# Carregando modelo que foi feito o treinamento de machine learn'''

def carregando_modelo(modelo):
    carregando = joblib.load(open(os.path.join(modelo), "rb"))
    return carregando


senha_vectorizer = open("pswd_cv.pkl", "rb")
senha_cv = joblib.load(senha_vectorizer)


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


senh_labels = {"Fraca": 0, "Medio": 1, "Forte": 2}  # Informo para o modelo setando pra ele se for zero um ou dois


# ''' Função principal que roda o codigo '''

def main():
    global prediction
    st.title("  Gerador de senhas ")  # titulo
    st.subheader("")  # subtitulo

    activities = ["Classificar a senha", "Gerar senha", "Sobre"]  # Menu com as opções de escolha
    escolha = st.sidebar.selectbox("Selecione ", activities)

    if escolha == "Classificar a senha":
        st.subheader("Classificação")
        sua = st.text_input("Entre com a senha para classificação: ", type="password")
        #       '''Temos que dizer qual modelo de Machine learning usamos, escolhi pela Recurrente neural networks '''
        modelo = ["Naive"]
        if st.button("Classifica"):
            vect_senha = senha_cv.transform([sua]).toarray()
            if modelo == 'Naive':
                predictor = carregando_modelo("logit_pswd_model.pkl")
                prediction = predictor.predict(vect_senha)

            resultado_final = get_key(prediction, senh_labels)
            st.write(resultado_final)



    #     SE  a escolha no menu for gerar senha e executa este comando'''

    elif escolha == "Gerar senha":
        st.subheader("Senha randomica")
        number = st.number_input("Entre com o tamanho da senha:", 8, 25)
        st.write(number)
        if st.button("Gerar"):
            senha = gerador_senha(number)
            st.write(senha)


if __name__ == '__main__':
    main()
