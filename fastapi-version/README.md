# Weather Updates Dashboard - FastAPI Version

A modern weather dashboard built with FastAPI and HTMX, featuring real-time weather updates for multiple cities.

## Features

- **Modern UI**: Clean, responsive design with Bootstrap 5
- **Real-time Updates**: HTMX-powered refresh buttons for instant weather updates
- **4 City Dashboard**: Displays weather for New York, London, Tokyo, and Sydney
- **Interactive Cards**: Hover effects and smooth animations
- **Mobile Responsive**: Works perfectly on all device sizes

## Setup Instructions

### 1. Create Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

The application will be available at: `http://localhost:8000`

## Project Structure

```
fastapi-version/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html         # Main dashboard page
│   └── weather_card.html  # Weather card component
└── static/
    └── style.css          # Custom styles
```

## API Integration

Currently, the app uses mock weather data. To integrate with a real weather API:

1. Replace the `get_mock_weather_data()` function in `main.py`
2. Add your API key to environment variables
3. Update the weather data structure as needed

Example APIs you can integrate:
- OpenWeatherMap API
- WeatherAPI
- AccuWeather API

## Technologies Used

- **Backend**: FastAPI
- **Frontend**: HTML, CSS, Bootstrap 5
- **Interactivity**: HTMX
- **Icons**: Font Awesome
- **Template Engine**: Jinja2

## Customization

- **Cities**: Modify the city names in `templates/index.html`
- **Styling**: Update `static/style.css` for custom themes
- **Weather Data**: Replace mock data with real API calls in `main.py`
