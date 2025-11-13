import streamlit as st
from ytmusicapi import YTMusic

ytmusic = YTMusic()

st.title("🎧 気分に合った YouTube Music アプリ")

# 気分リスト
moods = {
    "元気が出る": "upbeat J-pop",
    "落ち着きたい": "relax piano",
    "勉強中": "study lo-fi beats",
    "悲しい気分": "sad songs",
    "テンション上げたい": "party EDM",
    "眠れない夜": "sleep music",
    "雨の日": "rainy day songs"
}

mood = st.selectbox("今の気分・状況を選んでください：", list(moods.keys()))

if st.button("おすすめ曲を表示"):
    query = moods[mood]
    st.write(f"🎵 {mood} におすすめの曲（検索ワード：*{query}*）")

    results = ytmusic.search(query, filter="songs")

    if results:
        for song in results[:5]:
            title = song["title"]
            artist = ", ".join([a["name"] for a in song["artists"]])
            video_id = song["videoId"]
            thumbnail = song["thumbnails"][-1]["url"]

            st.image(thumbnail, width=200)
            st.write(f"**{title}** - {artist}")
            st.markdown(f"[▶ 再生する](https://music.youtube.com/watch?v={video_id})")
    else:
        st.error("結果が見つかりませんでした。")
