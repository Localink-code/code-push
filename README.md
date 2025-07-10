
# Local-Link Flask Blog Application

A modern Flask web application with cyberpunk-themed UI featuring user registration, OTP verification, and role-based access control.

## Features

- **User Registration**: Support for both regular users and admin accounts
- **OTP Verification**: Two-factor authentication via email
- **Role-based Access**: Different user roles (User/Admin) with appropriate permissions
- **Cyberpunk UI**: Modern, dark-themed interface with neon accents
- **Email Integration**: Automated OTP email sending using Gmail SMTP
- **AI-powered Content**: Dynamic email content generation using Google Gemini AI
- **Responsive Design**: Mobile-friendly interface

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login, Flask-WTF
- **Frontend**: HTML5, CSS3, JavaScript, Font Awesome
- **Database**: SQLite
- **Email**: SMTP (Gmail)
- **AI**: Google Gemini API for dynamic content generation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd flask-blog-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `secret.py` file in the `flaskblog` directory
   - Add your Google Gemini API key:
   ```python
   api_key = "your-gemini-api-key-here"
   ```

4. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
flaskblog/
├── __init__.py          # Flask app initialization
├── route.py             # Application routes and logic
├── database.py          # Database models (User, Admin)
├── form.py              # WTForms for user input validation
├── send_mail.py         # Email functionality with AI content
├── secret.py            # API keys and secrets
├── static/
│   ├── look.css         # Cyberpunk-themed CSS styles
│   └── style.js         # Frontend JavaScript
└── templates/
    ├── layout.html      # Base template
    ├── home.html        # Home page
    ├── register.html    # User registration form
    └── otp.html         # OTP verification form
```

## Configuration

### Database Configuration
- SQLite database: `sqlite:///site.db`
- Automatic table creation on first run

### Email Configuration
- SMTP Server: Gmail (smtp.gmail.com:587)
- Update email credentials in `send_mail.py`

### Security
- Secret key for session management
- CSRF protection enabled
- Password hashing (implement bcrypt for production)

## Usage

### User Registration
1. Navigate to `/register`
2. Fill in username, email, password, and select role
3. Verify email via OTP
4. Account created successfully

### OTP Verification
- Users receive OTP via email
- Admin users receive separate admin OTP
- Real-time verification process

### Role Management
- **User**: Standard user account
- **Admin**: Administrative privileges

## API Endpoints

- `GET /` - Home page (login required)
- `GET/POST /register` - User registration
- `GET/POST /otp/<page>` - OTP verification
- `GET/POST /login` - User login (placeholder)

## Development

### Adding New Features
1. Create new routes in `route.py`
2. Add corresponding templates in `templates/`
3. Update forms in `form.py` if needed
4. Add CSS styling in `static/look.css`

### Database Migration
The application automatically creates tables on startup. For schema changes:
1. Update models in `database.py`
2. Restart the application

## Security Considerations

- Implement proper password hashing for production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting for OTP requests
- Validate and sanitize user inputs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please open an issue in the repository.
