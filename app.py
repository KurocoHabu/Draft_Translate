import streamlit as st
from googletrans import Translator


#タイトル
st.title("翻訳ウェブアプリ_ドラフト版")
st.write("streamlitで実装")

translator = Translator()
text = st.text_input('英文を打ち込んでください', 'This is a pen')

result = translator.translate(text, dest="ja")
trans_text = result.text

st.markdown(trans_text)

st.download_button(
        label="翻訳済みテキストファイルをダウンロード",
        data=trans_text,
        file_name='翻訳文.txt',
        # mime='text/csv',
    )
