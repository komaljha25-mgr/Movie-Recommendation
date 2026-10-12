import streamlit as st
import joblib
import requests

model=joblib.load('model.pkl')
vectors=joblib.load('vectors.pkl')
df=joblib.load('dataframe.pkl')

st.set_page_config(layout='wide')

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Custom background and styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f0c29,
        #302b63,
        #24243e
    );
    color: white;
}

.banner {
    background:
        linear-gradient(
            rgba(0, 0, 0, 0.45),
            rgba(0, 0, 0, 0.85)
        ),
        url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
    background-size: cover;
    background-position: center;
    height: 300px;
    border-radius: 18px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.5);
}

.banner h1 {
    color: white;
    font-size: 42px;
    font-weight: 800;
    text-shadow: 2px 2px 10px black;
}

.banner p {
    color: #eeeeee;
    font-size: 18px;
}

.stButton > button {
    background-color: #e50914;
    color: white;
    border-radius: 10px;
    border: none;
}

</style>

<div class="banner">
    <h1>🎬 Movie Recommendation System</h1>
    <p>Discover movies you'll love 🍿</p>
</div>
""", unsafe_allow_html=True)

# Your application content
st.subheader("🍿 Discover Your Next Favorite Movie")
st.write("Select a movie below to get personalized recommendations.")

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Main page and sidebar styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #100E1B, #21162E, #15121F
    );
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg, #171326, #291B38, #171326
    );
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #F1ECF7;
}

.sidebar-title {
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: 800;
}

.sidebar-subtitle {
    color: #FF5364;
    text-align: center;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 1px;
}

.sidebar-card {
    background: #302440;
    padding: 15px;
    border-radius: 12px;
    border-left: 4px solid #FF5364;
    margin: 12px 0;
}

.sidebar-tagline {
    color: #FF7583;
    text-align: center;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    # Banner
    st.image(
        "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",
        use_container_width=True
    )

    st.markdown("""
    <div class="sidebar-title">🎬 CineMatch</div>
    <div class="sidebar-subtitle">
        MOVIE RECOMMENDATION SYSTEM
    </div>
    <p style="text-align:center;color:#C9BED9;">
        Discover. Explore. Enjoy.
    </p>
    <hr style="border-color:#493753;">

    <h3>🍿 Welcome, Movie Lover!</h3>

    <p>
        Explore the world of cinema and find movies
        that match your taste with smart recommendations.
    </p>

    <div class="sidebar-card">
        <h4>✨ What You Can Discover</h4>
        <p>🎥 Discover amazing movies</p>
        <p>🔍 Find similar films</p>
        <p>⭐ Explore new favorites</p>
        <p>🤖 Smart recommendations</p>
    </div>

    <p class="sidebar-tagline">
        "Less searching, more watching!"
    </p>

    <p style="text-align:center;color:#B7ADC7;
              font-size:12px;">
        Powered by Machine Learning 🤖
    </p>
    """, unsafe_allow_html=True)

st.sidebar.title("Contact us")
st.sidebar.text("+91-9958966311")

watched_movie=st.selectbox("🎬Select Watched Movie",options=df['name'])

if st.button("Recommend Movies",key="b1"):
    index=df[df.name==watched_movie].index[0]
    distances,indexes=model.kneighbors(vectors[index].toarray())
    for i in indexes[0][1:]:
        st.text(df.loc[i].values[1])
        mid=df.loc[i].values[0]
        resp=requests.get(f"http://www.omdbapi.com/?i={mid}&apikey=1bc645b1")
        data=resp.json()
        st.image(data['Poster'],width=200)
