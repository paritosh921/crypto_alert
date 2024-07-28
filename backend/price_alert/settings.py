INSTALLED_APPS = [
    
    'rest_framework',
    'alerts',
]

# Email configuration (replace with your credentials)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'manavjiji123@gmail.com'
EMAIL_HOST_PASSWORD = 'Vedujiji@4321'  # Use environment variables in production