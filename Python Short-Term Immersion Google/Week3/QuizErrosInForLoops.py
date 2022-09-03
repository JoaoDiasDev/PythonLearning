# Question
# validate_users function is used by the system to determine if a list of users is valid or invalid. A valid user is a user who is at least 3 characters in length. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. If you call it as in this example, something goes wrong. Do you know what to fix?
def is_valid(user):
    if len(user) >= 3:
        return True
    return False


def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users(["purplecat"])
