# Student Management System

The Student Management System is a Django web application designed to manage student records, including registration information, courses, and grades. It provides a user-friendly interface for administrators to view, add, edit, and delete student data.

## Features

- **Admin Dashboard**: Secure login for administrators to access the system.
- **Student Records**: View and manage student records, including registration details, course information, and grades.
- **User Authentication**: Authentication system to control access to the application, with different levels of access for administrators and students.

## Setup

Follow these steps to set up the Student Management System on your local machine:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```bash
   https://github.com/BeckyJobita/Student-Management.git
   ```

2. **Navigate to the Project Directory**: Change your current directory to the project directory:
   ```bash
   cd student-management-system
   ```

3. **Create a Virtual Environment**: Create a virtual environment to isolate project dependencies:
   ```bash
   python3 -m venv myenv
   ```

4. **Activate the Virtual Environment**: Activate the virtual environment:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```

5. **Install Dependencies**: Install the project dependencies from the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations**: Apply database migrations to create the database schema:
   ```bash
   python manage.py migrate
   ```

7. **Create Superuser**: Create a superuser account to access the admin dashboard:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**: Start the development server to run the application locally:
   ```bash
   python manage.py runserver
   ```

9. **Access the Application**: Open a web browser and navigate to `http://127.0.0.1:8000` to access the Student Management System.

## Usage

- **Admin Dashboard**: Log in with the superuser account created during setup to access the admin dashboard. From the dashboard, you can manage student records, courses, and grades.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README file according to your specific project requirements and preferences. Make sure to include any additional setup instructions, usage guidelines, or contribution guidelines as needed.
