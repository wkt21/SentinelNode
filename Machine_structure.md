# Building the SentinelNode Machine Image

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
7. Create the image:
   ```bash
   sudo dd if=/dev/sda of=sentinelnode.img bs=1M
