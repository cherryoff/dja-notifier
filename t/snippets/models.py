from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

class Tag(models.Model):
    label = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.label

class Recipient(models.Model):
    class RecipientType(models.TextChoices):
        EMAIL = 'email'
        TELEGRAM = 'Telegram'

    type = models.CharField(max_length=100, choices=RecipientType.choices, default=RecipientType.EMAIL)
    settings = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} recipient"

class NotificationTemplate(models.Model):
    template = models.TextField()
    subject = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Check(models.Model):
    class CheckType(models.TextChoices):
        PING = 'ping'
        CONTENT = 'content'

    type = models.CharField(max_length=100, choices=CheckType.choices, default=CheckType.PING)
    url = models.URLField()
    template = models.ForeignKey(NotificationTemplate, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient, through='NotificationEvent')
    frequency = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.type} check for {self.url}"

class NotificationEvent(models.Model):
    related_check = models.ForeignKey(Check, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    notification_sent_at = models.DateTimeField()  # Timestamp of the notification
    status = models.CharField(max_length=20, choices=[('sent', 'Sent'), ('failed', 'Failed')])

    class Meta:
        unique_together = ('related_check', 'recipient', 'notification_sent_at')

    def __str__(self):
        return f"Notification for {self.recipient} on {self.related_check} at {self.notification_sent_at}"
