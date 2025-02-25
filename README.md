# AI Prompt Model - Setup Guide

## 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## 2️⃣ **Set Up Django Backend**

### **Create and Activate Virtual Environment**
```sh
python -m venv env
```
- **Windows:**
  ```sh
  env\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source env/bin/activate
  ```

### **Install Dependencies**
```sh
pip install django djangorestframework django-cors-headers requests python-dotenv
```

### **Create Django Project & App**
```sh
django-admin startproject backend
cd backend
django-admin startapp api
```

### **Apply Migrations & Run Server**
```sh
python manage.py migrate
python manage.py runserver
```

---

## 3️⃣ **Set Up React+Vite Frontend**

### **Navigate to Project Directory & Install Vite**
```sh
cd ..
npm create vite@latest frontend --template react
cd frontend
```

### **Install Dependencies**
```sh
npm install axios
```

### **Start React Development Server**
```sh
npm run dev
```

---

## 4️⃣ **Run the Full Stack Application**
### **Start Django Backend**
```sh
cd backend
python manage.py runserver
```

### **Start React Frontend**
```sh
cd frontend
npm run dev
```

---

## 5️⃣ **Git Commands for Version Control**

### **Initialize Git (if not already done)**
```sh
git init
git add .
git commit -m "Initial commit"
```

### **Push to GitHub**
```sh
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

### **Updating Changes**
```sh
git add .
git commit -m "Updated features"
git push origin main
```

---

## 6️⃣ **Deploying the Application**

### **Deploy Django Backend (Optional: on Render/Heroku)**
```sh
git push heroku main
```

### **Deploy React Frontend (Netlify/Vercel)**
```sh
npm run build
```

Now your AI Prompt Model is fully set up! 🚀
