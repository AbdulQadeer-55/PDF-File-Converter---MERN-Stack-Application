# PDF File Converter - MERN Stack Application

A modern web application for converting PDF files with user authentication, subscription plans, and a beautiful UI/UX.

## 🚀 Features

- **PDF File Processing**: Upload and convert PDF files
- **User Authentication**: Complete auth system with email verification
- **Subscription Plans**: Free and premium plans with different features
- **Beautiful UI/UX**: Modern interface with Tailwind CSS
- **Drag & Drop**: Intuitive file upload interface
- **Secure**: JWT authentication and file validation
- **Responsive**: Works on all devices

## 🛠️ Tech Stack

- **Frontend**: React, Tailwind CSS, Context API
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Authentication**: JWT, bcrypt
- **File Processing**: pdf-lib
- **Email**: Nodemailer
- **Storage**: Local storage with option for AWS S3

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-file-converter.git
cd pdf-file-converter
```

2. Install dependencies:
```bash
# Install root dependencies
npm install

# Install client dependencies
cd client
npm install

# Install server dependencies
cd ../server
npm install
```

3. Set up environment variables:
```bash
# In server directory, create .env file
cp .env.example .env

# In client directory, create .env file
cp .env.example .env
```

4. Start the development servers:
```bash
# Start backend server (from server directory)
npm run dev

# Start frontend server (from client directory)
npm run dev
```

## 🔐 Environment Variables

### Backend (.env)
```
NODE_ENV=development
PORT=5000
MONGODB_URI=your_mongodb_uri
JWT_SECRET=your_jwt_secret
EMAIL_USER=your_email
EMAIL_PASS=your_email_password
FRONTEND_URL=http://localhost:3000
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:5000
```

## 🗂️ Project Structure

[Project tree structure here - abbreviated for README]

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.