@echo off

echo ======== Starting Prompt Retreiver from %cd% =========
echo [PR Launcher] Activating Conda environment...
call conda activate promptretreiver

echo [PR Launcher] Launching Prompt Retreiver...
call python webui.py

echo [PR Launcher] Process got interrupted
pause