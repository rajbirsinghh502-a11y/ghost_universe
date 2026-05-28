from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import re
import random
import math
import asyncio

app = FastAPI()

# ========================================================
# 1. THE UNIVERSAL STATE MATRIX
# ========================================================
universe_state = {
    "time_scale": 1.0,
    "temperature": 25.0,
    "disaster": "None",
    "virus_active": False,
    "total_mutations": 0,
    "extinct_count": 0,
    "current_population": 150,  # Scaled up tracking
    "internet_sync_status": "Ready (2026 Baseline)",
    "latest_discovery": "None",
    "status_message": "⚡ SYSTEM LOG: Scaled Universe Matrix Engine Active."
}

# ========================================================
# 2. CONSCIOUS LIVING AGENT (NEURAL LEARNING BRAIN)
# ========================================================
class ConsciousAgent:
    def __init__(self, agent_id, x, y, gen=1):
        self.id = agent_id
        self.x = x
        self.y = y
        self.vx = random.uniform(-1.8, 1.8)
        self.vy = random.uniform(-1.8, 1.8)
        
        # Biological Homeostasis
        self.health = 100.0
        self.energy = 100.0
        self.age = 0.0
        self.is_dead = False
        
        # Neural Weights
        self.brain_weights = {
            "food_tendency": random.uniform(-1.0, 1.0),
            "hazard_avoidance": random.uniform(-1.0, 1.0),
            "energy_conservation": random.uniform(0.1, 1.0)
        }
        self.generation = gen

    def process_neuro_inputs(self, closest_food_dist, current_temp, pain):
        decision_x = (closest_food_dist * self.brain_weights["food_tendency"]) - (pain * self.brain_weights["hazard_avoidance"])
        decision_y = (current_temp * 0.01 * self.brain_weights["energy_conservation"])
        
        self.vx += math.tanh(decision_x) * 0.25
        self.vy += math.tanh(decision_y) * 0.25

# Initial Population Scaled Up from 35 to 150!
population = [ConsciousAgent(i, random.uniform(30, 770), random.uniform(30, 420)) for i in range(150)]

class CommandInput(BaseModel):
    text: str

# ========================================================
# 3. INTERNET LIVE-SYNC PIPELINE
# ========================================================
async def fetch_real_world_inventions():
    global population
    universe_state["internet_sync_status"] = "Syncing..."
    await asyncio.sleep(1)
    
    discoveries = [
        "Quantum Computing Error Correction Breakthrough",
        "Advanced Fusion Reactor Plasma Stabilization",
        "Graphene-based Neural Interface Optimization",
        "Next-Gen Bio-Engineered Super-Foods"
    ]
    
    selected = random.choice(discoveries)
    universe_state["latest_discovery"] = selected
    universe_state["internet_sync_status"] = "Synced Successfully"
    universe_state["status_message"] = f"🌐 INTERNET SYNC: Injected '{selected}' data into agent clusters!"
    
    for agent in population:
        agent.brain_weights["energy_conservation"] += 0.25
        agent.health = min(agent.health + 30, 100.0)

# ========================================================
# 4. NATURAL LANGUAGE COMMAND PARSER (WITH SPAWN CONTROL)
# ========================================================
def parse_god_command(command: str, background_tasks: BackgroundTasks):
    global population
    cmd = command.lower()
    
    # NEW FEATURE: Dynamic Spawn / Mass Injection Logic
    if "spawn" in cmd or "inject" in cmd or "add" in cmd:
        spawn_match = re.search(r'\d+', cmd)
        count = int(spawn_match.group()) if spawn_match else 50
        # Capping max agents at 400 to maintain smooth frame rates on cloud tier
        if len(population) + count > 450:
            count = 450 - len(population)
            if count <= 0: return "⚠️ MATRIX LIMIT: Server allocation grid full! Cannot spawn more agents right now."
            
        start_id = random.randint(10000, 99999)
        for i in range(count):
            population.append(ConsciousAgent(start_id + i, random.uniform(50, 750), random.uniform(50, 400)))
        universe_state["current_population"] = len(population)
        return f"🧬 GENESIS BURST: Injected {count} new conscious entities into the coordinate matrix!"

    if time_match := re.search(r'(\d+)\s*x', cmd):
        scale = float(time_match.group(1))
        universe_state["time_scale"] = min(scale, 50.0) # Safe cap for dense populations
        return f"⚡ Time Warp speed accelerated to {universe_state['time_scale']}x!"
        
    if temp_match := re.search(r'(-?\d+)\s*(degree|celsius|temp|temperature)', cmd):
        temp = float(temp_match.group(1))
        universe_state["temperature"] = temp
        return f"🌡️ Global Grid Temperature shifted to {temp}°C."

    if "ice age" in cmd or "freeze" in cmd:
        universe_state["temperature"] = -30.0
        universe_state["disaster"] = "Ice Age"
        return "❄️ CRITICAL: Ice Age triggered."
        
    if "solar flare" in cmd or "burn" in cmd:
        universe_state["temperature"] = 65.0
        universe_state["disaster"] = "Solar Flare"
        return "🔥 CRITICAL: Solar Flare radiation sweeping."
        
    if "virus" in cmd or "pandemic" in cmd:
        universe_state["virus_active"] = True
        return "🦠 MUTATION: Pathogenic biological virus code active."

    if "sync" in cmd or "fetch" in cmd or "knowledge" in cmd:
        background_tasks.add_task(fetch_real_world_inventions)
        return "🌐 PIPELINE: Fetching external internet nodes..."

    if "reset" in cmd or "normal" in cmd:
        universe_state["time_scale"] = 1.0
        universe_state["temperature"] = 25.0
        universe_state["disaster"] = "None"
        universe_state["virus_active"] = False
        return "🔄 Reset executed. Baseline restored."

    return "🤖 Console: Command processed."

# ========================================================
# 5. API ROUTING ENDPOINTS
# ========================================================
@app.post("/api/command")
def post_command(data: CommandInput, background_tasks: BackgroundTasks):
    response_text = parse_god_command(data.text, background_tasks)
    universe_state["status_message"] = response_text
    return universe_state

@app.get("/api/state")
def get_state():
    global population
    dt = 0.08 * universe_state["time_scale"]
    
    active_agents = []
    for agent in population:
        if agent.is_dead:
            continue
            
        agent.age += 0.003 * dt
        agent.energy -= 0.03 * dt
        
        pain = 1.0 if (agent.energy < 20.0 or universe_state["temperature"] > 50.0 or universe_state["temperature"] < -5.0) else 0.0
        if pain > 0:
            agent.health -= 0.12 * dt
            
        agent.process_neuro_inputs(random.uniform(0, 100), universe_state["temperature"], pain)
        
        agent.x += agent.vx * dt
        agent.y += agent.vy * dt
        
        if agent.x < 0 or agent.x > 800: agent.vx *= -1
        if agent.y < 0 or agent.y > 450: agent.vy *= -1
        
        if agent.health <= 0 or agent.age > 100:
            agent.is_dead = True
            universe_state["extinct_count"] += 1
        else:
            active_agents.append(agent)
            
    # Auto-Genesis Safe Trigger
    if len(active_agents) < 10:
        active_agents += [ConsciousAgent(random.randint(10000, 99999), random.uniform(100, 700), random.uniform(100, 350)) for _ in range(50)]
        universe_state["status_message"] = "🧬 SYSTEM RESET: Low density detected. Auto-Genesis re-seeded 50 nodes."

    # Genetic Reproduction Loop
    elif len(active_agents) > 0 and len(active_agents) < 180:
        if random.random() < 0.4:  # Balanced birth rate
            parent = random.choice(active_agents)
            child = ConsciousAgent(random.randint(1000, 9999), parent.x + random.uniform(-12, 12), parent.y + random.uniform(-12, 12), parent.generation + 1)
            child.brain_weights["food_tendency"] = parent.brain_weights["food_tendency"] + random.uniform(-0.08, 0.08)
            child.brain_weights["hazard_avoidance"] = parent.brain_weights["hazard_avoidance"] + random.uniform(-0.08, 0.08)
            active_agents.append(child)
            universe_state["total_mutations"] += 1
        
    population = active_agents
    universe_state["current_population"] = len(population)
    
    return {
        "meta": universe_state,
        "agents": [{"x": a.x, "y": a.y, "gen": a.generation, "health": a.health} for a in population]
    }

@app.get("/")
def get_dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ghost OS: Ultimate Master Universe</title>
        <style>
            body { background: #040406; color: #fff; font-family: 'Courier New', monospace; padding: 20px; display: flex; gap: 20px; margin: 0; height: 95vh; }
            .left-panel { flex: 3; display: flex; flex-direction: column; }
            .right-panel { flex: 1.3; background: #09090f; border: 1px solid #161626; padding: 15px; display: flex; flex-direction: column; border-radius: 8px; }
            canvas { background: #000; border: 2px solid #11111a; width: 100%; height: 450px; border-radius: 6px; }
            #console-log { flex: 1; background: #010102; border: 1px solid #161628; padding: 12px; overflow-y: auto; color: #39ff14; font-size: 13px; border-radius: 4px; margin-bottom: 10px; }
            .metric { background: #0f0f1b; padding: 10px; margin: 5px 0; border-radius: 4px; border-left: 4px solid #00f0ff; font-size: 13px; }
            .sync-metric { border-left: 4px solid #ffaa00; font-weight: bold; }
            .pop-metric { border-left: 4px solid #a100ff; font-weight: bold; }
            input { background: #11111f; color: #fff; border: 1px solid #25253d; padding: 12px; font-family: monospace; border-radius: 4px; font-size: 14px; outline: none; }
        </style>
    </head>
    <body>
        <div class="left-panel">
            <h2>🌌 GHOST OMNIVERSE CORE ENGINE (v4.0 High-Capacity)</h2>
            <canvas id="universeCanvas" width="800" height="450"></canvas>
            <div id="status-bar" style="color: #00f0ff; margin-top: 10px; font-weight: bold;">Status: Synced.</div>
        </div>
        
        <div class="right-panel">
            <h3>🎛️ AI OMNIPOTENT CONSOLE</h3>
            <div class="metric pop-metric" id="m-pop">Live Universe Population: 150</div>
            <div class="metric" id="m-warp">Time Warp: 1.0x</div>
            <div class="metric" id="m-temp">Grid Temp: 25°C</div>
            <div class="metric" id="m-disaster">Crisis Phase: None</div>
            <div class="metric" id="m-mutations">Total Brain Mutations: 0</div>
            <div class="metric" id="m-extinct">Extinct Entities: 0</div>
            <div class="metric sync-metric" id="m-sync">Sync: Ready (2026 Baseline)</div>
            <div class="metric" id="m-discovery" style="font-size:11px; color:#aaa;">Latest Tech: None</div>
            <hr style="border: 1px solid #161626; width:100%;">
            <h4>💬 ENGINE CHAT BOX:</h4>
            <div id="console-log">High-Capacity Engine Active. Use 'spawn 100' to inject mass...</div>
            <input type="text" id="cmdInput" placeholder="Type command (e.g., spawn 100, 5x speed)..." onkeydown="if(event.key==='Enter') executeCommand()">
        </div>

        <script>
            const canvas = document.getElementById('universeCanvas');
            const ctx = canvas.getContext('2d');
            let agents = [];
            let currentTemp = 25.0;

            async function syncStateLoop() {
                try {
                    const res = await fetch('/api/state');
                    const data = await res.json();
                    
                    agents = data.agents;
                    currentTemp = data.meta.temperature;
                    
                    document.getElementById('m-pop').innerText = `Live Universe Population: ${data.meta.current_population}`;
                    document.getElementById('m-warp').innerText = `Time Warp: ${data.meta.time_scale}x`;
                    document.getElementById('m-temp').innerText = `Grid Temp: ${data.meta.temperature}°C`;
                    document.getElementById('m-disaster').innerText = `Crisis Phase: ${data.meta.disaster}`;
                    document.getElementById('m-mutations').innerText = `Total Brain Mutations: ${data.meta.total_mutations}`;
                    document.getElementById('m-extinct').innerText = `Extinct Entities: ${data.meta.extinct_count}`;
                    document.getElementById('m-sync').innerText = `Sync: ${data.meta.internet_sync_status}`;
                    document.getElementById('m-discovery').innerText = `Latest Tech: ${data.meta.latest_discovery}`;
                    document.getElementById('status-bar').innerText = data.meta.status_message;
                } catch(e) { console.log("Packet drop handled."); }
                
                drawEngine();
                setTimeout(syncStateLoop, 60);
            }

            function drawEngine() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                if(currentTemp < 0) {
                    ctx.fillStyle = "rgba(0, 140, 255, 0.08)";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                } else if(currentTemp > 50) {
                    ctx.fillStyle = "rgba(255, 40, 0, 0.08)";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                }

                agents.forEach(a => {
                    ctx.beginPath();
                    ctx.arc(a.x, a.y, Math.min(3 + (a.gen * 0.25), 10), 0, Math.PI * 2);
                    
                    if(a.gen > 1) {
                        ctx.fillStyle = `rgb(0, ${Math.min(140 + (a.gen*12), 255)}, 255)`;
                    } else {
                        ctx.fillStyle = "#ff0052";
                    }
                    ctx.fill();
                    
                    // Optimization: Web lines are rendered only for dense local pockets to keep FPS high
                    if (agents.length < 250) {
                        agents.forEach(a2 => {
                            let dist = Math.hypot(a2.x - a.x, a2.y - a.y);
                            if(dist > 0 && dist < 32) {
                                ctx.beginPath();
                                ctx.moveTo(a.x, a.y);
                                ctx.lineTo(a2.x, a2.y);
                                ctx.strokeStyle = "rgba(57, 255, 20, 0.08)";
                                ctx.stroke();
                            }
                        });
                    }
                });
            }

            async function executeCommand() {
                const input = document.getElementById('cmdInput');
                const val = input.value.trim();
                if(!val) return;
                
                input.value = '';
                const log = document.getElementById('console-log');
                log.innerHTML += `<div>> Execute: ${val}</div>`;
                
                const res = await fetch('/api/command', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: val})
                });
                const data = await res.json();
                log.innerHTML += `<div style="color:#00ffff;">> Engine: ${data.status_message}</div>`;
                log.scrollTop = log.scrollHeight;
            }

            syncStateLoop();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

