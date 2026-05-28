from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# Initializing Universe Data in Server Memory
universe_state = {
    "temperature": 25.0,
    "time_scale": 1.0,
    "disaster": "None"
}

@app.get("/")
def get_dashboard():
    # Yeh HTML/JS frontend code render karega jab tum link khologe
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Private Ghost Universe Core</title>
        <style>
            body { background: #0a0a0f; color: #fff; font-family: monospace; padding: 20px; }
            canvas { background: #000; border: 1px solid #333; display: block; margin: 20px 0; }
            .controls { display: flex; gap: 10px; margin-bottom: 20px; }
            button { background: #222; color: #0f0; border: 1px solid #0f0; padding: 10px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>🌌 GHOST OMNIVERSE PRIVATE RENDER ENGINE</h1>
        <div class="controls">
            <button onclick="changeTime(2.0)">Time Warp 2x</button>
            <button onclick="changeTime(1.0)">Normal Time</button>
            <button onclick="triggerDisaster()">Trigger Ice Age</button>
        </div>
        <canvas id="universeCanvas" width="800" height="400"></canvas>
        <div id="stats">Engine State: SECURE CLOUD DEPLOYMENT Active</div>

        <script>
            const canvas = document.getElementById('universeCanvas');
            const ctx = canvas.getContext('2d');
            let particles = [];

            // Spawn Atoms
            for(let i=0; i<30; i++) {
                particles.push({
                    x: Math.random()*canvas.width,
                    y: Math.random()*canvas.height,
                    vx: (Math.random()-0.5)*2,
                    vy: (Math.random()-0.5)*2,
                    type: Math.random() > 0.5 ? 'Hydrogen' : 'Oxygen'
                });
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Physics/Chemistry Rendering Loop
                particles.forEach((p, idx) => {
                    p.x += p.vx;
                    p.y += p.vy;

                    // Boundary Collision
                    if(p.x < 0 || p.x > canvas.width) p.vx *= -1;
                    if(p.y < 0 || p.y > canvas.height) p.vy *= -1;

                    // Render Atoms
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, 5, 0, Math.PI*2);
                    ctx.fillStyle = p.type === 'Hydrogen' ? '#00bcff' : '#ff0055';
                    ctx.fill();

                    // Simple Covalent Bonding Visualization
                    particles.forEach((p2, idx2) => {
                        if(idx !== idx2) {
                            let dist = Math.hypot(p2.x - p.x, p2.y - p.y);
                            if(dist < 30) {
                                ctx.beginPath();
                                ctx.moveTo(p.x, p.y);
                                ctx.lineTo(p2.x, p2.y);
                                ctx.strokeStyle = 'rgba(0, 255, 0, 0.2)';
                                ctx.stroke();
                            }
                        }
                    });
                });
                requestAnimationFrame(draw);
            }
            draw();

            function changeTime(scale) { alert("Time Warp Modified to: " + scale + "x"); }
            function triggerDisaster() { alert("Ice Age Triggered! Thermal Kinetic Energy Dropping..."); }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
