# 👥 Employee Attendance System

Command-line attendance management system for tracking employee check-in/out, daily status (P/A/L), monthly reports, and attendance percentage. Data persists in `attendance.json`. Ideal for engineering students practicing file I/O, date handling, and data structures. [web:40][web:46]

## ✨ Features
- **Employee management**: Add/view employees with ID, name, department
- **Daily attendance**: Mark Present(A)/Absent(P)/Leave(L) for any date
- **Check-in/out timestamps**: Track work hours
- **Monthly reports**: Attendance summary with percentage
- **Data persistence**: JSON storage with backup
- **Search & filter**: By employee ID, date range, department

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Storage**: JSON file handling
- **Date Handling**: `datetime` module
- **Data Structures**: Lists, Dictionaries

## 📊 Sample Reports
Employee: John Doe (ID: EMP001) - Jan 2025
Present: 18 days | Absent: 5 days | Leave: 3 days
Attendance %: 85.71%
Total Hours: 152.5 hrs


## 💻 Sample Data Structure
employees = {
"EMP001": {"name": "John Doe", "dept": "IT"},
"EMP002": {"name": "Jane Smith", "dept": "HR"}
}
attendance = {
"2025-01-15": {
"EMP001": {"status": "P", "checkin": "09:30", "checkout": "18:15"}
}


## 🎓 Learning Outcomes
- JSON file operations (read/write/update)
- Date parsing and manipulation
- Nested data structures (dict of dicts)
- Search algorithms and filtering
- Formatted table output
- Error handling for invalid dates/IDs

## 📈 Key Functions
| Function | Purpose |
|----------|---------|
| `add_employee()` | Register new employee |
| `mark_attendance()` | Record daily status + timestamps |
| `monthly_report()` | Generate attendance statistics |
| `search_employee()` | Find by ID/name/department |
| `backup_data()` | JSON persistence |

## 🤝 Contributing
1. Fork the repository
2. Create feature branch: `git checkout -b feature/add-biometric`
3. Commit changes: `git commit -m 'Add biometric attendance'`
4. Push: `git push origin feature/add-biometric`
5. Open Pull Request

## 📄 License
MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments
- Built for LPU Engineering portfolio
- Standard attendance management practices [web:40]
- JSON-based persistence for student projects

}
