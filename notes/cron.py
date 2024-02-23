from django.utils import timezone
import ezgmail
from .models import Notes

def send_reminder_emails() -> int:
    print('Sending reminder emails...')
    deadline_threshold = timezone.now() + timezone.timedelta(days=1)
    notes_to_remind = Notes.objects.filter(deadline=deadline_threshold)
    for note in notes_to_remind:
        subject = 'Reminder: Deadline approaching'
        message = f"Reminder: The deadline for '{note.title}' is approaching. Please take necessary actions."
        print(f"Sent reminder email to {note.recipient_email}")
        send_reminder(subject, message, recipient=note.recipient_email)        
    return len(notes_to_remind)

def send_reminder(subject, message, recipient='svcodin22@gmail.com'):
    ezgmail.send(recipient, subject, message)