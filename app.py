"""Python Flask app for workshop registration and email confirmation."""
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request


app = Flask(__name__)

MEETING_LINK = "https://teams.live.com/meet/9336306794393?p=kXFSydXysFaA19DXCD"
EMAIL_ADDRESS = "sandeep.kanchamreddy24@gmail.com"
EMAIL_PASSWORD = (
    "qqor jzlf vvxw qnbu"  # Use app password or environment variables for security
)


@app.route("/")
def home():
    """Render the main landing page."""
    # Render main landing page with title + register button
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Render registration form and handle form submission."""
    if request.method == "POST":
        # Get all form fields
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        organization = request.form["organization"]
        role = request.form["role"]
        year = request.form.get("year", "")
        experience = request.form.get("experience", "")
        topics = request.form.getlist("topics")  # multiple checkboxes
        expectations = request.form.get("expectations", "")
        referrer = request.form.get("referrer", "")

        # Send confirmation email
        send_confirmation_email(name, email)

        # Show thank you message or redirect
        return f"Thanks for registering, {name}! A confirmation email has been sent."

    return render_template("form.html")


def send_confirmation_email(name, recipient_email):
    """Send a confirmation email to the registrant."""
    subject = "Thanks for Registering for the Python Workshop!"
    body = f"""
Hi {name},

Thank you for registering for the "Python for Beginners" workshop.

📅 Date: 1st June 2025 - 10.00 AM to 01.00 PM  
📍 Join via Microsoft Teams: {MEETING_LINK}

We're excited to have you with us!

Best regards,  
Sandeep Kumar Kanchamreddy
"""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


if __name__ == "__main__":
    app.run(debug=True)
