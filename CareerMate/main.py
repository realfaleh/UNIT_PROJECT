# ---------------- imports ----------------
from storage import load_data, save_data 

from profile import (
    display_candidate,
    register_candidate,
    login_candidate
)

from ai import (
    analyze_candidate,
    suggest_job_titles,
    generate_interview_questions
)

# ---------------- File used to store candidate accounts ----------------
CANDIDATES_FILE = "data/candidates.json"

# ---------------- Display ----------------
def print_header():
    """
    Display the main CareerMate header.

    """
    print("\n")
    print("=" * 50)
    print("              🤖 CareerMate")
    print("   AI-Powered Career Discovery System")
    print("=" * 50)


def job_seeker_menu(current_candidate):
    """
    Display the career menu for the logged-in user.

    """

    while True:

        print("\n" + "=" * 40)
        print("              👩 MY CAREER")
        print("=" * 40)

        print(
            f"\nWelcome, {current_candidate['name']}!"
        )

        print("""
1. 👤 My Profile
2. 🤖 Career Analysis
3. 💼 Suitable Job Titles
4. 🎤 Interview Preparation
5. 🚪 Logout
""")

        choice = input(
            "Choose an option: "
        ).strip()

        # --------------------------------------------------
        # Option 1: Display Profile
        # --------------------------------------------------

        if choice == "1":

            display_candidate(
                current_candidate
            )

        # --------------------------------------------------
        # Option 2: Career Analysis
        # --------------------------------------------------

        elif choice == "2":

            print(
                "\n🤖 Analyzing your career profile..."
            )

            result = analyze_candidate(
                current_candidate
            )

            if result:
                print("\n" + "=" * 50)
                print("          🎯 CAREER ANALYSIS")
                print("=" * 50)
                print(result)
                print("=" * 50)

        # --------------------------------------------------
        # Option 3: Suitable Job Titles
        # --------------------------------------------------

        elif choice == "3":

            print(
                "\n🤖 Finding suitable job titles..."
            )

            result = suggest_job_titles(
                current_candidate
            )

            if result:
                print("\n" + "=" * 50)
                print("        💼 SUITABLE JOB TITLES")
                print("=" * 50)
                print(result)
                print("=" * 50)

        # --------------------------------------------------
        # Option 4: Interview Preparation
        # --------------------------------------------------

        elif choice == "4":

            job_title = input(
                "\nEnter the job title: "
            ).strip()

            if not job_title:
                print(
                    "Job title cannot be empty."
                )
                continue

            print("\n" + "=" * 50)
            print("          🎤 INTERVIEW PREP")
            print("=" * 50)

            print(
                f"\nJob: {job_title}"
            )

            print(
                f"Career Stage: "
                f"{current_candidate['career_stage']}"
            )

            print(
                "\n🤖 Preparing your "
                "interview questions..."
            )

            result = generate_interview_questions(
                job_title,
                current_candidate["career_stage"]
            )

            if result:
                print("\n" + "-" * 50)
                print(result)
                print("-" * 50)

        # --------------------------------------------------
        # Option 5: Logout
        # --------------------------------------------------

        elif choice == "5":

            print(
                "\n👋 Logged out successfully."
            )

            break

        else:

            print(
                "\nInvalid option. "
                "Please try again.."
            )


def main():
    """
    Start the CareerMate application.
    
    """

    # Load saved candidates from JSON
    candidates = load_data(
        CANDIDATES_FILE
    )

    while True:

        print_header()

        print("""
1. 🔐 Login
2. 📝 Create Account
3. ❌ Exit
""")

        choice = input(
            "Choose an option: "
        ).strip()

        # --------------------------------------------------
        # Login
        # --------------------------------------------------

        if choice == "1":

            candidate = login_candidate(
                candidates
            )

            if candidate:

                job_seeker_menu(
                    candidate
                )

        # --------------------------------------------------
        # Create Account
        # --------------------------------------------------

        elif choice == "2":

            candidate = register_candidate(
                candidates
            )

            # Save the new account
            save_data(
                CANDIDATES_FILE,
                candidates
            )

            # Open the career menu
            job_seeker_menu(
                candidate
            )

        # --------------------------------------------------
        # Exit
        # --------------------------------------------------

        elif choice == "3":

            print(
                "\nThank you for using "
                "CareerMate! 👋"
            )

            break

        else:

            print(
                "\nInvalid option. "
                "Please try again."
            )


# Run the program
if __name__ == "__main__":
    main()