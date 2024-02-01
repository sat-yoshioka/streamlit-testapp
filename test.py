import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.header('Streamlitのテストページ', divider='rainbow')
page = st.sidebar.selectbox('ページを選択', ['入力項目', 'グラフ', '地図'], index=0)


if page == '入力項目':
    '### テキストボックス'
    textValue = st.text_input('ラベル')
    st.write('入力された値：',textValue)

    st.divider()

    '### チェックボックス'
    if st.checkbox('ラベル'):
        st.write('チェックされました')

    st.divider()

    '### トグル'
    if st.toggle('ラベル'):
       st.write('有効になりました')

    st.divider()

    '### ラジオボタン'
    radioValue = st.radio(
        "選択してください",
        ["ラジオ1", "ラジオ2", "ラジオ3"]
    )

    st.write(radioValue,'が選択されました')

    st.divider()

    '### セレクトボックス'
    selectValue = st.selectbox(
        "選択してください",
        ["セレクト1", "セレクト2", "セレクト3"]
    )

    st.write(selectValue,'が選択されました')


    st.divider()

    '### スライダー'
    sliderValue = st.slider('ラベル', 0, 100, 50)
    st.write('スライダーの値：',sliderValue)

    st.divider()

    '### ボタン'
    if st.button('ラベル'):
        st.write('ボタンが押されました')

    st.divider()

    '### リンク'
    st.link_button("ラベル", "https://www.sat.ne.jp/")

    st.divider()

    '### 日付'
    d = st.date_input("日付を選択", datetime.date.today())
    st.write(d)

elif page == 'グラフ':
    df = pd.DataFrame(np.random.randint(-100,100,(5,5)))
    df.columns = [
        'column1',
        'column2',
        'column3',
        'column4',
        'column5'
    ]
    df.index = [
        '001',
        '002',
        '003',
        '004',
        '005',
    ]

    st.write('下記の表をグラフで表示します。')
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        '### area_chart'
    with col2:
        st.area_chart(df)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        '### bar_chart'
    with col2:
        st.bar_chart(df)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        '### line_chart'
    with col2:
        st.line_chart(df)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        '### scatter_chart'
    with col2:
        st.scatter_chart(df)


else:
    st.write('Streamlitのテストページ3です。')
    latitude = st.text_input('緯度','33.591106')
    longitude = st.text_input('経度','130.380869')
    df = pd.DataFrame(
        [[float(latitude), float(longitude)]],
        columns=['lat','lon']
    )
    st.map(df)