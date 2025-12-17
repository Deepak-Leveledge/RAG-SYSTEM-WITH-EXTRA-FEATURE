from services.embeddings import embedding_text, embedding_query



def test_embeddings():
    texts = ["""
        ✅ PDF loader test passed
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
t 2024
- Sep
2024
• Developed full-stack applications and implemented RESTful APIs with CRUD operations.
• Built responsive UIs and collaborated on front-end and back-end development.
• Contributed to database management and system optimization.
SKILLS
2024
• Developed full-stack applications and implemented RESTful APIs with CRUD operations.
• Built responsive UIs and collaborated on front-end and back-end development.
• Contributed to database management and system optimization.
SKILLS
• Developed full-stack applications and implemented RESTful APIs with CRUD operations.
• Built responsive UIs and collaborated on front-end and back-end development.
• Contributed to database management and system optimization.
SKILLS
• Built responsive UIs and collaborated on front-end and back-end development.
• Contributed to database management and system optimization.
SKILLS
d back-end development.
• Contributed to database management and system optimization.
SKILLS
ation.
SKILLS

Technical Skills JavaScript , Python , HTML, CSS , TailTechnical Skills JavaScript , Python , HTML, CSS , Tailwind CSS, SQL, MySQL , Mongodb
Fra"""
    ]

    vectors = embedding_text(texts)

    # assert len(vectors) == 2
    assert len(vectors[0]) > 100  # dimension check

    print("✅ Text embeddings generated successfully")
    # print(f"First embedding vector (truncated): {vectors[0][:5]}...")  # Print first 5 dimensions for verification


def test_query_embedding():
    query = "Who is Deepak Gupta?"
    vector = embedding_query(query)

    assert isinstance(vector, list)
    assert len(vector) > 100

    print("✅ Query embedding generated successfully")
    # print(f"Query embedding vector (truncated): {vector[:5]}...")  # Print first 5 dimensions for verification


if __name__ == "__main__":
    test_embeddings()
    test_query_embedding()

# python -m test.embeddings_test
