
# Django WebSocket Notification System

This is a minimal Django project that allows an admin to send real-time notifications to specific users using WebSockets via Django Channels.

## Features

- Admin page to send notifications to a specific user.
- Each user has a dedicated notification page.
- Real-time notification delivery using WebSockets and Django Channels.
- No external CSS — simple HTML for clarity and focus.

## Requirements

- Python 3.8+
- Django 4.x or 5.x
- Django Channels

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-websocket-notify.git
   cd django-websocket-notify

## 🌐 How to Access URLs in Browser

### 1. Admin Notification Form
http://127.0.0.1:8000/notify/

- Go to this URL to send a message from admin to a specific user.

### 2. User Notification Page
http://127.0.0.1:8000/<username>/

- Replace `<username>` with the actual username.
- Example: http://127.0.0.1:8000/suresh/



