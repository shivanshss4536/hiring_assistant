import random

class HiringAssistant:
    def __init__(self):
        self.state = 0
        self.info = {'name': '', 'email': '', 'phone': '', 'experience': '', 'position': '', 'location': '', 'tech_stack': []}
        self.questions = []
        self.answers = []
        self.ended = False
        self.ending_keywords = ['bye', 'exit', 'quit', 'end', 'finish', 'goodbye']
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
            self.info['tech_stack'] = [x.strip() for x in msg.split(',') if x.strip()]
            self.questions = self.generate_questions(self.info['tech_stack'])
            self.state = 7
            self.q_idx = 0
            return (f"Great! Let's start the technical questions.\nQuestion 1: {self.questions[0]}", False)
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
        for tech in techs:
            tech_lower = tech.lower()
            if 'python' in tech_lower:
                questions.append(f"What is your experience with {tech}? Can you explain a basic concept?")
            elif 'java' in tech_lower:
                questions.append(f"How familiar are you with {tech}? What's the main difference from other languages?")
            elif 'javascript' in tech_lower or 'js' in tech_lower:
                questions.append(f"Tell me about your experience with {tech}. What frameworks have you used?")
            elif 'react' in tech_lower:
                questions.append(f"What do you know about {tech}? How does it work?")
            elif 'django' in tech_lower:
                questions.append(f"Have you worked with {tech}? What's its main purpose?")
            elif 'sql' in tech_lower or 'mysql' in tech_lower or 'postgresql' in tech_lower:
                questions.append(f"What's your experience with {tech}? Can you write basic queries?")
            elif 'aws' in tech_lower or 'cloud' in tech_lower:
                questions.append(f"Tell me about your experience with {tech}. What services have you used?")
            elif 'docker' in tech_lower:
                questions.append(f"What do you know about {tech}? Why is it useful?")
            elif 'git' in tech_lower:
                questions.append(f"How do you use {tech}? What are the basic commands?")
            else:
                questions.append(f"Tell me about your experience with {tech}. What have you built with it?")
        if not questions:
            questions = ["Tell me about a project you've built with your tech stack."]
        random.shuffle(questions)
        return questions[:5]
