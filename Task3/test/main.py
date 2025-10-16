import faker
import json

generator = faker.Faker()

def get_fake_user():
    user = {
        "name": generator.name(),
        "address": generator.address(),
        "email": generator.email(),
        "phne_number": generator.phone_number(),
    }
    return user

filename = "fake_users.json"

users = []

for i in range(10):
    user = get_fake_user()
    users.append(user)

with open(filename, "w") as file:
    json.dump(users, file, indent=4)
  
       

print(users)
print(f"Total users generated: {len(users)}")