from services.chunker import chunk_text
text="""✅ PDF loader test passed
DEEPAKGUPT A 
7506604244 ⋄ Mumbai, Maharashtra ⋄ deepakleveledge@gmail.com
Portfolio ⋄ LinkedIn ⋄ GitHub
EDUCATION

Universal College Of Engineering, Mumbai University    
B.E in Data Engineering with Honors in Cyber security – CGPA : 8.1.
2021 -
2024
Viva College of Diploma Engineering Technology Diploma in Computer
Engineering – percentage : 84
EXPERIENCE

2019 -
2021
Leveledge Technologies (Full-Stack Developer Intern) Augus
t 2024
- Sep
2024
• Developed full-stack applications and implemented RESTful APIs with CRUD operations.
• Built responsive UIs and collaborated on front-end and back-end development.
• Contributed to database management and system optimization.
SKILLS

Technical Skills JavaScript , Python , HTML, CSS , Tailwind CSS, SQL, MySQL , Mongodb
FrameWorks React.js , Node.js ,Express.js, WordPress   
Developer Tools Git , GitHub ,Visual Studio editor , Android Studio,Pycharm
Other Skills web development, MERN stack, communication, problem-solving,Databases.
PROJECTS

Task Management System (TechStack: MERN Stack).        
• Developed a full-stack task management application with JWT-based user authentication for secure login and  
signup.
• Implemented task creation, deletion, updating, and viewing, with tasks displayed in a card format.
• Integrated email notifications using Nodemailer to welcome new users upon registration.
Plant Leaf Disease Detection (TechStack : Python , Flask)
• Developed a plant leaf detection application to classify healthy and unhealthy plants using a CNN model.    
• Utilized a detailed plant dataset along with NumPy, Pandas, and Matplotlib for data processing and
visualization.
Dual-portal healthcare management (TechStack: MERN Stack).
• Dual-portal healthcare management system with role-based authentication, enabling Receptionists to
manage patient records (CRUD) and Doctors to access data visualization and analytics.
Speech-to-Text Converter. (TechStack : React.js, SpeechRecognition API, react-use-clipboard )
• Developed a speech-to-text converter application using ReactJS, featuring real-time speech recognition and  
copy to clipboard functionality.
• Included user-friendly buttons for starting, stopping, and resetting transcription.
CERTIFICATIONS

• AWS Academy Graduates -AWS Academy Introduction to Cloud
• Info Sec Developer Mobile Application Development    
• Python Programming Language in Data Camp
✅ DOCX loader test passed
DEEPAKGUPTA
7506604244 ⋄ Mumbai, Maharashtra ⋄ deepakleveledge@gmail.com
Portfolio ⋄ LinkedIn ⋄ GitHub
EDUCATION
Developed full-stack applications and implemented RESTful APIs with CRUD operations.
Built responsive UIs and collaborated on front-end and back-end development.
Contributed to database management and system optimization.
SKILLS
PROJECTS
Task Management System (TechStack: MERN Stack).        
Developed a full-stack task management application with JWT-based user authentication for secure login and signup.
Implemented task creation, deletion, updating, and viewing, with tasks displayed in a card format.
Integrated email notifications using Nodemailer to welcome new users upon registration.
Plant Leaf Disease Detection (TechStack : Python , Flask)
Developed a plant leaf detection application to classify healthy and unhealthy plants using a CNN model.      
Utilized a detailed plant dataset along with NumPy, Pandas, and Matplotlib for data processing and visualization.
Dual-portal healthcare management (TechStack: MERN Stack).
Dual-portal healthcare management system with role-based authentication, enabling Receptionists to manage patient records (CRUD) and Doctors to access data visualization and analytics.
Speech-to-Text Converter. (TechStack : React.js, SpeechRecognition API, react-use-clipboard )
Developed a speech-to-text converter application using ReactJS, featuring real-time speech recognition and copy to clipboard functionality.
Included user-friendly buttons for starting, stopping, and resetting transcription.
CERTIFICATIONS
AWS Academy Graduates -AWS Academy Introduction to Cloud
Developed a speech-to-text converter application using ReactJS, featuring real-time speech recognition and copy to clipboard functionality.
Included user-friendly buttons for starting, stopping, and resetting transcription.
CERTIFICATIONS
AWS Academy Graduates -AWS Academy Introduction to Cloud
ReactJS, featuring real-time speech recognition and copy to clipboard functionality.
Included user-friendly buttons for starting, stopping, and resetting transcription.
CERTIFICATIONS
AWS Academy Graduates -AWS Academy Introduction to Cloud
Included user-friendly buttons for starting, stopping, and resetting transcription.
CERTIFICATIONS
AWS Academy Graduates -AWS Academy Introduction to Cloud
CERTIFICATIONS
AWS Academy Graduates -AWS Academy Introduction to Cloud
AWS Academy Graduates -AWS Academy Introduction to Cloud
d
Info Sec Developer Mobile Application Development      
Python Programming Language in Data Camp"""

def test_chunk_text(text:str):
    chunks = chunk_text(text)

    assert isinstance(chunks, list)
    assert len(chunks) > 0

    print(f"✅ Chunker created {len(chunks)} chunks")
    print(f"First chunk: {chunks[0]}")  # Print the first chunk for verification

if __name__ == "__main__":
    test_chunk_text(text)


# for testing purpose only
# python -m test.chunker_test