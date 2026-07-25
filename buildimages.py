import os
import subprocess
from pathlib import Path

TARGET_DIR = Path("Resources/Maps/_RMC14/Inserts/LV624")
PROJECT_PATH = "Content.MapRenderer"

def run_map_renderer_batch(target_directory):
    target_path = Path(target_directory)

    if not target_path.exists():
        print(f"Error: Directory '{target_path}' does not exist.")
        return

    yml_files = sorted([f for f in target_path.iterdir() if f.suffix in ('.yml', '.yaml')])

    if not yml_files:
        print(f"No YAML files found in '{target_path}'.")
        return

    print(f"Found {len(yml_files)} files to process in '{target_path}'.\n")

    for index, file_path in enumerate(yml_files, start=1):
        formatted_file_path = file_path.as_posix()

        command = [
            "dotnet", "run",
            "--project", PROJECT_PATH,
            "-c", "Release",
            "--",
            "--format", "webp",
            "-m",
            "-f", formatted_file_path
        ]

        print(f"[{index}/{len(yml_files)}] Processing: {file_path.name}")
        print(f"Executing: {' '.join(command)}")

        try:
            result = subprocess.run(command, check=True, text=True)
            print(f"✓ Finished {file_path.name}\n")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to process {file_path.name} (Exit code: {e.returncode})\n")
        except FileNotFoundError:
            print("Error: 'dotnet' CLI tool was not found on your PATH. Make sure the .NET SDK is installed.")
            break

if __name__ == "__main__":
    run_map_renderer_batch(TARGET_DIR)