# Scenario 01
# You are building course listing page. Store course names in a list and display them.
courses = []

while(True):
    course = input("Enter course: ")
    courses.append(course)
    if course == "":
        break

for course in courses:
    print(course)

# Scenario 02
# Store fixed admin roles in tuple and check whether a user role has admin access.
admin_roles = ("Owner", "Editor")
users = {"Babbli":"Viewer", "Bhavan":"Owner", "Babita":"Editor"} # {username : role}

for user in users:
    if users.get(user) in admin_roles:
        print(f"USER: {user} | ADMIN_ACCESS: allowed")
    else:
        print(f"USER: {user} | ADMIN_ACCESS: denied")