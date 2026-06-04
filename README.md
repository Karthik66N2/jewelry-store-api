# 💎 Jewelry Store Backend API

A production-ready REST API for an online jewelry store built with **Django** and **Django REST Framework**.
Features JWT authentication, advanced filtering, pagination, and admin-protected routes.

---

## 📁 Project Structure

```
jewelry_store_api/
│
├── core/                          # Django project configuration
│   ├── __init__.py
│   ├── settings.py                # All settings (JWT, DRF, DB, etc.)
│   ├── urls.py                    # Root URL configuration
│   └── wsgi.py                    # WSGI server entry point
│
├── products/                      # Products & Categories app
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py       # Command to populate sample data
│   ├── __init__.py
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py
│   ├── filters.py                 # django-filter configuration
│   ├── models.py                  # Category & Product models
│   ├── pagination.py              # Custom pagination class
│   ├── permissions.py             # IsAdminOrReadOnly permission
│   ├── serializers.py             # DRF serializers
│   ├── urls.py                    # Router URL configuration
│   └── views.py                   # ViewSets & business logic
│
├── accounts/                      # User authentication app
│   ├── __init__.py
│   ├── apps.py
│   ├── serializers.py             # Register & profile serializers
│   ├── urls.py
│   └── views.py                   # Register, login, profile views
│
├── .env.example                   # Environment variables template
├── .gitignore
├── manage.py                      # Django management utility
├── Procfile                       # For Render/Railway deployment
├── render.yaml                    # Render.com deployment config
└── requirements.txt               # Python dependencies
```

---

## ⚙️ Setup Instructions

### Step 1 — Prerequisites

Make sure you have Python 3.10+ installed:
```bash
python --version
```

### Step 2 — Clone & Create Virtual Environment

```bash
# Clone the repo
git clone https://github.com/yourusername/jewelry-store-api.git
cd jewelry-store-api

# Create virtual environment
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment

```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your values (the defaults work for local development)
```

### Step 5 — Run Migrations

```bash
# Create database tables from models
python manage.py makemigrations
python manage.py migrate
```

### Step 6 — Create Admin User

```bash
# This creates a superuser (is_staff=True, is_superuser=True)
python manage.py createsuperuser
# Follow the prompts for username, email, password
```

### Step 7 — Load Sample Data

```bash
# Populate the database with sample categories and products
python manage.py seed_data

# To clear and re-seed:
python manage.py seed_data --clear
```

### Step 8 — Run the Server

```bash
python manage.py runserver
```

The API is now running at: `http://127.0.0.1:8000/`
Django Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🔑 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.

### Register a new user

```
POST /api/auth/register/
```

### Login (get tokens)

```
POST /api/auth/login/
```

### Use the token

Add this header to protected requests:
```
Authorization: Bearer <your_access_token>
```

### Refresh an expired token

```
POST /api/auth/token/refresh/
Body: { "refresh": "<your_refresh_token>" }
```

---

## 📡 API Endpoints

### 🏷️ Categories

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/api/categories/` | No | List all categories |
| POST | `/api/categories/` | Admin | Create a category |
| GET | `/api/categories/<id>/` | No | Get single category |
| PUT | `/api/categories/<id>/` | Admin | Update a category |
| DELETE | `/api/categories/<id>/` | Admin | Delete a category |
| GET | `/api/categories/<id>/products/` | No | Products in a category |

### 💎 Products

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/api/products/` | No | List products (with filters) |
| POST | `/api/products/` | Admin | Create a product |
| GET | `/api/products/<id>/` | No | Get single product |
| PUT | `/api/products/<id>/` | Admin | Update a product |
| DELETE | `/api/products/<id>/` | Admin | Delete a product |

### 👤 Auth

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/auth/register/` | No | Register new user |
| POST | `/api/auth/login/` | No | Login, get JWT tokens |
| GET | `/api/auth/profile/` | Yes | View own profile |
| PUT | `/api/auth/profile/` | Yes | Update own profile |
| POST | `/api/auth/token/refresh/` | No | Refresh access token |

---

## 🔍 Filtering & Sorting

### Filter by price range

```
GET /api/products/?min_price=100&max_price=1000
```

### Filter by metal

```
GET /api/products/?metal=gold
GET /api/products/?metal=silver
GET /api/products/?metal=platinum
```

### Filter by category

```
GET /api/products/?category=1
GET /api/products/?category_name=rings
```

### Filter by rating

```
GET /api/products/?min_rating=4.5
```

### Sorting options

```
GET /api/products/?sort=latest      # Newest first (default)
GET /api/products/?sort=price_low   # Cheapest first
GET /api/products/?sort=price_high  # Most expensive first
GET /api/products/?sort=popularity  # Highest rated first
```

### Combine filters

```
GET /api/products/?min_price=500&max_price=2000&metal=gold&sort=price_low
```

### Search

```
GET /api/products/?search=diamond
```

### Pagination

```
GET /api/products/?page=2&page_size=5
```

---

## 📋 Sample JSON Requests & Responses

### Register User

**Request:**
```json
POST /api/auth/register/
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response (201):**
```json
{
  "message": "Account created successfully. Please log in.",
  "user": {
    "id": 2,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_staff": false,
    "date_joined": "2024-01-15T10:30:00Z"
  }
}
```

### Login

**Request:**
```json
POST /api/auth/login/
{
  "username": "johndoe",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 2,
    "username": "johndoe",
    "email": "john@example.com",
    "is_staff": false,
    "full_name": "John Doe"
  }
}
```

### Create Category (Admin)

**Request:**
```json
POST /api/categories/
Authorization: Bearer <admin_token>
{
  "name": "Rings",
  "image_url": "https://example.com/rings.jpg"
}
```

**Response (201):**
```json
{
  "id": 1,
  "name": "Rings",
  "image_url": "https://example.com/rings.jpg",
  "product_count": 0
}
```

### Create Product (Admin)

**Request:**
```json
POST /api/products/
Authorization: Bearer <admin_token>
{
  "name": "Diamond Solitaire Ring",
  "description": "Classic single diamond ring set in 18K gold.",
  "category": 1,
  "price": "2499.99",
  "discount": "10.00",
  "base_metal": "gold",
  "polish": "polished",
  "rating": "4.8",
  "image_url": "https://example.com/diamond-ring.jpg"
}
```

**Response (201):**
```json
{
  "message": "Product created successfully.",
  "product": {
    "id": 1,
    "name": "Diamond Solitaire Ring",
    "description": "Classic single diamond ring set in 18K gold.",
    "category": 1,
    "category_name": "Rings",
    "price": "2499.99",
    "discount": "10.00",
    "discounted_price": 2249.99,
    "base_metal": "gold",
    "base_metal_display": "Gold",
    "polish": "polished",
    "polish_display": "Polished",
    "rating": "4.8",
    "image_url": "https://example.com/diamond-ring.jpg",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

### List Products

**Response (200):**
```json
{
  "pagination": {
    "total_items": 14,
    "total_pages": 2,
    "current_page": 1,
    "page_size": 10,
    "next": "http://localhost:8000/api/products/?page=2",
    "previous": null
  },
  "results": [
    {
      "id": 1,
      "name": "Diamond Solitaire Ring",
      "category_name": "Rings",
      "price": "2499.99",
      "discount": "10.00",
      "discounted_price": 2249.99,
      "base_metal": "gold",
      "rating": "4.8",
      "image_url": "https://example.com/diamond-ring.jpg",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

### Validation Error Response (400)

```json
{
  "price": ["Price must be greater than 0."],
  "discount": ["Discount must be between 0 and 100."]
}
```

### Unauthorized Response (401)

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Forbidden Response (403)

```json
{
  "detail": "You must be an admin to perform this action."
}
```

---

## 🧪 Postman Testing Guide

### 1. Import the Collection

Create a new Postman collection called "Jewelry Store API".

### 2. Set Environment Variables

In Postman → Environments → New:
- `base_url`: `http://127.0.0.1:8000`
- `access_token`: (fill after login)
- `refresh_token`: (fill after login)

### 3. Test Sequence

**Step 1: Register**
- Method: POST
- URL: `{{base_url}}/api/auth/register/`
- Body (JSON): `{ "username": "admin", "email": "admin@example.com", "password": "Admin123!", "password2": "Admin123!" }`

**Step 2: Make yourself admin**
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username='admin')
>>> u.is_staff = True
>>> u.save()
```

**Step 3: Login**
- Method: POST
- URL: `{{base_url}}/api/auth/login/`
- Body: `{ "username": "admin", "password": "Admin123!" }`
- Copy `access` token → set as `access_token` env variable

**Step 4: Create Category**
- Method: POST
- URL: `{{base_url}}/api/categories/`
- Headers: `Authorization: Bearer {{access_token}}`
- Body: `{ "name": "Rings", "image_url": "https://example.com/rings.jpg" }`

**Step 5: Create Product**
- Method: POST
- URL: `{{base_url}}/api/products/`
- Headers: `Authorization: Bearer {{access_token}}`
- Body: (see sample above)

**Step 6: Test Filters**
- GET `{{base_url}}/api/products/?metal=gold`
- GET `{{base_url}}/api/products/?min_price=100&max_price=500`
- GET `{{base_url}}/api/products/?sort=price_low`

---

## 🚀 Deployment Guide

### Option A: Deploy to Render.com (Free Tier)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/jewelry-store-api.git
   git push -u origin main
   ```

2. **Create Render account** at [render.com](https://render.com)

3. **New Web Service** → Connect GitHub repo

4. **Configure:**
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - Start Command: `gunicorn core.wsgi:application`
   - Environment: Python 3

5. **Add Environment Variables** in Render dashboard:
   - `SECRET_KEY` → generate a random key
   - `DEBUG` → `False`
   - `ALLOWED_HOSTS` → `.onrender.com`

6. **Deploy!** — Render will build and deploy automatically.

### Option B: Deploy to Railway.app

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and deploy:**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Set environment variables:**
   ```bash
   railway variables set SECRET_KEY=your-secret-key
   railway variables set DEBUG=False
   ```

---

## 🔧 Available Metal Options

| Value | Display |
|-------|---------|
| `gold` | Gold |
| `silver` | Silver |
| `platinum` | Platinum |
| `rose_gold` | Rose Gold |
| `white_gold` | White Gold |
| `copper` | Copper |
| `brass` | Brass |
| `stainless_steel` | Stainless Steel |

## ✨ Polish Options

| Value | Display |
|-------|---------|
| `glossy` | Glossy |
| `matte` | Matte |
| `antique` | Antique |
| `brushed` | Brushed |
| `hammered` | Hammered |
| `polished` | Polished |

---

## 🌟 Resume/Interview Improvements

Ideas to level up this project:

1. **Add image upload** — Use Cloudinary or AWS S3 to store product images
2. **Add reviews/ratings** — Let users submit reviews, auto-calculate product rating
3. **Add inventory tracking** — `stock_quantity` field, low-stock alerts
4. **Add wishlist** — Authenticated users can save favorite products
5. **Add order system** — Cart → Order → Order Items flow
6. **Add Celery** — Background tasks (send order confirmation emails)
7. **Add Redis caching** — Cache popular product lists for performance
8. **Add API versioning** — `/api/v1/products/` for backward compatibility
9. **Add pytest tests** — Unit tests for models, serializers, views
10. **Add Swagger docs** — `drf-spectacular` for auto-generated API docs
11. **Switch to PostgreSQL** — More production-ready than SQLite
12. **Add Docker** — `Dockerfile` + `docker-compose.yml` for containerization
13. **Add GitHub Actions CI** — Auto-run tests on every push

---

## 📦 Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Language |
| Django | 4.2.7 | Web framework |
| Django REST Framework | 3.14.0 | REST API |
| SimpleJWT | 5.3.0 | JWT Authentication |
| django-filter | 23.3 | Query filtering |
| Gunicorn | 21.2.0 | Production WSGI server |
| WhiteNoise | 6.6.0 | Static files serving |
| SQLite | built-in | Development database |

---

## 👨‍💻 Author

Built with ❤️ using Django REST Framework.
