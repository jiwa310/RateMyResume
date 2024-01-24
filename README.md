# SBHacksX 
Jim Wang, Jason Wang, Vincent Cheong, Edwin Yee

# RateMyResume

# Steps to run web application
In order to run this web application, follow these steps:
1. Run "npm install" in ratemyresume folder
2. Run "npm run dev" in ratemyresume folder
3. Run "uvicorn main:app --reload" in the fastapi folder

# Inspiration
As 2nd/3rd-year undergraduate college students, we wanted an online platform where we could gain inspiration from existing resumes and quickly receive resume critiques. However, individuals generally do not want to upload the sensitive information that's found on their resume to the internet due to privacy concerns. Thus, we thought of trying to create a project that automatically anonymizes our resume whenever a user uploads their resume to the site. In addition to anonymizing the resume, we also wanted to create a large database of resumes from real people (as opposed to the existing databases of templates and fake resumes) that users can view at any time to use for inspiration for their resumes. This will hopefully foster a large community that supports each other by giving career advice.

# What it does
RateMyResume is a web app that allows users to upload a resume in PDF format. Then, we will automatically anonymize the resume by redacting any personally identifiable information (PII) on it. Then, the user will have the option to post them on a forum-like website that other people can view, critique, and comment on.
When the user decides to post their resume, it will be added to a large database of resumes that can be viewed by anyone at any time.

# How we built it
We built the project using Next.js for the front end and FastAPI to process the PDFs with Python. Using a Python backend, we used FastAPI to make calls to other APIs like Amazon Comprehend. Utilizing Next.js and FastAPI simplified much of the code for us.

# Challenges we ran into
Our biggest challenge was building the infrastructure of the web app. As beginners, we had limited knowledge of which technologies/services were suitable for what we wanted to accomplish with our project. By talking to mentors during the SBHacks X event, we were able to learn from their valuable advice and gained insight into how to use various technologies. For example, we didn't know that the Amazon Comprehend API existed and what FastAPI was.
Connecting the database to the front end and back end. Since we did not have much experience with the backend, we struggled with our first usage of FastAPI, and connecting the frontend to the backend.
Displaying PDFs on the Next.js app as a clickable grid also proved to be a challenge.

# Accomplishments that we're proud of
1) Integrated a disqus comment section for each resume
2) Used FastApi to process the PDFs with Python and send them back to the Next.js app
3) Learning about various AWS services & integrating Comprehend into our project
What we learned
How to use FastAPI, and how to efficiently send post requests from a Next.js app to FastAPI to use Python with Next.js. We also learned how to utilize the Amazon Comprehend API and call it when needed for our project.

# What's next for RateMyResume
We would love to start a community on RateMyResume by having people upload their resumes. We would also like to add a manual review stage before the user posts their resume, where the user can choose to redact additional information or restore redacted text. Though the NLP model used by the Comprehend API is usually quite accurate, the way the PyMuPDF library searches for the PII words is sometimes inaccurate, causing the black boxes to appear where we don't want them to. We also would like to have a way for users to sort resumes by major and by votes.
