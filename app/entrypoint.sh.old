#!/bin/bash

HOSTNAME=$(hostname)
IP=$(hostname -i)
DATE=$(date)

cat <<EOF > /usr/share/nginx/html/index.html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Balanceador Dani</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Inter", "Segoe UI", Roboto, sans-serif;
}

/* Fondo animado */
body {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(-45deg, #6b73ff, #000dff, #00c6ff, #00ff6a);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  overflow: hidden;
}

@keyframes gradientBG {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Tarjeta */
.container {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 50px;
  width: 460px;
  text-align: center;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  animation: fadeIn 1s ease forwards;
}

/* Animación entrada */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Títulos y textos */
h1 {
  font-size: 28px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 30px;
  letter-spacing: 0.5px;
}

.info {
  background: rgba(255,255,255,0.2);
  padding: 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 16px;
  color: #f0f0f0;
  border: 1px solid rgba(255,255,255,0.3);
  transition: transform 0.2s ease;
}

.info:hover {
  transform: translateY(-3px);
}

.label {
  font-weight: 600;
}

.status {
  margin-top: 25px;
  padding: 12px;
  border-radius: 12px;
  background: #22c55e;
  color: white;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: background 0.3s ease;
}

.status:hover {
  background: #16a34a;
}

.footer {
  margin-top: 25px;
  font-size: 12px;
  color: rgba(255,255,255,0.7);
}

/* Partículas */
.particles {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
  top: 0;
  left: 0;
  z-index: 0;
  pointer-events: none;
}

.particle {
  position: absolute;
  width: 8px;
  height: 8px;
  background: rgba(255,255,255,0.3);
  border-radius: 50%;
  animation: floatParticle 20s linear infinite;
}

@keyframes floatParticle {
  0% { transform: translateY(100vh) translateX(0); opacity: 0; }
  10% { opacity: 1; }
  100% { transform: translateY(-10vh) translateX(50px); opacity: 0; }
}
</style>
</head>
<body>

<!-- Más partículas -->
<div class="particles">
  <div class="particle" style="left:10%; animation-delay: 0s;"></div>
  <div class="particle" style="left:30%; animation-delay: 5s;"></div>
  <div class="particle" style="left:50%; animation-delay: 2s;"></div>
  <div class="particle" style="left:70%; animation-delay: 7s;"></div>
  <div class="particle" style="left:90%; animation-delay: 4s;"></div>
</div>

<div class="container">
  <h1>Balanceador Traefik Infraestructura Dani</h1>

  <div class="info">
    <span class="label">Servidor:</span> $HOSTNAME
  </div>

  <div class="info">
    <span class="label">IP interna:</span> $IP
  </div>

  <div class="status">
    BACKEND ACTIVO
  </div>

  <div class="footer">
    Generado: $DATE
  </div>
</div>

</body>
</html>
EOF

nginx -g "daemon off;"
