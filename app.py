import streamlit as st
import random

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Stone Paper Scissors",
    page_icon="🎮",
    layout="centered"
)


# ==========================================
# CUSTOM DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: white;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #d9e6ff;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Score card */
.score-card {
    background: rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.20);
    box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.25);
    min-height: 150px;
}

.score-title {
    color: white;
    font-size: 22px;
    font-weight: bold;
}

.score-number {
    color: white;
    font-size: 48px;
    font-weight: 800;
    margin: 10px 0;
}

/* Choice title */
.choice-title {
    text-align: center;
    color: white;
    font-size: 25px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Computer choice */
.computer-box {
    text-align: center;
    color: #d9e6ff;
    font-size: 20px;
    margin-top: 20px;
}

/* Result */
.result-box {
    background: rgba(255, 255, 255, 0.12);
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    color: white;
    font-size: 24px;
    font-weight: bold;
    margin-top: 25px;
}

/* Winner */
.winner-box {
    background: rgba(255, 255, 255, 0.18);
    border-radius: 25px;
    padding: 30px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
    margin-top: 25px;
    box-shadow: 0px 10px 35px rgba(0, 0, 0, 0.35);
}

/* Footer */
.footer {
    text-align: center;
    color: #b8c7df;
    margin-top: 35px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "result" not in st.session_state:
    st.session_state.result = "Choose your move! 🎮"

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = "Waiting..."


# ==========================================
# GAME LOGIC
# ==========================================

def play_game(user_choice):

    # Computer randomly chooses
    computer_choice = random.choice(
        ["Stone", "Paper", "Scissors"]
    )

    # Save computer choice
    st.session_state.computer_choice = computer_choice

    # ------------------------------
    # DRAW
    # ------------------------------

    if user_choice == computer_choice:

        st.session_state.result = "🤝 DRAW! TRY AGAIN!"

    # ------------------------------
    # USER WINS
    # ------------------------------

    elif (
        (user_choice == "Stone" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Stone")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):

        st.session_state.user_score += 5

        st.session_state.result = "🥳 YOU WON THIS ROUND!"

    # ------------------------------
    # COMPUTER WINS
    # ------------------------------

    else:

        st.session_state.computer_score += 5

        st.session_state.result = "🤖 COMPUTER WON THIS ROUND!"


# ==========================================
# RESET GAME
# ==========================================

def reset_game():

    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = "Choose your move! 🎮"
    st.session_state.computer_choice = "Waiting..."


# ==========================================
# TITLE
# ==========================================

st.markdown(
    '<div class="main-title">🎮 STONE PAPER SCISSORS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">First player to reach 30 points wins the game!</div>',
    unsafe_allow_html=True
)


# ==========================================
# SCORE BOARD
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        f'<div class="score-card">'
        f'<div class="score-title">👤 YOU</div>'
        f'<div class="score-number">{st.session_state.user_score}</div>'
        f'<div class="score-title">POINTS</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f'<div class="score-card">'
        f'<div class="score-title">🤖 COMPUTER</div>'
        f'<div class="score-number">{st.session_state.computer_score}</div>'
        f'<div class="score-title">POINTS</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ==========================================
# GAME OVER CHECK
# ==========================================

game_over = (
    st.session_state.user_score >= 30
    or
    st.session_state.computer_score >= 30
)


# ==========================================
# CHOOSE YOUR MOVE
# ==========================================

st.markdown(
    '<div class="choice-title">🎯 CHOOSE YOUR MOVE</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


# ==========================================
# STONE
# ==========================================

with col1:

    if st.button(
        "🪨 STONE",
        use_container_width=True,
        disabled=game_over,
        key="stone"
    ):

        play_game("Stone")
        st.rerun()


# ==========================================
# PAPER
# ==========================================

with col2:

    if st.button(
        "📄 PAPER",
        use_container_width=True,
        disabled=game_over,
        key="paper"
    ):

        play_game("Paper")
        st.rerun()


# ==========================================
# SCISSORS
# ==========================================

with col3:

    if st.button(
        "✂️ SCISSORS",
        use_container_width=True,
        disabled=game_over,
        key="scissors"
    ):

        play_game("Scissors")
        st.rerun()


# ==========================================
# COMPUTER CHOICE
# ==========================================

st.markdown(
    f'<div class="computer-box">'
    f'🤖 Computer chose: '
    f'<b>{st.session_state.computer_choice}</b>'
    f'</div>',
    unsafe_allow_html=True
)


# ==========================================
# RESULT / WINNER
# ==========================================

if st.session_state.user_score >= 30:

    st.markdown(
        '<div class="winner-box">'
        '🏆🎉 CONGRATULATIONS! 🎉🏆'
        '<br><br>'
        'YOU WON THE GAME!'
        '<br>'
        '🥳'
        '</div>',
        unsafe_allow_html=True
    )

    st.balloons()


elif st.session_state.computer_score >= 30:

    st.markdown(
        '<div class="winner-box">'
        '🤖🏆 COMPUTER WON THE GAME!'
        '<br><br>'
        'Better luck next time! 😄'
        '</div>',
        unsafe_allow_html=True
    )


else:

    st.markdown(
        f'<div class="result-box">'
        f'{st.session_state.result}'
        f'</div>',
        unsafe_allow_html=True
    )


# ==========================================
# RESET BUTTON
# ==========================================

st.write("")

st.button(
    "🔄 RESET GAME",
    use_container_width=True,
    on_click=reset_game
)


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    '<div class="footer">'
    '🎮 Stone Paper Scissors | Built with Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
