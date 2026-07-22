# SentinelNode
AI‑Defense Challenge | HTB‑Style Machine by wkt12**  SentinelNode is a fictional HackTheBox‑style machine designed for CTF environments.   It combines web exploitation, logic puzzles, and AI‑defense misdirection.

<img width="1536" height="1024" alt="IMG_2951" src="https://github.com/user-attachments/assets/8fa6d097-d15b-4339-80d5-a0193565b5e9" />


---

## 🧠 Overview
- **Difficulty:** Medium–Hard  
- **Category:** Web / Logic / AI‑Defense  
- **Flags:** 3  
- **Author:** wkt12  

---

## 🧩 Challenge Flow
1. DOM manipulation → Flag 1  
2. SQL injection simulation → Port 8822 discovery  
3. Multi‑phase AI‑defense puzzle → Flag 2  
4. Logic reasoning → Flag 3  

---

## 🛠️ Setup
See `MACHINE_STRUCTURE.md` for deployment steps.

---

## 📜 License
This repository is for educational and CTF purposes only.🧩 RELEASE_NOTES.mdmarkdownCopy# SentinelNode — Release Notes

## v1.0.0
- Initial release
- Added DOM challenge
- Added SQLi simulation engine
- Added admin panel with decoy tables
- Added fake SSH service
- Added backdoor port puzzle (multi‑phase)
- Added flags 1–3🧩 MACHINE_STRUCTURE.mdmarkdownCopy# Building the SentinelNode Machine Image

## Requirements
- Ubuntu 22.04 Server
- Nginx + PHP or Python Flask
- Python 3.10+
- Systemd

## Steps
1. Install Ubuntu Server in a VM.
2. Copy the `web/`, `services/`, and `flags/` directories into the VM.
3. Configure Nginx to serve `/var/www/html`.
4. Install systemd services for:
   - backdoor_service.py
   - fake_ssh.py
5. Place flags in `/opt/sentinelnode/flags/`.
6. Shut down the VM.
7. Create the image:sudo dd if=/dev/sda of=sentinelnode.img bs=1MCopy8. Compress:gzip sentinelnode.imgCopyUpload `sentinelnode.img.gz` to your GitHub release.🧩 CONTRIBUTING.mdmarkdownCopy# Contributing to SentinelNode

We welcome contributions that improve clarity, documentation, or educational value.

## Guidelines
- Keep all content safe and fictional.
- Do not introduce real vulnerabilities.
- Follow the existing folder structure.
- Use Markdown for documentation.
- Attribute all contributions in `CREDITS.md`.

## Pull Request Process
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request with a clear description.🧩 LICENSE.mdmarkdownCopy# License

SentinelNode © 2026 wkt12

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software for educational and non‑commercial purposes only.🧩 CHANGELOG.mdmarkdownCopy# SentinelNode — Changelog

## [1.0.0] — 2026‑07‑22
### Added
- Initial machine release
- DOM enumeration challenge
- SQLi simulation engine
- Admin panel with decoy tables
- Backdoor port puzzle
- Fake SSH service
- Flags 1–3

### Fixed
- Minor syntax corrections in fake_db.py🧩 CREDITS.mdmarkdownCopy# SentinelNode — Credits

