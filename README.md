### Notes App Backend

Welcome to the backend repository of our Notes App! This Django application serves as the backend server for managing notes and providing data to the [frontend](ttps://github.com/spellsharp/Notes_Frontend)

#### Features:
- RESTful API endpoints for CRUD operations on notes.
- Secure authentication and authorization mechanisms.
- Integration with databases for persistent storage.

#### How to Run:

Follow these simple steps to run the Notes App backend on your local machine:

1. **Clone the Repository:**
   ```
   git clone https://github.com/spellsharp/notes_backend.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd Notes_Backend
   ```

3. **Create a Virtual Environment (Optional but Recommended):**
   ```
   python3 -m venv venv
   ```

   This command will create a virtual environment named venv in the project directory. 
   
4. **Activate the Virtual Environment and Install Dependencies:**
   ```
   source venv/bin/activate
   pip install -r requirements.txt

   ```
   These commands will activate the virtual environment and install all the required dependencies for the Notes App backend. Make sure you have pip installed.

4. **Apply Migrations:**
   ```
   python manage.py makemigrations
   ```
   This command will create new migrations based on the changes you have made to your models.

   ```
   python manage.py migrate
   ```
   This command will apply any pending database migrations.

5. **Create Superuser (Optional):**
   ```
   python manage.py createsuperuser
   ```
   You can create a superuser to access the Django admin panel and manage users and notes.

6. **Run the Development Server:**
   ```
   python manage.py runserver
   ```
   This command will start the development server.

7. **Access the API Endpoints:**
   Open your web browser or use tools like Postman to access the API endpoints provided by the backend server.

   - Admin Panel: `http://localhost:8000/admin` (If you created a superuser)
   - API Endpoints: `http://localhost:8000/`

#### Contributing:

We welcome contributions from the community to improve the Notes App backend. If you find any bugs, have feature requests, or want to contribute enhancements, feel free to open an issue or submit a pull request.

#### Feedback:

We would love to hear your feedback about the Notes App backend! If you have any suggestions or encounter any issues, please don't hesitate to let us know by opening an issue.

---

Thank you for using our Notes App backend! 📝✨