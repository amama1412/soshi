import streamlit as st
import requests

# タイトル
st.title("🌤 天気情報アプリ")

# 都市名の入力
city = st.text_input("都市名を入力してください（例：Tokyo, Osaka, Nagano）")

# APIキーを設定（←あなたのキーをここに入れてください）
API_KEY = "99906c46f61705011e1fdbea5cdcb716"

# ボタンが押されたら実行
if st.button("天気を表示"):
    if city:
        # APIエンドポイント
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=ja&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            st.subheader(f"🌍 {data['name']} の天気")
            st.write(f"**天気**：{data['weather'][0]['description']}")
            st.write(f"**気温**：{data['main']['temp']} ℃")
            st.write(f"**湿度**：{data['main']['humidity']} %")
            st.write(f"**風速**：{data['wind']['speed']} m/s")

            # 天気アイコン表示
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            st.image(icon_url)
        else:
            st.error("❌ エラーが発生しました。都市名やAPIキーを確認してください。")
    else:
        st.warning("都市名を入力してください。")
