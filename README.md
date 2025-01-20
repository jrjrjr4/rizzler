# Rizz Approval Scanner

A web application that classifies images based on whether they contain a cat or a hotdog, returning 'Rizz Approved' or 'Not Rizz Approved'.

## Tech Stack

### Frontend
- React
- Material-UI
- React Dropzone
- Axios

### Backend
- FastAPI
- Python
- YOLOv5 (for image classification)
- Pillow

## Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source env/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the backend server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The application will be available at http://localhost:3000

## Development

### Project Structure
```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── models/
│   └── requirements.txt
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/
    │   └── App.js
    └── package.json
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License. 