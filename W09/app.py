import streamlit as st

st.title("🎴我的學習名片")
st.subheader("歡迎來到我的個人學習空間！")

name = st.text_input("請輸入姓名")
st.write("Ex.創作者姓名")
topic = st.text_input("感興趣的資訊主題")
st.write("Python Web App開發")
if st.button("建立我的學習名片"):
    if name.strip() == "" or topic.strip() == "":
        st.warning("請先輸入完整資訊！")
    else:
        st.success("學習名片建立完成！")
        st.write("### 我的學習名片")
        st.write("姓名：", name)
        st.write("興趣主題：", topic)
        st.write("我正在學習 Python，")
        st.write("希望透過程式解決生活中的問題。")
