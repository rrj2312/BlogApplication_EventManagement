

from events.models import Event, Registration, Attendance
from django.utils import timezone
from datetime import timedelta
import random

# Create sample events
events_data = [
    {
        'name': 'Tech Conference 2024',
        'description': 'Annual technology conference featuring latest trends in AI, ML, and Web Development',
        'location': 'Convention Center, Hall A',
        'date': timezone.now() + timedelta(days=7)
    },
    {
        'name': 'Workshop on Artificial Intelligence',
        'description': 'Hands-on workshop covering machine learning, deep learning, and AI applications',
        'location': 'University Campus, Room 101',
        'date': timezone.now() + timedelta(days=14)
    },
    {
        'name': 'Startup Networking Event',
        'description': 'Connect with entrepreneurs, investors, and fellow startup enthusiasts',
        'location': 'Business Park, Conference Room B',
        'date': timezone.now() + timedelta(days=21)
    },
    {
        'name': 'Digital Marketing Masterclass',
        'description': 'Learn the latest digital marketing strategies and tools',
        'location': 'Marketing Hub, Seminar Hall',
        'date': timezone.now() + timedelta(days=28)
    }
]

print("Creating sample events...")
for event_data in events_data:
    event, created = Event.objects.get_or_create(
        name=event_data['name'],
        defaults=event_data
    )
    if created:
        print(f"✓ Created event: {event.name}")
    else:
        print(f"- Event already exists: {event.name}")

# Create sample registrations
sample_participants = [
    {'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    {'name': 'Mike Johnson', 'email': 'mike.johnson@example.com'},
    {'name': 'Sarah Wilson', 'email': 'sarah.wilson@example.com'},
    {'name': 'David Brown', 'email': 'david.brown@example.com'},
    {'name': 'Emily Davis', 'email': 'emily.davis@example.com'},
    {'name': 'Chris Miller', 'email': 'chris.miller@example.com'},
    {'name': 'Lisa Anderson', 'email': 'lisa.anderson@example.com'},
    {'name': 'Tom Taylor', 'email': 'tom.taylor@example.com'},
    {'name': 'Anna Martinez', 'email': 'anna.martinez@example.com'},
    {'name':'Tim Buffer','email':'tim.buffer@example.com'},
]

print("\nCreating sample registrations...")
events = Event.objects.all()
registrations_created = []

for event in events:
    # Register 6-8 random participants for each event
    num_participants = random.randint(6, 8)
    selected_participants = random.sample(sample_participants, num_participants)
    
    for participant in selected_participants:
        registration, created = Registration.objects.get_or_create(
            event=event,
            email=participant['email'],
            defaults={'name': participant['name']}
        )
        if created:
            registrations_created.append(registration)
            print(f"✓ Registered {participant['name']} for {event.name}")

print(f"\nCreated {len(registrations_created)} registrations")

# Create sample attendance (mark 60-80% as attended)
print("\nCreating sample attendance records...")
attendance_count = 0

for registration in registrations_created:
    # 70% chance of attendance
    if random.random() < 0.7:
        attendance, created = Attendance.objects.get_or_create(
            registration=registration,
            defaults={
                'scanned_by': 'Sample Data Generator',
                'timestamp': timezone.now() - timedelta(
                    hours=random.randint(1, 48),
                    minutes=random.randint(0, 59)
                )
            }
        )
        if created:
            attendance_count += 1
            print(f"✓ Marked attendance for {registration.name}")

print(f"\nCreated {attendance_count} attendance records")

# Print summary
print("\n" + "="*50)
print("SAMPLE DATA CREATION SUMMARY")
print("="*50)

for event in Event.objects.all():
    total_reg = event.registrations.count()
    total_att = event.registrations.filter(attendance__isnull=False).count()
    rate = (total_att / total_reg * 100) if total_reg > 0 else 0
    
    print(f"\n{event.name}:")
    print(f"  Registrations: {total_reg}")
    print(f"  Attendance: {total_att}")
    print(f"  Attendance Rate: {rate:.1f}%")

print(f"\nTotal Events: {Event.objects.count()}")
print(f"Total Registrations: {Registration.objects.count()}")
print(f"Total Attendance: {Attendance.objects.count()}")
print("\nSample data created successfully!")
print("You can now test the system with this data.")
print("\nAccess URLs:")
print("- Home: http://localhost:8000/")
print("- Admin Dashboard: http://localhost:8000/admin/dashboard/")
print("- QR Scanner: http://localhost:8000/scanner/")
print("- Django Admin: http://localhost:8000/admin/")