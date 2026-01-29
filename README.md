# Head Soccer

## About

Head Soccer is a 2D single-player soccer game where you control a red-headed player competing against a CPU opponent (blue-headed). Players use arrow keys to move left/right and spacebar to jump. The objective is to score goals by heading the ball into the opponent's goal. The game features two modes: Quick Game and Tournament mode with three elimination rounds.

## Architecture

The game follows a state-based architecture with multiple specialized components:

### Core Game Loop (main.py - Game class)
- Main entry point that initializes pygame, manages the game loop, and handles state transitions
- Coordinates all game systems: player, cpu, ball, UI, game manager, mode select, and tournament
- Updates and renders based on current game state

### Game State Management
- **GameState (game_state.py)**: Enum defining all possible game states (MODE_SELECT, PLAYING, SCORING, GAME_OVER, OVERTIME, CHAMPION, etc.)
- **GameManager (game_manager.py)**: Manages match scoring, timer, tie detection, overtime logic, and winner determination
- Handles match reset and score tracking between states

### Player System
- **Player (player.py)**: Base class for all players
  - Handles position, velocity, gravity physics
  - Manages keyboard input for human control
  - Enforces field boundaries (goal areas for each side)
  - Renders body and head with eyes
- **CPU (cpu.py)**: Inherits from Player, adds AI behavior
  - Tracks ball position with reaction delays
  - Makes decisions on when to jump and move toward ball
  - Can move anywhere on its half of the field (right side)

### Ball Physics (ball.py)
- Ball movement with gravity, velocity, and bounce physics
- Collision detection with players (head vs body collisions with different bounces)
- Goal detection (left/right goal areas)
- Crossbar collision (bounces off goal posts)
- Ball rendering with soccer pattern

### UI System (ui.py - UI class)
- Static methods for drawing all game elements
- **draw_field()**: Field with goals, grass lines, center circle
- **draw_score()**: Score display
- **draw_timer()**: Match timer (red when <10s, yellow "Golden Goal" in overtime)
- **draw_game_over()**: Winner announcement
- **draw_champion()**: Tournament victory screen
- **draw_tournament_progress()**: Round progress display

### Mode Selection (mode_select.py)
- Handles menu navigation (left/right arrows to select, enter to confirm)
- Two options: Quick Game and Tournament mode
- Visual selection highlighting

### Tournament System (tournament.py)
- Manages three-round tournament (Quarterfinals, Semi Finals, Finals)
- Tracks wins and losses
- Advances rounds or eliminates player based on match results
- Awards champion status for winning finals

### Constants (constants.py)
- Game configuration: screen dimensions, FPS, colors
- Player/ball physics: speed, gravity, jump force
- Field layout: goal dimensions, ground level
- Key bindings: Left, Right, Space (jump), Enter, Escape

## How to Run

```bash
cd head-soccer
python main.py
```

## How to Use

### Controls
- **Left Arrow**: Move left
- **Right Arrow**: Move right
- **Spacebar**: Jump
- **Enter**: Confirm selection / Continue
- **Escape**: Return to menu

### Game Modes

#### Quick Game
1. Select "Quick Game" from main menu
2. 60-second match against CPU
3. Score more goals to win
4. If tied, go to overtime (Golden Goal)
5. Press Enter to restart after game over

#### Tournament Mode
1. Select "Tournament" from main menu
2. 3-round elimination: Quarterfinals → Semi Finals → Finals
3. Win 3 matches to become champion
4. One loss eliminates you
5. Press Enter between rounds to continue

### Gameplay
- Headbutt the ball to score (hit with head for stronger shots)
- Defend your left goal, attack the right goal
- Ball bounces off crossbars and ground
- CPU AI moves on its half to intercept ball

### Player Instructions
**Positioning:**
- Start on the left side of the field (red player)
- Use left/right arrows to position yourself under the ball
- Press spacebar to jump when ball is overhead for better headers

**Scoring Goals:**
- Time your jumps to hit the ball toward the right goal
- Head shots (ball hits head) give the ball more power than body shots
- Aim just below the crossbar for harder-to-block goals

**Defending:**
- Stay in front of your left goal when opponent attacks
- Jump to head the ball away from your goal
- CPU can score if ball crosses the left goal line

**Tips:**
- Use jump kicks by meeting the ball in the air
- Ball bounces unpredictably off crossbars, be ready
- CPU has reaction delays, use this to your advantage
- In overtime (Golden Goal), first goal wins immediately

## Dependencies

- Python 3.x
- pygame: `pip install pygame`