# Dev-App

Dev-App is a Django-based application designed for developers to manage projects, communicate through messages, and handle user registration and login. The app includes various features to enhance user interaction and project management.

## Features

- **User Registration and Login**: Secure user authentication with Django's built-in user management system.
- **Profile Management**:
  - View and edit user profiles
  - Social media links
- **Project Listing**:
  - Create, edit, and delete projects
  - View project details and associated reviews
- **Messaging**:
  - Send and receive messages
  - View messages in an inbox with unread counts and conditional styling
- **Search Functionality**:
  - Search for projects by tags and attributes
- **Pagination**:
  - Paginated views for user profiles and projects
- **Reviews and Tags**:
  - Add reviews and tags to projects
- **Custom User Model**:
  - Extend the default user model with additional fields

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bulma CSS framework

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yashovardhn/Dev-App.git
    cd Dev-App
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations and run the server:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Project Structure

Dev-App/
├── devapp/
│ ├── templates/
│ ├── static/
│ ├── views.py
│ ├── models.py
│ ├── forms.py
│ └── urls.py
├── manage.py
└── requirements.txt


## Usage

- **User Registration**: Create a new account.
- **Login**: Access your account.
- **Profile Management**: Update your profile information.
- **Project Management**: Add, edit, and view projects.
- **Messaging**: Send and receive messages.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The [Bulma](https://bulma.io/) framework for CSS styling.
- The Django community for their extensive documentation and support.
