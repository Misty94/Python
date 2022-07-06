# List of dictionaries
users = [
    {"first": "Harry", "last": "Potter"}, # index 0
    {"first": "Hermione", "last": "Granger"}, # index 1
    {"first": "Ron", "last": "Weasley"}, # index 2
]

print(users[0]["last"])


# Dictionary containing lists
resume_data = {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies": ["rock climbing", "knitting"]
}

print(resume_data["skills"][1])
print(users[2]["first"])


# Print the first listed language of the 2nd resume

resumes = [

    {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies": ["rock climbing", "knitting"]
    },
    {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies": ["rock climbing", "knitting"]
    },
    {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies": ["rock climbing", "knitting"]
    },

]

# resumes[index number]
# resumes[1][string]
# resumes[1][string][index number]
print(resumes[1]["languages"][0])
