import streamlit as st
import random
import time
from streamlit.components.v1 import html

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Snake Pro: Ultra Edition", 
    page_icon="🐍", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CONSTANTS ---
CELLS = 20 
BASE_SPEED = 0.12

# --- INITIALIZE STATE ---
if 'snake' not in st.session_state:
    st.session_state.snake = [(10, 10), (10, 11), (10, 12)]
    st.session_state.direction = (0, -1)
    st.session_state.food = (5, 5)
    st.session_state.bonus_food = None
    st.session_state.bonus_timer = 0
    st.session_state.food_count = 0
    st.session_state.score = 0
    st.session_state.high_score = 0
    st.session_state.game_over = False
    st.session_state.game_started = False
    st.session_state.game_mode = "Classic 🟦"

# Professional "Plus" Obstacle
OBSTACLES = {
    (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14),
    (6, 10), (7, 10), (8, 10), (9, 10), (11, 10), (12, 10), (13, 10), (14, 10)
}

def spawn_food(exclude_cells):
    all_cells = [(c, r) for r in range(CELLS) for c in range(CELLS)]
    possible_cells = [cell for cell in all_cells if cell not in exclude_cells]
    return random.choice(possible_cells) if possible_cells else (0, 0)

def restart_game():
    if "Obstacles" in st.session_state.game_mode:
        st.session_state.snake = [(3, 3), (3, 4), (3, 5)] 
    else:
        st.session_state.snake = [(10, 10), (10, 11), (10, 12)] 
    
    st.session_state.direction = (0, -1)
    invalid = set(st.session_state.snake)
    if "Obstacles" in st.session_state.game_mode: invalid.update(OBSTACLES)
    
    st.session_state.food = spawn_food(invalid)
    st.session_state.bonus_food = None
    st.session_state.bonus_timer = 0
    st.session_state.food_count = 0
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.game_started = True

# --- STATIC STYLES (Moved outside loop to prevent flashing) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    .stApp {{
        background: radial-gradient(circle at center, #111 0%, #000 100%);
        font-family: 'Rajdhani', sans-serif;
        color: white;
    }}

    .glass-panel {{
        background: rgba(20, 20, 20, 0.7);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
    }}

    .score-value {{ 
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem; 
        color: #00ffcc; 
    }}

    .grid-container {{
        display: grid;
        grid-template-columns: repeat({CELLS}, 32px); 
        grid-template-rows: repeat({CELLS}, 32px);
        gap: 0; 
        background: #050505;
        padding: 5px;
        border: 3px solid #222;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.15);
        width: fit-content;
        margin: 0 auto;
        overflow: hidden;
    }}

    @media (max-width: 768px) {{
        .grid-container {{
            grid-template-columns: repeat({CELLS}, 18px);
            grid-template-rows: repeat({CELLS}, 18px);
        }}
        .cell {{ width: 18px !important; height: 18px !important; font-size: 14px !important; }}
    }}

    .cell {{
        width: 32px; height: 32px;
        display: flex; align-items: center; justify-content: center;
        position: relative; background: rgba(255, 255, 255, 0.01);
        border: 0.1px solid rgba(255, 255, 255, 0.02);
        box-sizing: border-box;
    }}

    .snake-segment {{ width: 100%; height: 100%; position: absolute; z-index: 50; box-sizing: border-box; }}
    .snake-body {{ background: linear-gradient(135deg, #00ff88 0%, #008855 100%); border: 1px solid rgba(0,0,0,0.1); }}
    .snake-head {{ background: linear-gradient(135deg, #00ffcc, #0088ff); z-index: 100; }}
    .snake-tail {{ background: #004433; border-radius: 4px; }}
    .eye {{ position: absolute; background: black; width: 15%; height: 15%; border-radius: 50%; z-index: 101; }}

    .food {{ font-size: 24px; filter: drop-shadow(0 0 5px #ff4757); }}
    .bonus-food {{ font-size: 28px; filter: drop-shadow(0 0 10px #ffdf00); animation: pulse 0.6s infinite alternate; }}
    .obstacle {{ background: #333; border: 0.5px solid #ff4b4b; box-sizing: border-box; }}

    @keyframes pulse {{ from {{ transform: scale(0.9); }} to {{ transform: scale(1.1); }} }}

    .stButton > button {{
        background: rgba(0, 255, 204, 0.1) !important;
        color: #00ffcc !important;
        border: 1px solid rgba(0, 255, 204, 0.4) !important;
        font-family: 'Orbitron', sans-serif !important;
        height: 55px !important;
    }}
    
    /* Hide Streamlit elements that cause flickering */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
</style>
""", unsafe_allow_html=True)

# --- KEYBOARD LISTENER ---
html("""
<script>
    const doc = window.parent.document;
    doc.addEventListener("keydown", function(e) {
        const key = e.key.replace("Arrow", "").toUpperCase();
        const buttons = Array.from(doc.querySelectorAll('button'));
        const target = buttons.find(el => el.innerText.trim() === key);
        if (target) target.click();
    });
</script>
""", height=0, width=0)

# --- RENDERING ENGINE ---
def render_game():
    snake = st.session_state.snake
    dir_x, dir_y = st.session_state.direction
    grid_html = "<div class='grid-container'>"
    snake_lookup = {pos: i for i, pos in enumerate(snake)}
    
    for r in range(CELLS):
        for c in range(CELLS):
            pos = (c, r)
            cell_cls = "cell"
            content = ""
            style = ""
            
            if pos in snake_lookup:
                idx = snake_lookup[pos]
                if idx == 0: # HEAD
                    rad = "10px 10px 2px 2px" if dir_y == -1 else "2px 2px 10px 10px" if dir_y == 1 else "10px 2px 2px 10px" if dir_x == -1 else "2px 10px 10px 2px"
                    eye_style = "top: 20%; left: 20%;" if dir_y != 0 else "top: 20%; left: 20%;"
                    content = f"<div class='snake-segment snake-head' style='border-radius: {rad};'></div>"
                    content += f"<div class='eye' style='{eye_style}'></div>"
                    content += f"<div class='eye' style='{'top: 20%; right: 20%;' if dir_y != 0 else 'bottom: 20%; left: 20%;'}'></div>"
                elif idx == len(snake) - 1: # TAIL
                    content = "<div class='snake-segment snake-tail'></div>"
                else: # BODY
                    content = "<div class='snake-segment snake-body'></div>"
            elif pos == st.session_state.food: content = "<span class='food'>🍎</span>"
            elif pos == st.session_state.bonus_food: content = "<span class='bonus-food'>🌟</span>"
            elif "Obstacles" in st.session_state.game_mode and pos in OBSTACLES: cell_cls += " obstacle"; content = "🧱"
            
            grid_html += f"<div class='{cell_cls}' style='{style}'>{content}</div>"
    return grid_html + "</div>"

# --- MAIN LAYOUT ---
l_col, r_col = st.columns([1, 2.5])

with l_col:
    st.markdown("<h1 style='color:#00ffcc; text-align:center; font-family:Orbitron; font-size:1.8rem; letter-spacing:2px; text-shadow:0 0 20px #00ffcc;'>SNAKE PRO</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        modes = ["Classic 🟦", "Portal 🌀", "Obstacles 🧱", "Flash ⚡"]
        new_mode = st.selectbox("MISSION TYPE", modes, index=modes.index(st.session_state.game_mode))
        if new_mode != st.session_state.game_mode:
            st.session_state.game_mode = new_mode
            restart_game()
            st.rerun()
        
        st.markdown(f"""
        <div style='text-align:center;'>
            <div style='color:#777; font-size:0.8rem; letter-spacing:1px;'>REWARD</div>
            <div class='score-value'>{st.session_state.score}</div>
            <div style='color:#777; font-size:0.8rem; letter-spacing:1px;'>RECORD</div>
            <div class='score-value' style='color:#ff007f;'>{st.session_state.high_score}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c2: 
            if st.button("UP", use_container_width=True) and st.session_state.direction != (0, 1):
                st.session_state.direction = (0, -1); st.session_state.game_started = True
        c4, c5, c6 = st.columns(3)
        with c4: 
            if st.button("LEFT", use_container_width=True) and st.session_state.direction != (1, 0):
                st.session_state.direction = (-1, 0); st.session_state.game_started = True
        with c5: 
            if st.button("RESTART", use_container_width=True): restart_game(); st.rerun()
        with c6: 
            if st.button("RIGHT", use_container_width=True) and st.session_state.direction != (-1, 0):
                st.session_state.direction = (1, 0); st.session_state.game_started = True
        c7, c8, c9 = st.columns(3)
        with c8: 
            if st.button("DOWN", use_container_width=True) and st.session_state.direction != (0, -1):
                st.session_state.direction = (0, 1); st.session_state.game_started = True
        st.markdown("</div>", unsafe_allow_html=True)

with r_col:
    game_placeholder = st.empty()

# --- GAME ENGINE (ANTI-FLICKER LOOP) ---
if st.session_state.game_started and not st.session_state.game_over:
    # Use a while loop instead of st.rerun() to eliminate flashing
    while st.session_state.game_started and not st.session_state.game_over:
        if st.session_state.bonus_food:
            st.session_state.bonus_timer -= 1
            if st.session_state.bonus_timer <= 0: st.session_state.bonus_food = None

        current_speed = max(0.04, BASE_SPEED - (st.session_state.score // 30) * 0.01)
        dx, dy = st.session_state.direction
        new_head = (st.session_state.snake[0][0] + dx, st.session_state.snake[0][1] + dy)

        if any(m in st.session_state.game_mode for m in ["Portal", "Obstacles"]):
            new_head = (new_head[0] % CELLS, new_head[1] % CELLS)

        wall_hit = (not any(m in st.session_state.game_mode for m in ["Portal", "Obstacles"]) and 
                   (new_head[0] < 0 or new_head[0] >= CELLS or new_head[1] < 0 or new_head[1] >= CELLS))
        obs_hit = ("Obstacles" in st.session_state.game_mode and new_head in OBSTACLES)
        
        if wall_hit or obs_hit or new_head in st.session_state.snake:
            st.session_state.game_over = True
            st.session_state.high_score = max(st.session_state.score, st.session_state.high_score)
            st.rerun() # Exit loop to show Game Over screen
        else:
            st.session_state.snake.insert(0, new_head)
            if new_head == st.session_state.food:
                st.session_state.score += 10
                st.session_state.food_count += 1
                invalid = set(st.session_state.snake) | OBSTACLES
                if st.session_state.food_count % 5 == 0:
                    st.session_state.bonus_food = spawn_food(invalid)
                    st.session_state.bonus_timer = 60
                st.session_state.food = spawn_food(invalid | ({st.session_state.bonus_food} if st.session_state.bonus_food else set()))
            elif st.session_state.bonus_food and new_head == st.session_state.bonus_food:
                st.session_state.score += 50
                st.session_state.bonus_food = None
            else:
                st.session_state.snake.pop()

        # Update only the placeholder - NO FULL PAGE REFRESH
        game_placeholder.markdown(render_game(), unsafe_allow_html=True)
        time.sleep(current_speed)

elif st.session_state.game_over:
    game_placeholder.markdown(render_game(), unsafe_allow_html=True)
    st.error(f"NEURAL LINK SEVERED! REWARD: {st.session_state.score}")
    if st.button("RE-INITIALIZE"): restart_game(); st.rerun()
else:
    game_placeholder.markdown(render_game(), unsafe_allow_html=True)
    st.info("INITIATE NEURAL LINK VIA ARROW KEYS")

st.caption(f"Reality Engine v2.0 | Stable Immersive Resolution | Mode: {st.session_state.game_mode}")
