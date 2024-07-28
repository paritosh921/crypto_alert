from rest_framework import generics, permissions
from .models import Alert
from .serializers import AlertSerializer
from django.core.mail import send_mail

class AlertCreateAPIView(generics.CreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        alert = serializer.save(user=self.request.user)
        self.send_alert_email(alert)

    def send_alert_email(self, alert):
        send_mail(
            'Price Alert Created',
            f'You have created an alert for {alert.coin} at ${alert.target_price}.',
            'your_email@gmail.com',
            [alert.user.email],
            fail_silently=False,
        )

class AlertListAPIView(generics.ListAPIView):
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)

class AlertDeleteAPIView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    permission_classes = [permissions.IsAuthenticated]