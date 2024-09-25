    Webstack - Portfolio Project
    Title: Dispatch Route

Getting started:
* Running the frontend,
- cd frontend
- npm run dev -- access the frontend http://localhost:5173

* Run Backend
-- cd backend
-- python manage.py runserver -- access the backend http://127.0.0.1:8000/

	Tools:
Backend:
- Django: Django restframework
rest_framework: a powerful and popular toolkit for building Web APIs with Django.
		- It simplifies the process of creating serializers, views, and other components for handling API requests and 				responses.
In the code, following functionalities are implemented using rest_framework:

. API view creation using @api_view decorator.
. Serializers to convert between Django models and JSON data.
. ViewSets for handling CRUD operations on models.
- pip install django-filter // for search functionality
    Api Root
The default basic root view for DefaultRouter

    "teams": "http://127.0.0.1:8000/teams/",
    "services": "http://127.0.0.1:8000/services/",
    "userrequests": "http://127.0.0.1:8000/userrequests/"

For frontend:
-  user-friendly JavaScript framework widely used for developing modern web applications. 
- Vite is a tool that helps you develop and build that application more efficiently.
- Vite is a build tool designed for working with modern JavaScript frameworks. Specifically created for Vue.js projects
  . https://vitejs.dev/
 .  https://vuejs.org/

 Usage: 
 Backend http://127.0.0.1:8000/
 Frontend http://localhost:5173/Login

