from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import re
import random
import math
import asyncio

app = FastAPI()

# ========================================================
# 1. THE COSMIC TIMELINE STATE MATRIX (SPEED UNLOCKED)
# ========================================================
universe_state = {
    "cosmic_years": 0,           # Simulation Age Clock
    "current_era": "BIG BANG",    # The current Evolutionary Epoch
    "time_scale": 1.0,           # Controls the hyper-drive multiplier
    "temperature": 1000.0,       # Starts super hot like the actual Big Bang!
    "disaster": "Cosmic Inflation",
    "total_mutations": 0,
    "extinct_count": 0,
    "current_population": 150,
    "latest_invention": "None",
    "status_message": "🌌 COSMIC GENESIS: The Big Bang has initiated. Speed limits removed."
}

# ========================================================
# 2. EVOLVING CONSCIOUS NODE (SPECIES GENETICS)
# ========================================================
class CosmicNode:
    def __init__(self, node_id, x, y, species_type="Star Dust", gen=1):
        self.id = node_id
        self.x = x
        self.y = y
        self.vx = random.uniform(-2.5, 2.5)
        self.vy = random.uniform(-2.5, 2.5)

        # Biology Matrix
        self.health = 100.0
        self.energy = 100.0
        self.generation = gen
        self.species_type = species_type 
        self.is_dead = False

        # Neural Adaptability Weights
        self.brain_weights = {
            "thermal_resistance": random.uniform(-1.0, 1.0),
            "reproduction_drive": random.uniform(0.1, 1.0)
        }

    def update_physics(self, dt, temp):
        # Friction based on environmental cooling
        friction = 0.99 if temp > 500 else 1.0
        self.x += self.vx * dt * friction
        self.y += self.vy * dt * friction

        # Boundary bounces
        if self.x < 0 or self.x > 800: self.vx *= -1
        if self.y < 0 or self.y > 450: self.vy *= -1

# Initial Genesis Population
population = [CosmicNode(i, random.uniform(300, 500), random.uniform(150, 300), "Star Dust") for i in range(150)]

class CommandInput(BaseModel):
    text: str

# ========================================================
# 3. AUTOMATED TIME-WARP ERA MANAGER (SCALED FOR HIGH SPEED)
# ========================================================
def manage_cosmic_evolution():
    global population
    years = universe_state["cosmic_years"]

    # ERA 0 -> ERA 1: COOLING DOWN & EARTH FORMATION (At 1000 Cycles)
    if universe_state["current_era"] == "BIG BANG" and years > 1000:
        universe_state["current_era"] = "PRIMORDIAL EARTH"
        universe_state["temperature"] = 45.0 
        universe_state["disaster"] = "Ocean Formation"
        universe_state["status_message"] = "🌍 ERA SHIFT: Earth is cooling down. Oceans are forming. Single-cell life emerging!"
        for node in population:
            node.species_type = "Protozoa"

    # ERA 1 -> ERA 2: AGE OF DINOSAURS (At 3500 Cycles)
    elif universe_state["current_era"] == "PRIMORDIAL EARTH" and years > 3500:
        universe_state["current_era"] = "AGE OF DINOSAURS"
        universe_state["temperature"] = 32.0
        universe_state["disaster"] = "None"
        universe_state["status_message"] = "🦖 ERA SHIFT: The Carboniferous burst! Giant Dinosaurs rule the digital plane."
        for node in population:
            node.species_type = "Dinosaur"

    # ERA 2 -> ERA 3: THE ASTEROID EXTINCTION EVENT (At 7500 Cycles)
    elif universe_state["current_era"] == "AGE OF DINOSAURS" and years > 7500:
        universe_state["current_era"] = "ASTEROID IMPACT"
        universe_state["temperature"] = 180.0 
        universe_state["disaster"] = "Chicxulub Asteroid Crash"
        universe_state["status_message"] = "☄️ CRITICAL EVENT: A massive Asteroid has hit the grid! Dinosaurs are going extinct!"
        # Mass Extinction
        population = [n for n in population if random.random() < 0.12]

    # ERA 3 -> ERA 4: HUMAN CIVILIZATION & 2026 RE-INVENTION (At 9000 Cycles)
    elif universe_state["current_era"] == "ASTEROID IMPACT" and years > 9000:
        universe_state["current_era"] = "ANTHROPOCENE (HUMANS)"
        universe_state["temperature"] = 22.0 
        universe_state["disaster"] = "None"
        universe_state["status_message"] = "🧠 ERA SHIFT: Humans have evolved. Constructing internet pipelines and AI infrastructure..."
        universe_state["latest_invention"] = "Silicon Microchip & AI Networks (2026 Baseline)"
        for node in population:
            node.species_type = "Human"

# ========================================================
# 4. API ENGINE CHANNELS (CLOCK MULTIPLIER UNLOCKED)
# ========================================================
@app.get("/api/state")
def get_state():
    global population
    time_multiplier = universe_state["time_scale"]
    
    # Physics delta step controlled to prevent teleportation bugs outside canvas boundaries
    dt = 0.1 * (1.0 if time_multiplier > 50 else (time_multiplier * 0.2))

    # 🔥 The Core Speed Engine Fix: Increases cosmic clock matching your multiplier!
    universe_state["cosmic_years"] += 2.0 * time_multiplier

    # Check for historical epoch updates
    manage_cosmic_evolution()

    active_nodes = []
    temp = universe_state["temperature"]

    for node in population:
        if node.is_dead: continue

        node.update_physics(dt, temp)

        # Metabolic decay scaled by species behavior
        decay_factor = 0.09 if node.species_type == "Dinosaur" else 0.04
        node.energy -= decay_factor * dt

        if node.energy <= 0:
            node.is_dead = True
            universe_state["extinct_count"] += 1
        else:
            active_nodes.append(node)

    # Safe Population Padding to prevent total universe death during fast forwards
    if len(active_nodes) < 20:
        current_era_type = "Human" if "HUMAN" in universe_state["current_era"] else ("Protozoa" if "EARTH" in universe_state["current_era"] else "Star Dust")
        active_nodes += [CosmicNode(random.randint(1000, 9999), random.uniform(50, 750), random.uniform(50, 400), current_era_type) for _ in range(60)]

    # Speciation Reproduction Loop
    if len(active_nodes) > 0 and len(active_nodes) < 220:
        if random.random() < 0.4:
            parent = random.choice(active_nodes)
            child = CosmicNode(random.randint(10000, 99999), parent.x + random.uniform(-10, 10), parent.y + random.uniform(-10, 10), parent.species_type, parent.generation + 1)
            active_nodes.append(child)
            universe_state["total_mutations"] += 1

    population = active_nodes
    universe_state["current_population"] = len(population)

    return {
        "meta": universe_state,
        "agents": [{"x": n.x, "y": n.y, "gen": n.generation, "type": n.species_type} for n in population]
    }

@app.post("/api/command")
def post_command(data: CommandInput):
    cmd = data.text.lower()
    
    # 🔥 FIX: Dynamically grabs ANY number from your message (e.g., '200x', '500 speed')
    if speed_match := re.search(r'\d+', cmd):
        target_speed = float(speed_match.group())
        universe_state["time_scale"] = target_speed
        return {"status_message": f"⚡ HYPER TIME WARP: Speed set to {target_speed}x!"}
        
    if "reset" in cmd or "ragnarok" in cmd:
        universe_state["cosmic_years"] = 0
        universe_state["current_era"] = "BIG BANG"
        universe_state["temperature"] = 1000.0
        universe_state["time_scale"] = 1.0
        return {"status_message": "🔄 RAGNAROK: Cosmic system recycled back to T-0."}
        
    return {"status_message": "Console synchronized."}

# ========================================================
# 5. HIGH-DYNAMICS VISUALIZER DASHBOARD
# ========================================================
@app.get("/")
def get_dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ghost Cosmic Simulator v5.1 (Speed Unlocked)</title>
        <style>
            body { background: #020204; color: #fff; font-family: 'Courier New', monospace; padding: 20px; display: flex; gap: 20px; margin: 0; }
            .left-panel { flex: 3; display: flex; flex-direction: column; }
            .right-panel { flex: 1.2; background: #07070c; border: 1px solid #141424; padding: 15px; border-radius: 8px; }
            canvas { background: #000; border: 2px solid #141424; width: 100%; height: 450px; border-radius: 6px; }
            .metric { background: #0d0d18; padding: 10px; margin: 5px 0; border-radius: 4px; border-left: 4px solid #00f0ff; font-size: 13px; }
            .era-tag { font-size: 18px; color: #ff0055; font-weight: bold; text-align: center; border: 1px dashed #ff0055; padding: 10px; margin-bottom: 10px; text-shadow: 0 0 8px #ff0055; }
            input { background: #0e0e1c; color: #fff; border: 1px solid #282846; padding: 12px; font-family: monospace; border-radius: 4px; font-size: 14px; outline: none; width: 93%; }
        </style>
    </head>
    <body>
        <div class="left-panel">
            <h2>🌌 GHOST OMNIVERSE: COSMIC OVERDRIVE MATRIX</h2>
            <canvas id="cosmicCanvas" width="800" height="450"></canvas>
            <div id="status-bar" style="color: #39ff14; margin-top: 10px; font-weight: bold;">Loading Big Bang Engine...</div>
        </div>
        
        <div class="right-panel">
            <div class="era-tag" id="m-era">ERA: BIG BANG</div>
            <div class="metric" id="m-warp" style="border-left-color: #a100ff; font-weight:bold;">Core Throttle Speed: 1x</div>
            <div class="metric" id="m-years">Cosmic Cycles Counter: 0</div>
            <div class="metric" id="m-pop">Total Active Species: 150</div>
            <div class="metric" id="m-temp">Ambient Temp: 1000°C</div>
            <div class="metric" id="m-disaster">Current Phase Crisis: Inflation</div>
            <div class="metric" id="m-invention" style="border-left-color: #ffaa00;">Latest Invention: None</div>
            <hr style="border-color: #141424; margin: 15px 0;">
            <h4>💬 MATRIX CHAT TERMINAL:</h4>
            <input type="text" id="cmdInput" placeholder="Type speed parameter (e.g., 200 speed, 500x)..." onkeydown="if(event.key==='Enter') executeWarpCommand()">
        </div>

        <script>
            const canvas = document.getElementById('cosmicCanvas');
            const ctx = canvas.getContext('2d');
            let nodes = [];

            async function refreshCosmosLoop() {
                try {
                    const res = await fetch('/api/state');
                    const data = await res.json();
                    
                    nodes = data.agents;
                    
                    document.getElementById('m-era').innerText = `ERA: ${data.meta.current_era}`;
                    document.getElementById('m-warp').innerText = `Core Throttle Speed: ${data.meta.time_scale}x`;
                    document.getElementById('m-years').innerText = `Cosmic Cycles: ${Math.floor(data.meta.cosmic_years)}`;
                    document.getElementById('m-pop').innerText = `Total Active Species: ${data.meta.current_population}`;
                    document.getElementById('m-temp').innerText = `Ambient Temp: ${data.meta.temperature}°C`;
                    document.getElementById('m-disaster').innerText = `Current Phase Crisis: ${data.meta.disaster}`;
                    document.getElementById('m-invention').innerText = `Latest Invention: ${data.meta.latest_invention}`;
                    document.getElementById('status-bar').innerText = data.meta.status_message;
                } catch(e) {}
                
                renderCosmos();
                setTimeout(refreshCosmosLoop, 50); // Fluid frame refresh
            }

            function renderCosmos() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                nodes.forEach(n => {
                    ctx.beginPath();
                    if (n.type === "Star Dust") {
                        ctx.arc(n.x, n.y, 2, 0, Math.PI * 2);
                        ctx.fillStyle = "#ffffff";
                    } else if (n.type === "Protozoa") {
                        ctx.arc(n.x, n.y, 4, 0, Math.PI * 2);
                        ctx.fillStyle = "#00ffaa";
                    } else if (n.type === "Dinosaur") {
                        ctx.arc(n.x, n.y, 7, 0, Math.PI * 2);
                        ctx.fillStyle = "#ffaa00";
                    } else if (n.type === "Human") {
                        ctx.arc(n.x, n.y, 4.5, 0, Math.PI * 2);
                        ctx.fillStyle = "#00f0ff";
                    }
                    ctx.fill();
                });
            }

            async function executeWarpCommand() {
                const input = document.getElementById('cmdInput');
                const val = input.value.trim();
                if(!val) return;
                input.value = '';
                
                await fetch('/api/command', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: val})
                });
            }

            refreshCosmosLoop();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
