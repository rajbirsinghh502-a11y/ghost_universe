from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import re
import random
import math
import asyncio

app = FastAPI()

# ========================================================
# 1. THE COSMIC TIMELINE STATE MATRIX
# ========================================================
universe_state = {
    "cosmic_years": 0,           # Simulation Age Clock
    "current_era": "BIG BANG",    # The current Evolutionary Epoch
    "time_scale": 1.0,
    "temperature": 1000.0,       # Starts super hot like the actual Big Bang!
    "disaster": "Cosmic Inflation",
    "total_mutations": 0,
    "extinct_count": 0,
    "current_population": 150,
    "latest_invention": "None",
    "status_message": "🌌 COSMIC GENESIS: The Big Bang has initiated. Star dust assembling."
}

# ========================================================
# 2. EVOLVING CONSCIOUS NODE (SPECIES GENETICS)
# ========================================================
class CosmicNode:
    def __init__(self, node_id, x, y, species_type="Star Dust", gen=1):
        self.id = node_id
        self.x = x
        self.y = y
        self.vx = random.uniform(-2.0, 2.0)
        self.vy = random.uniform(-2.0, 2.0)
        
        # Biology Matrix
        self.health = 100.0
        self.energy = 100.0
        self.generation = gen
        self.species_type = species_type # "Star Dust", "Protozoa", "Dinosaur", "Human"
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

# Initial Genesis Population (Star Dust Particles)
population = [CosmicNode(i, random.uniform(300, 500), random.uniform(150, 300), "Star Dust") for i in range(150)]

class CommandInput(BaseModel):
    text: str

# ========================================================
# 3. AUTOMATED TIME-WARP ERA MANAGER (THE BRAHMAN LOOP)
# ========================================================
def manage_cosmic_evolution():
    global population
    years = universe_state["cosmic_years"]
    temp = universe_state["temperature"]
    
    # ERA 0 -> ERA 1: COOLING DOWN & EARTH FORMATION
    if universe_state["current_era"] == "BIG BANG" and years > 100:
        universe_state["current_era"] = "PRIMORDIAL EARTH"
        universe_state["temperature"] = 45.0 # Cooling down
        universe_state["disaster"] = "Ocean Formation"
        universe_state["status_message"] = "🌍 ERA SHIFT: Earth is cooling down. Oceans are forming. Single-cell life emerging!"
        for node in population:
            node.species_type = "Protozoa"
            
    # ERA 1 -> ERA 2: AGE OF DINOSAURS
    elif universe_state["current_era"] == "PRIMORDIAL EARTH" and years > 300:
        universe_state["current_era"] = "AGE OF DINOSAURS"
        universe_state["temperature"] = 32.0
        universe_state["disaster"] = "None"
        universe_state["status_message"] = "🦖 ERA SHIFT: The Carboniferous burst! Giant Dinosaurs rule the digital plane."
        for node in population:
            node.species_type = "Dinosaur"
            
    # ERA 2 -> ERA 3: THE ASTEROID EXTINCTION EVENT
    elif universe_state["current_era"] == "AGE OF DINOSAURS" and years > 500:
        universe_state["current_era"] = "ASTEROID IMPACT"
        universe_state["temperature"] = 180.0 # Extreme Heat Shock
        universe_state["disaster"] = "Chicxulub Asteroid Crash"
        universe_state["status_message"] = "☄️ CRITICAL EVENT: A massive Asteroid has hit the grid! Dinosaurs are going extinct!"
        # Kill 85% of the population instantly
        survivors = [n for n in population if random.random() < 0.15]
        population = survivors
        
    # ERA 3 -> ERA 4: HUMAN CIVILIZATION & 2026 RE-INVENTION
    elif universe_state["current_era"] == "ASTEROID IMPACT" and years > 580:
        universe_state["current_era"] = "ANTHROPOCENE (HUMANS)"
        universe_state["temperature"] = 22.0 # Perfect Living Conditions
        universe_state["disaster"] = "None"
        universe_state["status_message"] = "🧠 ERA SHIFT: Humans have evolved. Constructing internet pipelines and AI infrastructure..."
        
        # Inject modern tech baseline
        universe_state["latest_invention"] = "Silicon Microchip & AI"
        for node in population:
            node.species_type = "Human"

# ========================================================
# 4. API ENGINE CHANNELS
# ========================================================
@app.get("/api/state")
def get_state():
    global population
    dt = 0.1 * universe_state["time_scale"]
    
    # Tick the cosmic clock
    universe_state["cosmic_years"] += 1 * universe_state["time_scale"]
    
    # Check if it's time to shift history eras
    manage_cosmic_evolution()
    
    active_nodes = []
    temp = universe_state["temperature"]
    
    for node in population:
        if node.is_dead: continue
        
        # Physics Step
        node.update_physics(dt, temp)
        
        # Metabolic Entropy based on current Eras
        if universe_state["current_era"] == "BIG BANG":
            node.energy -= 0.01 * dt # Pure kinetic energy
        elif node.species_type == "Dinosaur":
            node.energy -= 0.08 * dt # Big bodies consume heavy energy
        else:
            node.energy -= 0.04 * dt
            
        # Death criteria
        if node.energy <= 0:
            node.is_dead = True
            universe_state["extinct_count"] += 1
        else:
            active_nodes.append(node)
            
    # Reproduction / Speciation Loop
    if len(active_nodes) > 0 and len(active_nodes) < 250:
        if random.random() < 0.3:
            parent = random.choice(active_nodes)
            child = CosmicNode(random.randint(10000, 99999), parent.x + random.uniform(-10, 10), parent.y + random.uniform(-10, 10), parent.species_type, parent.generation + 1)
            active_nodes.append(child)
            universe_state["total_mutations"] += 1
            
    # If complete extinction happens, prompt a sub-genesis trigger
    if len(active_nodes) == 0:
        active_nodes = [CosmicNode(random.randint(1, 1000), random.uniform(100, 700), random.uniform(100, 350), "Mammal Base") for _ in range(40)]
        universe_state["current_era"] = "MAMMALIAN REBOUND"
        
    population = active_nodes
    universe_state["current_population"] = len(population)
    
    return {
        "meta": universe_state,
        "agents": [{"x": n.x, "y": n.y, "gen": n.generation, "type": n.species_type} for n in population]
    }

@app.post("/api/command")
def post_command(data: CommandInput):
    cmd = data.text.lower()
    if "speed" in cmd or "x" in cmd:
        universe_state["time_scale"] = 5.0 # Speed up cosmic time warp
        return {"status_message": "⚡ COSMIC WARP: Time acceleration active."}
    if "reset" in cmd:
        universe_state["cosmic_years"] = 0
        universe_state["current_era"] = "BIG BANG"
        universe_state["temperature"] = 1000.0
        return {"status_message": "🔄 RAGNAROK: Universe recycled back to the primeval point."}
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
        <title>Ghost Cosmic Simulator v5.0</title>
        <style>
            body { background: #020204; color: #fff; font-family: 'Courier New', monospace; padding: 20px; display: flex; gap: 20px; margin: 0; }
            .left-panel { flex: 3; display: flex; flex-direction: column; }
            .right-panel { flex: 1.2; background: #07070c; border: 1px solid #141424; padding: 15px; border-radius: 8px; }
            canvas { background: #000; border: 2px solid #111; width: 100%; height: 450px; border-radius: 6px; }
            .metric { background: #0d0d18; padding: 10px; margin: 5px 0; border-radius: 4px; border-left: 4px solid #00f0ff; font-size: 13px; }
            .era-tag { font-size: 18px; color: #ff0055; font-weight: bold; text-align: center; border: 1px dashed #ff0055; padding: 10px; margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <div class="left-panel">
            <h2>🌌 GHOST OMNIVERSE: THE COSMIC TIMELINE ENGINE</h2>
            <canvas id="cosmicCanvas" width="800" height="450"></canvas>
            <div id="status-bar" style="color: #39ff14; margin-top: 10px; font-weight: bold;">Loading Big Bang...</div>
        </div>
        
        <div class="right-panel">
            <div class="era-tag" id="m-era">ERA: BIG BANG</div>
            <div class="metric" id="m-years">Cosmic Timeline Counter: 0</div>
            <div class="metric" id="m-pop">Total Active Species: 150</div>
            <div class="metric" id="m-temp">Ambient Temp: 1000°C</div>
            <div class="metric" id="m-disaster">Current Phase Crisis: Inflation</div>
            <div class="metric" id="m-invention" style="border-left-color: #ffaa00;">Latest Invention: None</div>
            <hr style="border-color: #141424;">
            <p style="font-size: 11px; color: #668;">Leave this window open to let the timeline organically progress across millions of digital cycles.</p>
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
                    
                    // Live UI Bindings
                    document.getElementById('m-era').innerText = `ERA: ${data.meta.current_era}`;
                    document.getElementById('m-years').innerText = `Cosmic Cycles: ${Math.floor(data.meta.cosmic_years)}`;
                    document.getElementById('m-pop').innerText = `Total Active Species: ${data.meta.current_population}`;
                    document.getElementById('m-temp').innerText = `Ambient Temp: ${data.meta.temperature}°C`;
                    document.getElementById('m-disaster').innerText = `Current Phase Crisis: ${data.meta.disaster}`;
                    document.getElementById('m-invention').innerText = `Latest Invention: ${data.meta.latest_invention}`;
                    document.getElementById('status-bar').innerText = data.meta.status_message;
                } catch(e) { console.log("Frame drop."); }
                
                renderCosmos();
                setTimeout(refreshCosmosLoop, 70);
            }

            function renderCosmos() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                nodes.forEach(n => {
                    ctx.beginPath();
                    
                    // VISUAL RENDER STYLE PER SPECIES TYPE
                    if (n.type === "Star Dust") {
                        ctx.arc(n.x, n.y, 2, 0, Math.PI * 2);
                        ctx.fillStyle = "#ffffff"; // Hot white dust
                    } else if (n.type === "Protozoa") {
                        ctx.arc(n.x, n.y, 4, 0, Math.PI * 2);
                        ctx.fillStyle = "#00ffaa"; // Organic Green
                    } else if (n.type === "Dinosaur") {
                        ctx.arc(n.x, n.y, 8, 0, Math.PI * 2); // Big Nodes!
                        ctx.fillStyle = "#ffaa00"; // Reptilian Gold
                    } else if (n.type === "Human") {
                        ctx.arc(n.x, n.y, 5, 0, Math.PI * 2);
                        ctx.fillStyle = "#00f0ff"; // Advanced Cyan
                    } else {
                        ctx.arc(n.x, n.y, 4, 0, Math.PI * 2);
                        ctx.fillStyle = "#ff0055";
                    }
                    ctx.fill();
                    
                    // Constellation mapping connections
                    nodes.forEach(n2 => {
                        let d = Math.hypot(n2.x - n.x, n2.y - n.y);
                        if (d > 0 && d < 35) {
                            ctx.beginPath();
                            ctx.moveTo(n.x, n.y);
                            ctx.lineTo(n2.x, n2.y);
                            ctx.strokeStyle = n.type === "Human" ? "rgba(0, 240, 255, 0.15)" : "rgba(255, 255, 255, 0.05)";
                            ctx.stroke();
                        }
                    });
                });
            }

            refreshCosmosLoop();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
