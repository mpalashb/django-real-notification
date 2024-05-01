# Real-Time Django Notifications with Channels

This Django application enables real-time notifications to users through Django Channels, offering an instant notification experience without page refreshes. It leverages Django 5 and Channels 3.0.5.

**Features:**

- **WebSocket Support:** Employs Django Channels to manage WebSocket connections for seamless server-client communication in real time.
- **Channels Layers:** Implements a communication channel for transmitting and receiving notifications across various application components.
- **Django Signals Integration:** Utilizes Django's signals framework to trigger notifications based on specific application events (e.g., new messages, mentions).
- **Frontend Integration:** Integrates JavaScript to handle WebSocket events and update the UI in real time, ensuring smooth notification delivery.

**Usage:**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mpalashb/django-real-notification.git
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Start Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at http://127.0.0.1:8000 to begin receiving real-time notifications.