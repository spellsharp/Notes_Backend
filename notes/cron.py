from django.utils import timezone
import ezgmail
from .models import Notes
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

def send_reminder_emails() -> int:
    print('Sending reminder emails...')
    deadline_threshold = timezone.now() - timedelta(days=1)
    notes_to_remind = Notes.objects.filter(deadline__gte=deadline_threshold)
    users_to_remind = User.objects.filter(notes__in=notes_to_remind)

    for user in users_to_remind:
        notes = Notes.objects.filter(author=user, deadline__gte=deadline_threshold)
        for note in notes:
            subject = 'Reminder: Deadline approaching'
            message = f"Reminder: The deadline for the note '{note.title}' is approaching. Please take necessary actions."
            print(f"Sent reminder email to {user.email}")   
            print(f"Subject: {subject}")
            print(f"Body: {message}")     
            # send_reminder(subject, message, recipient=note.recipient_email)        
    return len(notes_to_remind)

def send_reminder(subject, message, recipient='svcodin22@gmail.com'):
    ezgmail.send(recipient, subject, message)