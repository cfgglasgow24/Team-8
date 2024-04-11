import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refugeeJobs.settings')
django.setup()

from jobSite.models import CustomUser, JobPost
from faker import Faker

fake = Faker()


def populate_users(num_users):
    for _ in range(num_users):
        user = CustomUser.objects.create(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
            bio=fake.text(),
            skills=" ".join(fake.words(nb=5)),
            language=fake.language_name(),
            education=fake.job(),
            experience=fake.text()
        )


def populate_job_posts(num_posts):
    # Define a set of common qualifications for better matching simulation
    common_qualifications = [
        "Bachelor's degree in Computer Science",
        "Master's degree in Business Administration",
        "Certified Public Accountant",
        "Project Management Professional certification",
        "Associate's degree in Graphic Design"
    ]

    for i in range(num_posts):
        # Select qualification based on a repeating pattern
        qualification = common_qualifications[i % len(common_qualifications)]

        job_post = JobPost.objects.create(
            title=fake.job(),
            description=fake.text(),
            company=fake.company(),
            location=fake.city(),
            requirements="Part-Time" if i % 2 == 0 else "Full-Time",  # Alternate requirements
            salary=fake.random_number(digits=5),
            qualifications=qualification  # Use predefined qualifications
        )


if __name__ == '__main__':
    num_users = 10  # Number of users to create
    num_posts = 20  # Number of job posts to create

    populate_users(num_users)
    populate_job_posts(num_posts)

    print("Data population complete!")
