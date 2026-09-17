# ---------------- imports ----------------
import hashlib # library to save the password as hashed format
import getpass # to hide password input

# --------------------------------
def get_list_input(message):
    """
    Get comma-separated values from the user
    and convert them into a list.

    """

    while True:

        user_input = input(message).strip()

        if user_input:

            items = user_input.split(",")

            return [
                item.strip().lower()
                for item in items
                if item.strip()
            ]

        print(
            "Please enter at least one value."
        )


def hash_password(password):
    """
    Hash the password before storing it.

    """

    return hashlib.sha256( 
        password.encode()
    ).hexdigest() # store the password in json in sha256 format 


def create_candidate():
    """
    Collect the user's career information.

    """

    print("\n" + "=" * 40)
    print("CREATE YOUR PROFILE")
    print("=" * 40)

    # Get user's name
    name = input("Name: ").strip()

    while not name:

        print("Name cannot be empty.")

        name = input(
            "Name: "
        ).strip()

    # Get user's major
    major = input(
        "Major: "
    ).strip()

    # Get user's career_stage
    career_stage = input(
        "Career Stage: "
    ).strip()

    # Get user's skills
    skills = get_list_input(
        "Skills (separated by commas): "
    )

    # Get user's interests
    interests = get_list_input(
        "Interests (separated by commas): "
    )

    # Store the profile information in dictionary
    candidate = {
        "name": name,
        "major": major,
        "career_stage": career_stage,
        "skills": skills,
        "interests": interests
    }

    return candidate


def register_candidate(candidates):
    """
    Create a new user account.

    """

    print("\n" + "=" * 40)
    print("CREATE ACCOUNT")
    print("=" * 40)

    # --------------------------------------------------
    # Get Email
    # --------------------------------------------------

    while True:

        email = input(
            "Email: "
        ).strip().lower()

        if not email:

            print(
                "Email cannot be empty."
            )

            continue

        # Check if the email already exists
        email_exists = any(
            candidate.get("email") == email
            for candidate in candidates
        )

        if email_exists:

            print(
                "This email is already registered."
            )

            continue

        break

    # --------------------------------------------------
    # Create Password
    # --------------------------------------------------

    while True:

        password = getpass.getpass(
            "Password: "
        )

        if len(password) < 4:

            print(
                "Password must be at least 4 characters."
            )

            continue

        confirm_password = getpass.getpass(
            "Confirm Password: "
        )

        if password != confirm_password:

            print(
                "Passwords do not match."
            )

            continue # return to the while loop

        break # exit the loop

    # --------------------------------------------------
    # Create Career Profile
    # --------------------------------------------------

    candidate = create_candidate()

    # Add account information
    candidate["email"] = email

    # Store the hashed password
    candidate["password_hash"] = hash_password(
        password
    )

    # Add the candidate to the list of dictionary
    candidates.append(candidate)

    print(
        "\n✅ Account created successfully!"
    )

    return candidate


def login_candidate(candidates):
    """
    Check the user's email and password.

    """

    print("\n" + "=" * 40)
    print("LOGIN")
    print("=" * 40)

    email = input(
        "Email: "
    ).strip().lower()

    password = getpass.getpass(
        "Password: "
    )

    # Hash the entered password
    password_hash = hash_password(
        password
    )

    # Search for a matching account
    for candidate in candidates:

        if (
            candidate.get("email") == email
            and candidate.get("password_hash")
            == password_hash
        ):

            print(
                f"\n✅ Welcome back, "
                f"{candidate['name']}!"
            )

            return candidate

    print(
        "\n❌ Invalid email or password."
    )

    return None


def display_candidate(candidate):
    """
    Display the user's career profile.

    """

    print("\n" + "-" * 40)

    print(
        f"Name: {candidate['name']}"
    )

    print(
        f"Email: "
        f"{candidate.get('email')}"
    )

    print(
        f"Major: {candidate['major']}"
    )

    print(
        f"Career Stage: "
        f"{candidate['career_stage']}"
    )

    print(
        "Skills: "
        + ", ".join(candidate["skills"]) # join() converts the list into a readable string for display.
    )

    print(
        "Interests: "
        + ", ".join(candidate["interests"]) # join() converts the list into a readable string for display.
    )

    print("-" * 40)