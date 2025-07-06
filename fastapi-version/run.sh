#!/bin/bash

# Weather Dashboard Setup and Run Script

echo "🌤️  Weather Dashboard - FastAPI Version"
echo "========================================"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "🚀 Starting Weather Dashboard..."
echo "   Access at: http://localhost:8000"
echo "   Press Ctrl+C to stop"
echo ""

python main.py
