#!/usr/bin/env bash
set -e

echo "=== [Step 1] Pulling latest changes from repository ==="
git pull origin main

echo "=== [Step 2] Validating application code ==="
if [ ! -f "app.py" ]; then
    echo "[-] Error: app.py missing!"
    exit 1
fi
python3 -m py_compile app.py
echo "[+] Code syntax verified."

echo "=== [Step 3] Restarting application service ==="
# Terminate existing instance on port 8080 if running
fuser -k 8080/tcp 2>/dev/null || true

# Start server in background
nohup python3 app.py > app.log 2>&1 &
sleep 2

# Verify server responds locally
if curl -s -I http://127.0.0.1:8080 | grep -q "200 OK"; then
    echo "[+] Application deployed and running successfully!"
else
    echo "[-] Health check failed. Check app.log for details."
    exit 1
fi
