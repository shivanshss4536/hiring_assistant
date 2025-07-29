import openai
import random

class HiringAssistant:
    def __init__(self):
        self.state = 0
        self.info = {'name': '', 'email': '', 'phone': '', 'experience': '', 'position': '', 'location': '', 'tech_stack': []}
        self.questions = []
        self.answers = []
        self.ended = False
        self.ending_keywords = ['bye', 'exit', 'quit', 'end', 'finish', 'goodbye']
        self.question_source = "AI Generated"
        
        self.fallback_questions = {
            'python': [
                "What are the key differences between Python 2 and Python 3?",
                "Explain the concept of decorators in Python with an example.",
                "How does Python handle memory management?",
                "What is the difference between a list and a tuple in Python?",
                "Explain the GIL (Global Interpreter Lock) in Python."
            ],
            'javascript': [
                "What is the difference between '==' and '===' in JavaScript?",
                "Explain closures in JavaScript with an example.",
                "What is hoisting in JavaScript?",
                "How does the 'this' keyword work in JavaScript?",
                "Explain the event loop in JavaScript."
            ],
            'java': [
                "What is the difference between HashMap and HashTable in Java?",
                "Explain the concept of polymorphism in Java.",
                "What are the differences between abstract classes and interfaces?",
                "How does garbage collection work in Java?",
                "Explain the concept of threads in Java."
            ],
            'react': [
                "What is the difference between state and props in React?",
                "Explain the React component lifecycle methods.",
                "What are hooks in React and how do you use them?",
                "How does React handle state updates?",
                "What is the Virtual DOM and how does it work?"
            ],
            'node.js': [
                "What is the event-driven programming model in Node.js?",
                "Explain the difference between synchronous and asynchronous operations.",
                "How does Node.js handle concurrency?",
                "What is the purpose of package.json in Node.js?",
                "Explain the concept of middleware in Express.js."
            ],
            'sql': [
                "What is the difference between INNER JOIN and LEFT JOIN?",
                "Explain the concept of database normalization.",
                "What are indexes and when should you use them?",
                "How do you optimize a slow SQL query?",
                "What is the difference between DELETE and TRUNCATE?"
            ],
            'docker': [
                "What is the difference between a Docker image and a container?",
                "Explain the concept of Docker layers.",
                "How do you optimize Docker image size?",
                "What is Docker Compose and when would you use it?",
                "How do you handle environment variables in Docker?"
            ],
            'aws': [
                "What is the difference between EC2 and Lambda?",
                "Explain the concept of auto-scaling in AWS.",
                "What is the purpose of IAM roles and policies?",
                "How does S3 handle data consistency?",
                "What are the different types of load balancers in AWS?"
            ],
            'machine learning': [
                "What is the difference between supervised and unsupervised learning?",
                "Explain the concept of overfitting and how to prevent it.",
                "What is cross-validation and why is it important?",
                "How do you handle imbalanced datasets?",
                "Explain the bias-variance tradeoff."
            ],
            'data science': [
                "What is the difference between correlation and causation?",
                "How do you handle missing data in a dataset?",
                "Explain the concept of feature engineering.",
                "What is the purpose of exploratory data analysis?",
                "How do you evaluate the performance of a model?"
            ]
        }
        
        self.general_questions = [
            "Tell me about a challenging project you've worked on recently.",
            "How do you approach debugging a complex issue?",
            "What's your experience with version control systems like Git?",
            "How do you stay updated with the latest technology trends?",
            "Describe a time when you had to learn a new technology quickly.",
            "How do you handle working with legacy code?",
            "What's your experience with agile development methodologies?",
            "How do you approach code reviews and giving feedback?",
            "Tell me about a time when you had to optimize performance.",
            "How do you handle conflicting requirements from stakeholders?"
        ]

    def get_greeting(self):
        return "Hello! I'm TalentScout's Hiring Assistant. I'll collect your info and ask you technical questions based on your skills. Let's start with your full name."

    def process_message(self, msg):
        if any(k in msg.lower() for k in self.ending_keywords):
            self.ended = True
            return ("Thank you for your time. We'll be in touch soon!", True)
        
        if self.state == 0:
            self.info['name'] = msg.strip()
            self.state = 1
            return ("What's your email address?", False)
        if self.state == 1:
            self.info['email'] = msg.strip()
            self.state = 2
            return ("What's your phone number?", False)
        if self.state == 2:
            self.info['phone'] = msg.strip()
            self.state = 3
            return ("How many years of experience do you have?", False)
        if self.state == 3:
            self.info['experience'] = msg.strip()
            self.state = 4
            return ("What position are you interested in?", False)
        if self.state == 4:
            self.info['position'] = msg.strip()
            self.state = 5
            return ("Where are you currently located?", False)
        if self.state == 5:
            self.info['location'] = msg.strip()
            self.state = 6
            return ("List your tech stack (comma separated, e.g. Python, Django, React):", False)
        if self.state == 6:
            self.info['tech_stack'] = [x.strip().lower() for x in msg.split(',') if x.strip()]
            self.questions = self.generate_questions(self.info['tech_stack'])
            self.state = 7
            self.q_idx = 0
            
            source_info = f"📝 Questions generated using: {self.question_source}"
            return (f"Great! Let's start the technical questions.\n{source_info}\n\nQuestion 1: {self.questions[0]}", False)
        if self.state == 7:
            self.answers.append(msg.strip())
            self.q_idx += 1
            if self.q_idx < len(self.questions):
                return (f"Question {self.q_idx+1}: {self.questions[self.q_idx]}", False)
            else:
                self.state = 8
                return ("Thanks for answering the questions! Type 'bye' or 'exit' to finish.", False)
        if self.state == 8:
            return ("Session ended. Thank you!", True)
        return ("Sorry, I didn't understand. Please try again.", False)

    def generate_questions(self, techs):
        questions = []
        
        try:
            questions = self._generate_with_openai(techs)
            if questions:
                self.question_source = "AI Generated"
                return self._finalize_questions(questions)
        except Exception as e:
            print(f"OpenAI API failed: {e}")
        
        questions = self._get_fallback_questions(techs)
        if questions:
            self.question_source = "Predefined Tech Questions"
            return self._finalize_questions(questions)
        
        questions = random.sample(self.general_questions, min(5, len(self.general_questions)))
        self.question_source = "General Technical Questions"
        return self._finalize_questions(questions)

    def _finalize_questions(self, questions):
        random.shuffle(questions)
        return questions[:5]

    def _generate_with_openai(self, techs):
        prompt = (
            "You are a technical interviewer. Generate 3-5 technical interview questions for a candidate proficient in the following technologies: "
            + ", ".join(techs) + ". Questions should be relevant, clear, and assess both breadth and depth. "
            "Return only the questions, one per line, without numbering."
        )
        
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.7
            )
            
            questions = [q.strip() for q in response.choices[0].message.content.split('\n') if q.strip()]
            return questions
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return []

    def _get_fallback_questions(self, techs):
        all_questions = []
        
        for tech in techs:
            if tech in self.fallback_questions:
                all_questions.extend(self.fallback_questions[tech])
            
            for key in self.fallback_questions:
                if key in tech or tech in key:
                    all_questions.extend(self.fallback_questions[key])
        
        seen = set()
        unique_questions = []
        for q in all_questions:
            if q not in seen:
                seen.add(q)
                unique_questions.append(q)
        
        return unique_questions

    def get_question_source(self):
        return self.question_source
