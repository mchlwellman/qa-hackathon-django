# qa-hackathon-django

A starter Django project with the first step of the official Django tutorial completed.

## Project Structure

This project includes:
- Django 5.2.7 installation
- A Django project named `mysite`
- A `polls` app (from Django tutorial part 1)
- Initial views and URL routing configured

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mchlwellman/qa-hackathon-django.git
cd qa-hackathon-django
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Open your browser and visit:
   - `http://127.0.0.1:8000/polls/` - Polls app index page
   - `http://127.0.0.1:8000/admin/` - Django admin interface

## What's Included

This project completes part 1 of the official Django tutorial, which includes:
- Creating a Django project
- Creating the `polls` application
- Writing a simple view
- Configuring URL routing

## Next Steps

To continue with the Django tutorial:
- Part 2: Database setup and models
- Part 3: Views and templates
- Part 4: Forms and generic views
- Part 5: Testing
- Part 6: Static files
- Part 7: Customizing the admin site

Visit the [official Django tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) for more information.
