# DRF Pagination & Throttling

A Django REST Framework (DRF) project demonstrating how to implement **API pagination** and **request throttling** — two essential patterns for building scalable, production-ready REST APIs.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
- [Pagination](#pagination)
  - [PageNumberPagination](#pagenumberpagination)
  - [LimitOffsetPagination](#limitoffsetpagination)
  - [CursorPagination](#cursorpagination)
- [Throttling](#throttling)
  - [AnonRateThrottle](#anonratethrottle)
  - [UserRateThrottle](#userratethrottle)
  - [ScopedRateThrottle](#scopedratethrottle)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Author](#author)

---

## About

This project serves as a hands-on reference for implementing **pagination** and **throttling** in Django REST Framework. It covers:

- Multiple pagination strategies (page number, limit-offset, cursor-based)
- Rate limiting for both anonymous and authenticated users
- Per-view and global throttle configurations

---

## Features

- ✅ Page Number Pagination
- ✅ Limit-Offset Pagination
- ✅ Cursor-based Pagination
- ✅ Anonymous user rate limiting
- ✅ Authenticated user rate limiting
- ✅ Scoped throttling per endpoint
- ✅ SQLite database for quick local setup

---

## Tech Stack

| Technology | Version |
|---|---|
| Python | 3.10+ |
| Django | 4.x |
| Django REST Framework | 3.x |
| Database | SQLite (default) |

---

## Project Structure

```
DRF-Pagination-and-throttling/
│
├── drf/                    # Project configuration (settings, urls, wsgi)
│   ├── settings.py         # DRF pagination & throttling config
│   ├── urls.py
│   └── wsgi.py
│
├── home/                   # Core app with models, views, serializers
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── db.sqlite3              # SQLite database
├── manage.py
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Prajapati-vijay/DRF-Pagination-and-throttling.git
cd DRF-Pagination-and-throttling
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install django djangorestframework
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser** *(optional — for testing authenticated throttle limits)*

```bash
python manage.py createsuperuser
```

### Running the Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## Pagination

Configured globally in `drf/settings.py` under the `REST_FRAMEWORK` dict, or overridden per view using `pagination_class`.

### PageNumberPagination

Splits results into numbered pages. Use the `?page=` query parameter.

```
GET /api/items/?page=2
```

**Sample Response:**
```json
{
  "count": 100,
  "next": "http://127.0.0.1:8000/api/items/?page=3",
  "previous": "http://127.0.0.1:8000/api/items/?page=1",
  "results": [ ... ]
}
```

### LimitOffsetPagination

Returns a slice of results based on `limit` and `offset`.

```
GET /api/items/?limit=10&offset=20
```

### CursorPagination

Cursor-based pagination for stable, real-time data feeds. Uses an opaque cursor token rather than page numbers.

```
GET /api/items/?cursor=cD0yMDIz...
```

---

## Throttling

Controls the rate of requests clients can make to the API.

### AnonRateThrottle

Limits unauthenticated (anonymous) requests. Keyed by the incoming IP address.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
    }
}
```

### UserRateThrottle

Limits authenticated user requests. Keyed by the user's ID.

```python
'DEFAULT_THROTTLE_RATES': {
    'user': '100/day',
}
```

### ScopedRateThrottle

Applies different rate limits to specific views using a `throttle_scope`.

```python
# views.py
class MyView(APIView):
    throttle_scope = 'uploads'

# settings.py
'DEFAULT_THROTTLE_RATES': {
    'uploads': '5/hour',
}
```

When a limit is exceeded, the API responds with:

```
HTTP 429 Too Many Requests
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/items/` | List all items (paginated) |
| POST | `/api/items/` | Create a new item |
| GET | `/api/items/<id>/` | Retrieve a specific item |
| PUT | `/api/items/<id>/` | Update a specific item |
| DELETE | `/api/items/<id>/` | Delete a specific item |

> **Note:** Endpoints may vary — check `home/urls.py` for the exact routes registered in this project.

---

## Configuration

All DRF settings live in `drf/settings.py`. Example configuration:

```python
REST_FRAMEWORK = {
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    # Throttling
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '100/day',
    }
}
```

---

## Author

**Vijay Prajapati**  
Senior Software Engineer | Full-Stack Developer  
📧 vijayprajapati260263@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/vijay-prajapati-60a3b5247) | [GitHub](https://github.com/Prajapati-vijay)
