# Doctor Project

This is a Django-based Doctor Information System for managing and viewing doctor details.

## Features
- Doctor list with search and filter
- Doctor detail popup with photo and address
- Responsive, modern UI using Tailwind CSS
- Admin  support

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Midlester/Doctor_Project.git
   cd Doctor_Project
   ```
2. **Install dependencies:**
   - Python 3.8+
   - Django 4+
   - (Optional) Node.js for frontend assets
3. **Activate virtual environment:**
   ```bash
   core/Scripts/activate  # On Windows
   source core/bin/activate  # On Linux/Mac
   ```
4. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Start the server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   Open your browser at [http://localhost:8000](http://localhost:8000)

## Tailwind CSS Commands
If you use Tailwind CSS and need to build or watch CSS changes, run:
```bash
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

## Project Structure
- `doctor_project/` - Main Django project
- `doctor_info/` - Doctor app
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)

## License
This project is for educational/demo purposes.
