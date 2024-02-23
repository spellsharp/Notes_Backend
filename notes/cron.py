
from django.utils import timezone
import ezgmail
from notes.models import Notes
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import sys

CREDENTIALS_PATH="backend/credentials.json"
TOKEN_PATH="backend/token.json"

def send_reminder_emails() -> int:
    print('Sending reminder emails...')
    notes_to_remind = Notes.objects.filter(deadline__range=(timezone.now() - timedelta(days=1), timezone.now() + timedelta(days=1)))
    users_to_remind = User.objects.filter(notes__in=notes_to_remind)
    for user in users_to_remind:
        notes = Notes.objects.filter(author=user, deadline__range=(timezone.now() - timedelta(days=1), timezone.now() + timedelta(days=1)))
        for note in notes:
            print(note.title)
            subject = 'Deadline approaching'
            message = f"Reminder: \nThe deadline for the note '{note.title}' is approaching.\nPlease take necessary actions."
            print(f"Recipient: {user.email}")
            print(f"Subject: {subject}")
            print(f"Body: {message}")
            try:
                ezgmail.send(user.email, subject, message)
            except Exception as e:
                print(e)
            print("Email send?")
    return len(notes_to_remind)