SentinelNode — OSINT Intelligence Documentation

Executive Summary

SentinelNode is a controlled, fictional HTB‑style machine designed to simulate an AI‑defense environment.
The OSINT footprint intentionally exposes misleading artifacts, decoy services, and logic‑based puzzles.

This documentation outlines the intelligence‑gathering process an analyst would follow before exploitation.

---

🛰️ 1. Surface Reconnaissance

Initial OSINT collection focuses on publicly visible machine metadata, banners, and exposed services.

1.1 Host Fingerprinting

• Hostname: sentinelnode.local
• OS: Ubuntu 22.04 Server
• Web Stack: Nginx + PHP / optional Flask
• Open Ports:• 80/tcp — Web Challenge
• 22/tcp — Fake SSH
• 8822/tcp — Backdoor AI‑Defense Port



1.2 Web Banner Enumeration

The landing page reveals:

• AI‑Defense theme
• DOM‑based puzzle hints
• JavaScript references to hidden DOM nodes


1.3 Service Banners

• Port 22: “Fake SSH Service”
• Port 8822: “AI‑Defense Layer 1”


These banners are intentionally misleading and part of the puzzle chain.

---

🛰️ 2. Web OSINT Collection

The web challenge is the primary OSINT surface.

2.1 HTML Structure Analysis

Key findings:

• Hidden DOM elements containing partial flag fragments
• JavaScript obfuscation in static/js/app.js
• Decoy admin panel at /admin/panel.php
• Fake SQLi endpoint at /api/sqli_sim.php


2.2 Directory Enumeration

Common findings:

/static/css/style.css
/static/js/app.js
/api/sqli_sim.php
/admin/panel.php
/img/banner.png


2.3 SQLi Simulation Endpoint

The endpoint returns controlled responses:

• "admin'--" → Decoy table message
• Other queries → “Invalid query”


This is a logic puzzle, not a real SQL engine.

---

🛰️ 3. Service OSINT

SentinelNode exposes two custom services.

3.1 Fake SSH (Port 22)

Purpose:

• Misdirection
• Teaches analysts to validate service authenticity
• Provides no shell access


3.2 Backdoor AI‑Defense Port (8822)

Purpose:

• Multi‑phase puzzle entry point
• Returns AI‑Defense “layers”
• Requires sequential reasoning to progress


---

🛰️ 4. File System Intelligence

Flags stored in:

/opt/sentinelnode/flags/


Service scripts stored in:

/opt/sentinelnode/services/


Web content stored in:

/var/www/html/


---

🛰️ 5. Threat Model Simulation

SentinelNode simulates:

• AI‑defense misdirection
• Logic‑based exploitation
• Controlled SQLi scenarios
• Multi‑phase reasoning puzzles


Adversary Emulation Goals

• Test analyst ability to distinguish real vs decoy services
• Evaluate DOM enumeration skills
• Assess logic‑chain reasoning under misleading conditions


---

🛰️ 6. Intelligence Summary

SentinelNode’s OSINT footprint is intentionally noisy.
Analysts must filter:

• Decoy admin panels
• Fake SQLi responses
• Fake SSH banners
• AI‑Defense “layers”


True attack surface emerges only after:

• DOM enumeration
• Logic‑based SQLi simulation
• Backdoor port analysis


---

🛰️ 7. OSINT Artifacts

Below is a structured list of artifacts discovered during reconnaissance.

Web Artifacts

• /index.html
• /static/js/app.js
• /static/css/style.css
• /api/sqli_sim.php
• /admin/panel.php


Service Artifacts

• backdoor_service.py
• fake_ssh.py
• backdoor.service
• fake_ssh.service


Flag Artifacts

• flag1.txt
• flag2.txt
• flag3.txt


---

🛰️ 8. Analyst Notes

SentinelNode is designed to:

• Teach OSINT filtering
• Encourage multi‑layer reasoning
• Simulate AI‑defense misdirection
• Provide a safe, fictional training environment

