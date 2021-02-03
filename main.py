
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"Don!!!"

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字表示")
if button:
    right_column.write("ここは右カラム")

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせ内容を書く")



#text = st.text_input("あなたの趣味を教えて下さい。")
#condition = st.slider("あなたの今の調子は", 0,100,50)

#"あなたの趣味は、", text
#"コンディション", condition

# 実行する場合→　streamlit run main.py



#if st.checkbox("Show Image"):
#    img = Image.open("image.png")
#    st.image(img, caption="test", use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=["lat","lon"]
# )
#df
# st.table(df.style.highlight_max(axis=0))

#st.map(df)

