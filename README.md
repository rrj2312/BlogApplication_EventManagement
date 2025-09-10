# BlogApplication_EventManagement
Event Attendance &amp; Registration System with QR check-in, admin dashboard, and export features.  Personal Blogging Platform with user auth, content management, and commenting. Both projects include setup guides and deployment instructions.

Personal Blogging Platform:
A feature-rich blogging platform with user authentication, content management, and social engagement features.

Installation
- Clone the repository.
- Install dependencies with npm install or pip install -r requirements.txt (depending on stack)
- Setup environment variables for DB credentials and auth secrets.
- Run database migrations.
- Start the development server using npm run dev or python manage.py runserver.
- Open browser at http://localhost:3000

Environment Setup
  Prerequisites:
- Install Node.js (v16+ recommended) with npm
- Install Python 3.8+ (if backend uses Python) and pip
- Install a relational database server (PostgreSQL or MySQL)
- Git for version control
     
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
          - DATABASE_URL=postgres://username:password@localhost:5432/dbname
          - AUTH_SECRET=your_auth_secret_key
          - NEXT_PUBLIC_API_URL=http://localhost:3000/api
    - Adapt keys depending on backend framework and authentication provider used.
  
  5. Run Database Migrations
    Run migrations to create tables based on the ORM you use:
    - For Django: python manage.py migrate
    - For Flask with Alembic, use alembic commands.
  
  7. Start Development Servers
    - Backend: python manage.py runserver or appropriate backend start command
    - Frontend: npm run dev

Deployment
  Deploying Locally
  - Set environment variables in .env file
Build the frontend for production:
  - npm run build
  - Run backend server in production mode with WSGI (e.g., Gunicorn for Python) or Node production server
  - Access via localhost
  
  Deploying on a Cloud Server (e.g. DigitalOcean, AWS, Heroku)
  - Provision a virtual server or platform with Node.js/Python and database support
  - Clone the repo on the server
  - Configure environment variables securely
  - Install dependencies and build frontend
  - Run backend with process manager (e.g., PM2) for Node or Gunicorn + Nginx for Python
  - Setup reverse proxy with SSL termination for HTTPS
  - Use persistent storage for database backups and logs
  
  Deploying on Vercel/Netlify (Frontend only)
  - Connect GitHub repo to Vercel/Netlify
  - Configure build command: npm run build
  - Configure publish directory (e.g., .next for Next.js)
  - Add environment variables in the dashboard
  - Backend APIs hosted separately with accessible endpoints

Pictures of Features
1. Front Page
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/02a64fc3-e53f-4f57-aaef-ce15a1db314e" />

2. User Dashboard
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/272d7401-db13-4a4e-96fe-f6e9f34e744b" />

3. Login required for some blogs
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/0a70d813-dbc5-4559-ae5d-37c00178d4d0" />

4. Authentication using Google OAuth 2.0 authentication
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/93f7e548-b56e-4fa5-a304-92d1c992336c" />


Event Management System:
A comprehensive event attendance and registration system with QR code check-in, admin dashboard, and data export capabilities.

Installation
- Clone the repository.
- Install dependencies.
- Configure environment variables for the database and other secrets.
- Run the necessary database setup and migrations.
- Launch backend server and frontend server.
- Access the app at http://localhost:8000/

Environment Setup 
Prerequisites
- Install Python 3.8+ or Node.js 16+
- Install Git
- Install and configure database (PostgreSQL/MySQL recommended)
- For QR code generation, ensure dependencies are installed via pip or npm

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
        - DATABASE_URL=postgres://username:password@localhost:5432/eventdb
        - SECRET_KEY=your_secret_key_here
        - QR_SECRET_KEY=your_qr_code_secret
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
  - Create .env with necessary keys and credentials
  - Run production build for frontend (if applicable): npm run build
  - Use WSGI server (Gunicorn/Daphne) or Node production server for backend
  - Access via localhost
  
  Deploying on a Cloud VPS or Platform
   - Setup server with necessary runtime environments
   - Clone repo, configure environment variables securely
   - Install dependencies and build assets
   - Run backend with process managers and setup reverse proxy (Nginx/Apache)
   - Secure with SSL certificates
   - Setup regular backups for the database and exported files
  
  Deploying on Platform-as-a-Service (Heroku, AWS Elastic Beanstalk)
  - Push code via Git
  - Configure environment variables in platform dashboard
  - Use managed database services or attach external DB
  - Configure build and start commands as required by platform

Login Information(Superuser):
Admin
- Username: NSCC
- Password: nscc123!
- Email: nscc@gmail.com

  Pictures of Features
1. Front page
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/e64c82e7-0336-4d60-99cb-df7934b04b1f" />

2. QR Scanner
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/5e8dec5e-9cb4-4bd7-91b2-2fbd151af318" />

3. Login Page
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/90311ae1-5fc2-475d-a1bc-f837fa4bcc41" />

4. Admin Dashboard
   
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/3dc5eb93-2c49-4d62-843d-67727a463e6d" />a

5. Users List
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/b481126d-e2b9-4d67-b0e6-87599dc846cc" />

6. Attendence List
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/7a401496-a76f-479b-b337-fb23561dd24a" />

7. Events List
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/94bc9e39-57d0-425e-9b7e-29c85e1ea6ac" />

8. Resgistration List
<img width="500" height="800" alt="Image" src="https://github.com/user-attachments/assets/d7aeedfd-db18-4158-ad9d-1bf0be965844" />


  
