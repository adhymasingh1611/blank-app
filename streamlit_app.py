import streamlit as st
import random
from collections import deque
from enum import Enum
import time

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def initialize_game():
    return {
        'snake': deque([(10, 10)]),
        'direction': Direction.RIGHT,
        'next_direction': Direction.RIGHT,
        'food': (random.randint(0, 19), random.randint(0, 19)),
        'score': 0,
        'game_over': False,
        'grid_width': 20,
        'grid_height': 20,
        'game_started': False,
        'moves': 0
    }

def spawn_food(snake, grid_width, grid_height):
    while True:
        x = random.randint(0, grid_width - 1)
        y = random.randint(0, grid_height - 1)
        if (x, y) not in snake:
            return (x, y)

def is_valid_direction(current_dir, new_dir):
    opposites = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT
    }
    return new_dir != opposites[current_dir]

def update_game(game, direction):
    if game['game_over'] or not game['game_started']:
        return game
    
    if is_valid_direction(game['direction'], direction):
        game['direction'] = direction
    
    head_x, head_y = game['snake'][0]
    dx, dy = game['direction'].value
    new_head = (head_x + dx, head_y + dy)
    
    # Check wall collision
    if (new_head[0] < 0 or new_head[0] >= game['grid_width'] or
        new_head[1] < 0 or new_head[1] >= game['grid_height']):
        game['game_over'] = True
        return game
    
    # Check self collision
    if new_head in game['snake']:
        game['game_over'] = True
        return game
    
    game['snake'].appendleft(new_head)
    game['moves'] += 1
    
    # Check food collision
    if new_head == game['food']:
        game['score'] += 10
        game['food'] = spawn_food(game['snake'], game['grid_width'], game['grid_height'])
    else:
        game['snake'].pop()
    
    return game

def draw_grid(game):
    grid = [['⬜' for _ in range(game['grid_width'])] for _ in range(game['grid_height'])]
    
    # Draw snake body
    for i, segment in enumerate(game['snake']):
        if i == 0:
            grid[segment[1]][segment[0]] = '🟩'  # Head
        else:
            grid[segment[1]][segment[0]] = '🟢'  # Body
    
    # Draw food
    grid[game['food'][1]][game['food'][0]] = '🔴'
    
    return '\n'.join([''.join(row) for row in grid])

# Initialize session state
if 'game' not in st.session_state:
    st.session_state.game = initialize_game()

st.set_page_config(page_title="Snake Game", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
    <style>
    .game-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .metrics-row {
        display: flex;
        justify-content: space-around;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐍 Snake Game Streamlit Edition")

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Score", st.session_state.game['score'])
with col2:
    st.metric("Length", len(st.session_state.game['snake']))
with col3:
    st.metric("Moves", st.session_state.game['moves'])

# Display grid
st.write("### Game Board")
st.code(draw_grid(st.session_state.game), language="")

# Game status
if not st.session_state.game['game_started']:
    st.info("📌 Click START GAME to begin!")
elif st.session_state.game['game_over']:
    st.error("💥 GAME OVER!")
else:
    st.success("🎮 Game Running...")

# Controls Section
st.write("### Controls")

# Direction buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("⬆️ UP", key="up", use_container_width=True):
        st.session_state.game['game_started'] = True
        st.session_state.game = update_game(st.session_state.game, Direction.UP)
        st.rerun()

with col2:
    if st.button("⬅️ LEFT", key="left", use_container_width=True):
        st.session_state.game['game_started'] = True
        st.session_state.game = update_game(st.session_state.game, Direction.LEFT)
        st.rerun()

with col3:
    if st.button("⬇️ DOWN", key="down", use_container_width=True):
        st.session_state.game['game_started'] = True
        st.session_state.game = update_game(st.session_state.game, Direction.DOWN)
        st.rerun()

with col4:
    if st.button("➡️ RIGHT", key="right", use_container_width=True):
        st.session_state.game['game_started'] = True
        st.session_state.game = update_game(st.session_state.game, Direction.RIGHT)
        st.rerun()

# Game action buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start Game", use_container_width=True):
        st.session_state.game['game_started'] = True
        st.rerun()

with col2:
    if st.button("🔄 Restart Game", use_container_width=True):
        st.session_state.game = initialize_game()
        st.rerun()

# Game Over section
if st.session_state.game['game_over']:
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Final Score", st.session_state.game['score'])
    with col2:
        st.metric("Final Length", len(st.session_state.game['snake']))
    with col3:
        st.metric("Total Moves", st.session_state.game['moves'])
    
    st.warning("Game ended! Click 'Restart Game' to play again.")

# Instructions
with st.expander("📖 How to Play"):
    st.write("""
    **Objective:** Eat the red food (🔴) to grow and earn points
    
    **Rules:**
    - Move the snake (🟢) using the direction buttons
    - Eat food to increase your score by 10 points
    - Avoid hitting the walls (borders)
    - Avoid hitting yourself
    
    **Symbols:**
    - 🟩 = Snake Head
    - 🟢 = Snake Body
    - 🔴 = Food
    - ⬜ = Empty Space
    
    **Scoring:**
    - Each food eaten: +10 points
    - Game over if snake hits wall or itself
    """)

st.divider()
st.caption("Made with ❤️ using Streamlit")
