# BlogApplication_EventManagement
Event Attendance &amp; Registration System with QR check-in, admin dashboard, and export features.  Personal Blogging Platform with user auth, content management, and commenting. Both projects include setup guides and deployment instructions.

Personal Blogging Platform:
A feature-rich blogging platform with user authentication, content management, and social engagement features.

Installation
  1. Clone the repository.
  2. Install dependencies with npm install or pip install -r requirements.txt (depending on stack)
  3. Setup environment variables for DB credentials and auth secrets.
  4. Run database migrations.
  5. Start the development server using npm run dev or python manage.py runserver.
  6. Open browser at http://localhost:3000

Environment Setup
  Prerequisites
       1. Install Node.js (v16+ recommended) with npm
       2. Install Python 3.8+ (if backend uses Python) and pip
       3. Install a relational database server (PostgreSQL or MySQL)
       4. Git for version control
     
  Steps
  1. Clone the repository
       - git clone <repo-url>
       - cd BlogApplication_EventManagement
  
  2. Install dependencies
     - For frontend: npm install
     - For backend (Python example): pip install -r requirements.txt
  
  3. Setup Database:
    - Install and run PostgreSQL or MySQL server locally or use a remote DB
    - Create a database for the project
    - Note the database name, username, and password for environment configuration
  
  4.Configure Environment Variables
    - Create a .env file at the root project directory with:
          DATABASE_URL=postgres://username:password@localhost:5432/dbname
          AUTH_SECRET=your_auth_secret_key
          NEXT_PUBLIC_API_URL=http://localhost:3000/api
    - Adapt keys depending on backend framework and authentication provider used.
  
  5. Run Database Migrations
    Run migrations to create tables based on the ORM you use:
      - For Django: python manage.py migrate
      - For Flask with Alembic, use alembic commands.
  
  6. Start Development Servers
    - Backend: python manage.py runserver or appropriate backend start command
    - Frontend: npm run dev

Deployment
  Deploying Locally
    1. Set environment variables in .env file
    2. Build the frontend for production:
    3. npm run build
    4. Run backend server in production mode with WSGI (e.g., Gunicorn for Python) or Node production server
    5. Access via localhost
  
  Deploying on a Cloud Server (e.g. DigitalOcean, AWS, Heroku)
    1. Provision a virtual server or platform with Node.js/Python and database support
    2. Clone the repo on the server
    3. Configure environment variables securely
    4. Install dependencies and build frontend
    5. Run backend with process manager (e.g., PM2) for Node or Gunicorn + Nginx for Python
    6. Setup reverse proxy with SSL termination for HTTPS
    7. Use persistent storage for database backups and logs
  
  Deploying on Vercel/Netlify (Frontend only)
    1. Connect GitHub repo to Vercel/Netlify
    2. Configure build command: npm run build
    3. Configure publish directory (e.g., .next for Next.js)
    4. Add environment variables in the dashboard
    5. Backend APIs hosted separately with accessible endpoints

Pictures of Features

1. Front Page
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/02a64fc3-e53f-4f57-aaef-ce15a1db314e" />

2. User Dashboard
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/272d7401-db13-4a4e-96fe-f6e9f34e744b" />

3. Login required for some blogs
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/0a70d813-dbc5-4559-ae5d-37c00178d4d0" />

4. Authentication using Google OAuth 2.0 authentication
<img width="1312" height="872" alt="Image" src="https://github.com/user-attachments/assets/93f7e548-b56e-4fa5-a304-92d1c992336c" />


Event Management System:
A comprehensive event attendance and registration system with QR code check-in, admin dashboard, and data export capabilities.

Installation
  1. Clone the repository.
  2. Install dependencies.
  3. Configure environment variables for the database and other secrets.
  4. Run the necessary database setup and migrations.
  5. Launch backend server and frontend server.
  6. Access the app at http://localhost:8000/

Environment Setup 
  Prerequisites
    1. Install Python 3.8+ or Node.js 16+
    2. Install Git
    3. Install and configure database (PostgreSQL/MySQL recommended)
    4. For QR code generation, ensure dependencies are installed via pip or npm

Steps
  1. Clone the repository
    - git clone <repo-url>
    - cd BlogApplication_EventManagement
  
  2.Install dependencies
    - Python backend: pip install -r requirements.txt
    - For Node backend or frontend: npm install
  
  3. Setup Database
    - Install and launch PostgreSQL/MySQL server
    - Create a dedicated database
    
  4. Configure Environment Variables
    - Create .env file with:
        DATABASE_URL=postgres://username:password@localhost:5432/eventdb
        SECRET_KEY=your_secret_key_here
        QR_SECRET_KEY=your_qr_code_secret
    - Adjust based on project config.
  
  5. Run Migrations
    - Apply ORM migrations to create tables:
    - python manage.py migrate or relevant commands
  
  6. Start Development Server
    - Run backend and (if separate) frontend servers:
    - python manage.py runserver
    - npm run dev

Deployment
  Deploying Locally
    1. Create .env with necessary keys and credentials
    2. Run production build for frontend (if applicable): npm run build
    3. Use WSGI server (Gunicorn/Daphne) or Node production server for backend
    4. Access via localhost
  
  Deploying on a Cloud VPS or Platform
    1. Setup server with necessary runtime environments
    2. Clone repo, configure environment variables securely
    3. Install dependencies and build assets
    4. Run backend with process managers and setup reverse proxy (Nginx/Apache)
    5. Secure with SSL certificates
    6. Setup regular backups for the database and exported files
  
  Deploying on Platform-as-a-Service (Heroku, AWS Elastic Beanstalk)
    1. Push code via Git
    2. Configure environment variables in platform dashboard
    3. Use managed database services or attach external DB
    4. Configure build and start commands as required by platform

  Pictures of Features
    

  
