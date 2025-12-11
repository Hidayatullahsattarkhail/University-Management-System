# 🎓 University Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A comprehensive web-based university management system for managing students, exams, fees, and transport services. Built with Python and Flask, featuring a modern dark-themed interface and implementing fundamental Data Structures & Algorithms concepts.

## ✨ Features

### 📚 Student Management
- **Add Students**: Register new students with ID, name, email, phone, and department
- **View All Students**: Display complete student records in an organized table
- **Search Students**: Find students by ID or name using linear search
- **Update Records**: Modify existing student information
- **Delete Students**: Remove student records from the system
- **Sort Students**: Organize by ID or name using bubble sort algorithm

### 📝 Exam Management
- **Record Exam Results**: Store student exam marks and automatically calculate grades
- **View Exam Records**: Display all exam results with grades
- **Search by Student**: Find exam records for specific students
- **Grade Calculation**: Automatic grade assignment based on marks (A+, A, B, C, D, F)
- **Sort Results**: Organize by student name or marks using bubble/selection sort

### 💰 Fee Management
- **Fee Registration**: Record student fee payments
- **Payment Tracking**: Monitor paid and pending fees
- **Search Payments**: Find fee records by student ID
- **Fee Reports**: View complete payment history

### 🚌 Transport Management
- **Transport Registration**: Register students for transport services
- **Route Assignment**: Assign students to specific routes
- **Request Queue**: FIFO queue system for pending transport requests
- **Approve/Reject**: Process transport requests from the queue
- **View Registrations**: Display all active transport registrations

## 🛠️ Technology Stack

- **Backend**: Python 3.8+
- **Web Framework**: Flask
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Data Storage**: CSV files
- **Design**: Custom Black & Red dark theme

## 📊 Data Structures & Algorithms

This project demonstrates practical implementation of fundamental DSA concepts:

### Data Structures
- **Singly Linked List**: Used for student and transport management (dynamic size, O(1) insertion)
- **Dynamic Array**: Used for exam records (fast access, cache-friendly)
- **Queue (FIFO)**: Used for transport request processing (fairness in order)

### Algorithms
- **Bubble Sort**: Sorting students by ID/name, exams by name (O(n²))
- **Selection Sort**: Sorting exams by marks (O(n²))
- **Linear Search**: Finding records by ID or name (O(n))

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hidayatullahsattarkhail/University-Management-System.git
   cd University-Management-System
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📖 Usage

### Dashboard
The home page provides quick access to all modules:
- Student Management
- Exam Management
- Fee Management
- Transport Management

### Adding a Student
1. Navigate to "Student Management"
2. Click "Add New Student"
3. Fill in the form (ID, Name, Email, Phone, Department)
4. Click "Submit"

### Recording Exam Results
1. Navigate to "Exam Management"
2. Click "Add Exam Result"
3. Enter Student Name, Subject, and Marks
4. Grade is automatically calculated
5. Click "Submit"

### Managing Transport
1. Navigate to "Transport Management"
2. View pending requests in the queue
3. Approve or reject requests
4. View all active registrations

## 📁 Project Structure

```
University-Management-System/
├── app.py                  # Flask application & routes
├── student.py              # Student management (Linked List)
├── exam.py                 # Exam management (Dynamic Array)
├── fee.py                  # Fee management
├── transport.py            # Transport management (Linked List + Queue)
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Dashboard
│   ├── students.html      # Student management page
│   ├── exams.html         # Exam management page
│   ├── fees.html          # Fee management page
│   └── transport.html     # Transport management page
├── static/
│   └── css/
│       └── style.css      # Custom dark theme
├── students.csv           # Student data storage
├── exams.csv              # Exam data storage
├── fees.csv               # Fee data storage
├── transport.csv          # Transport data storage
└── transport_queue.csv    # Pending transport requests
```

## 🎨 Screenshots

*Coming soon - Screenshots of the dashboard, student management, and other modules*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Hidayatullah Sattarkhail**
- GitHub: [@Hidayatullahsattarkhail](https://github.com/Hidayatullahsattarkhail)
- Email: hidayatullahsattarkhail@gmail.com

## 🙏 Acknowledgments

- Originally conceived as a C++ console application
- Ported to Python with modern web interface
- Built as a practical demonstration of DSA concepts
- Designed for educational purposes and university administration

## 🔮 Future Enhancements

- [ ] Database integration (PostgreSQL/MySQL)
- [ ] User authentication and authorization
- [ ] Advanced reporting and analytics
- [ ] Email notifications
- [ ] Mobile responsive design improvements
- [ ] Export data to PDF/Excel
- [ ] Real-time updates using WebSockets
- [ ] RESTful API for mobile app integration

## 📞 Support

If you have any questions or need help, please open an issue in the GitHub repository.

---

⭐ **Star this repository if you find it helpful!**
