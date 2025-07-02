<<<<<<< HEAD
# booking_api
A scheduler and booking api application made using Django.
=======
# Booking API

This Django project provides a booking API with the following features:
- Manage user **availabilities** (day of week, start/end times).
- Allow **bookings** that must fit within those availabilities.
- Swagger/OpenAPI documentation at `/swagger/`, "swagger.json" is the json format of the swagger documentation.

## Setup

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Apply migrations:
    ```bash
   python manage.py makemigrations scheduler
   python manage.py migrate

4. Create a superuser to access Django admin:
   ```bash
   python manage.py createsuperuser
   
   # Create more users by going to http://localhost:8000/admin/, after running the server.
5. Run the development server:

    ```bash
   python manage.py runserver

6. Run testcases `scheduler/tests.py`

    ```bash
   python manage.py test

Access the API:
- Swagger UI: http://localhost:8000/swagger/
- Availability endpoint: http://localhost:8000/api/availability/
- Booking endpoint: http://localhost:8000/api/booking/
>>>>>>> 467b797 (added-booking-and-scheduler-apis)
