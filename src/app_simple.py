"""
Simple Flask application for API documentation demo.
"""
from flask import Flask
from flask_restx import Api, Namespace, Resource, fields
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
CORS(app)

# Create API
api = Api(
    version='1.0.0',
    title='Todo API',
    description='A simple Todo API for demonstration',
    doc='/docs',
    authorizations={
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Type 'Bearer <JWT>' where JWT is the token"
        }
    },
    security='apikey'
)

# Create namespaces
users_ns = Namespace('users', description='User management operations')
todos_ns = Namespace('todos', description='Todo management operations')
subjects_ns = Namespace('subjects', description='Subject management operations')
messages_ns = Namespace('messages', description='Message management operations')
tutor_profiles_ns = Namespace('tutor_profiles', description='Tutor profile management operations')

# User models
user_model = users_ns.model('User', {
    'user_id': fields.Integer(readonly=True, description='User ID'),
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email'),
    'full_name': fields.String(required=True, description='Full name')
})

user_create_model = users_ns.model('UserCreate', {
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email'),
    'full_name': fields.String(required=True, description='Full name'),
    'password': fields.String(required=True, description='Password')
})

# Todo models
todo_model = todos_ns.model('Todo', {
    'todo_id': fields.Integer(readonly=True, description='Todo ID'),
    'title': fields.String(required=True, description='Todo title'),
    'description': fields.String(description='Todo description'),
    'completed': fields.Boolean(description='Completion status')
})

todo_create_model = todos_ns.model('TodoCreate', {
    'title': fields.String(required=True, description='Todo title'),
    'description': fields.String(description='Todo description')
})

# Subject models
subject_model = subjects_ns.model('Subject', {
    'subject_id': fields.Integer(readonly=True, description='Subject ID'),
    'name': fields.String(required=True, description='Subject name'),
    'description': fields.String(description='Subject description')
})

subject_create_model = subjects_ns.model('SubjectCreate', {
    'name': fields.String(required=True, description='Subject name'),
    'description': fields.String(description='Subject description')
})

# Message models
message_model = messages_ns.model('Message', {
    'message_id': fields.Integer(readonly=True, description='Message ID'),
    'content': fields.String(required=True, description='Message content'),
    'sender': fields.String(required=True, description='Sender'),
    'timestamp': fields.DateTime(description='Message timestamp')
})

message_create_model = messages_ns.model('MessageCreate', {
    'content': fields.String(required=True, description='Message content'),
    'sender': fields.String(required=True, description='Sender')
})

# Tutor Profile models
tutor_profile_model = tutor_profiles_ns.model('TutorProfile', {
    'tutor_profile_id': fields.Integer(readonly=True, description='Tutor Profile ID'),
    'name': fields.String(required=True, description='Tutor name'),
    'specialization': fields.String(description='Specialization'),
    'experience_years': fields.Integer(description='Years of experience')
})

tutor_profile_create_model = tutor_profiles_ns.model('TutorProfileCreate', {
    'name': fields.String(required=True, description='Tutor name'),
    'specialization': fields.String(description='Specialization'),
    'experience_years': fields.Integer(description='Years of experience')
})

# User endpoints
@users_ns.route('/')
class UserList(Resource):
    @users_ns.doc('list_users')
    @users_ns.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        return [
            {
                "user_id": 1,
                "username": "john_doe",
                "email": "john@example.com",
                "full_name": "John Doe"
            },
            {
                "user_id": 2,
                "username": "jane_smith",
                "email": "jane@example.com",
                "full_name": "Jane Smith"
            }
        ]

    @users_ns.doc('create_user')
    @users_ns.expect(user_create_model)
    @users_ns.marshal_with(user_model)
    @users_ns.response(201, 'User created successfully')
    def post(self):
        """Create a new user"""
        data = users_ns.payload
        return {
            "user_id": 3,
            "username": data.get('username'),
            "email": data.get('email'),
            "full_name": data.get('full_name')
        }, 201

@users_ns.route('/<int:user_id>')
@users_ns.param('user_id', 'The user identifier')
class UserDetail(Resource):
    @users_ns.doc('get_user')
    @users_ns.marshal_with(user_model)
    def get(self, user_id):
        """Get a user by ID"""
        return {
            "user_id": user_id,
            "username": "john_doe",
            "email": "john@example.com",
            "full_name": "John Doe"
        }

    @users_ns.doc('update_user')
    @users_ns.expect(user_create_model)
    @users_ns.marshal_with(user_model)
    def put(self, user_id):
        """Update an existing user"""
        data = users_ns.payload
        return {
            "user_id": user_id,
            "username": data.get('username'),
            "email": data.get('email'),
            "full_name": data.get('full_name')
        }

    @users_ns.doc('update_user_partial')
    @users_ns.expect(user_create_model)
    @users_ns.marshal_with(user_model)
    def patch(self, user_id):
        """Partially update an existing user"""
        data = users_ns.payload
        return {
            "user_id": user_id,
            "username": data.get('username', "john_doe"),
            "email": data.get('email', "john@example.com"),
            "full_name": data.get('full_name', "John Doe")
        }

    @users_ns.doc('delete_user')
    def delete(self, user_id):
        """Delete a user"""
        return {"message": f"User {user_id} deleted successfully"}

# Todo endpoints
@todos_ns.route('/')
class TodoList(Resource):
    @todos_ns.doc('list_todos')
    @todos_ns.marshal_list_with(todo_model)
    def get(self):
        """Get all todos"""
        return [
            {
                "todo_id": 1,
                "title": "Learn Flask",
                "description": "Study Flask framework",
                "completed": False
            },
            {
                "todo_id": 2,
                "title": "Build API",
                "description": "Create REST API",
                "completed": True
            }
        ]

    @todos_ns.doc('create_todo')
    @todos_ns.expect(todo_create_model)
    @todos_ns.marshal_with(todo_model)
    @todos_ns.response(201, 'Todo created successfully')
    def post(self):
        """Create a new todo"""
        data = todos_ns.payload
        return {
            "todo_id": 3,
            "title": data.get('title'),
            "description": data.get('description'),
            "completed": False
        }, 201

@todos_ns.route('/<int:todo_id>')
@todos_ns.param('todo_id', 'The todo identifier')
class TodoDetail(Resource):
    @todos_ns.doc('get_todo')
    @todos_ns.marshal_with(todo_model)
    def get(self, todo_id):
        """Get a todo by ID"""
        return {
            "todo_id": todo_id,
            "title": "Learn Flask",
            "description": "Study Flask framework",
            "completed": False
        }

    @todos_ns.doc('update_todo')
    @todos_ns.expect(todo_create_model)
    @todos_ns.marshal_with(todo_model)
    def put(self, todo_id):
        """Update an existing todo"""
        data = todos_ns.payload
        return {
            "todo_id": todo_id,
            "title": data.get('title'),
            "description": data.get('description'),
            "completed": False
        }

    @todos_ns.doc('update_todo_partial')
    @todos_ns.expect(todo_create_model)
    @todos_ns.marshal_with(todo_model)
    def patch(self, todo_id):
        """Patch an existing todo"""
        data = todos_ns.payload
        return {
            "todo_id": todo_id,
            "title": data.get('title', "Learn Flask"),
            "description": data.get('description', "Study Flask framework"),
            "completed": False
        }

    @todos_ns.doc('delete_todo')
    def delete(self, todo_id):
        """Delete a todo"""
        return {"message": f"Todo {todo_id} deleted successfully"}

# Subject endpoints
@subjects_ns.route('/')
class SubjectList(Resource):
    @subjects_ns.doc('list_subjects')
    @subjects_ns.marshal_list_with(subject_model)
    def get(self):
        """Get all subjects"""
        return [
            {
                "subject_id": 1,
                "name": "Mathematics",
                "description": "Advanced mathematics"
            },
            {
                "subject_id": 2,
                "name": "Physics",
                "description": "Classical physics"
            }
        ]

    @subjects_ns.doc('create_subject')
    @subjects_ns.expect(subject_create_model)
    @subjects_ns.marshal_with(subject_model)
    @subjects_ns.response(201, 'Subject created successfully')
    def post(self):
        """Create a new subject"""
        data = subjects_ns.payload
        return {
            "subject_id": 3,
            "name": data.get('name'),
            "description": data.get('description')
        }, 201

@subjects_ns.route('/<int:subject_id>')
@subjects_ns.param('subject_id', 'The subject identifier')
class SubjectDetail(Resource):
    @subjects_ns.doc('get_subject')
    @subjects_ns.marshal_with(subject_model)
    def get(self, subject_id):
        """Get a subject by ID"""
        return {
            "subject_id": subject_id,
            "name": "Mathematics",
            "description": "Advanced mathematics"
        }

    @subjects_ns.doc('update_subject')
    @subjects_ns.expect(subject_create_model)
    @subjects_ns.marshal_with(subject_model)
    def put(self, subject_id):
        """Update an existing subject"""
        data = subjects_ns.payload
        return {
            "subject_id": subject_id,
            "name": data.get('name'),
            "description": data.get('description')
        }

    @subjects_ns.doc('update_subject_partial')
    @subjects_ns.expect(subject_create_model)
    @subjects_ns.marshal_with(subject_model)
    def patch(self, subject_id):
        """Patch an existing subject"""
        data = subjects_ns.payload
        return {
            "subject_id": subject_id,
            "name": data.get('name', "Mathematics"),
            "description": data.get('description', "Advanced mathematics")
        }

    @subjects_ns.doc('delete_subject')
    def delete(self, subject_id):
        """Delete a subject"""
        return {"message": f"Subject {subject_id} deleted successfully"}

# Message endpoints
@messages_ns.route('/')
class MessageList(Resource):
    @messages_ns.doc('list_messages')
    @messages_ns.marshal_list_with(message_model)
    def get(self):
        """Get all messages"""
        return [
            {
                "message_id": 1,
                "content": "Hello world!",
                "sender": "user1",
                "timestamp": "2024-01-01T10:00:00"
            },
            {
                "message_id": 2,
                "content": "How are you?",
                "sender": "user2",
                "timestamp": "2024-01-01T11:00:00"
            }
        ]

    @messages_ns.doc('create_message')
    @messages_ns.expect(message_create_model)
    @messages_ns.marshal_with(message_model)
    @messages_ns.response(201, 'Message created successfully')
    def post(self):
        """Create a new message"""
        data = messages_ns.payload
        return {
            "message_id": 3,
            "content": data.get('content'),
            "sender": data.get('sender'),
            "timestamp": "2024-01-01T12:00:00"
        }, 201

@messages_ns.route('/<int:message_id>')
@messages_ns.param('message_id', 'The message identifier')
class MessageDetail(Resource):
    @messages_ns.doc('get_message')
    @messages_ns.marshal_with(message_model)
    def get(self, message_id):
        """Get a message by ID"""
        return {
            "message_id": message_id,
            "content": "Hello world!",
            "sender": "user1",
            "timestamp": "2024-01-01T10:00:00"
        }

    @messages_ns.doc('update_message')
    @messages_ns.expect(message_create_model)
    @messages_ns.marshal_with(message_model)
    def put(self, message_id):
        """Update an existing message"""
        data = messages_ns.payload
        return {
            "message_id": message_id,
            "content": data.get('content'),
            "sender": data.get('sender'),
            "timestamp": "2024-01-01T10:00:00"
        }

    @messages_ns.doc('update_message_partial')
    @messages_ns.expect(message_create_model)
    @messages_ns.marshal_with(message_model)
    def patch(self, message_id):
        """Patch an existing message"""
        data = messages_ns.payload
        return {
            "message_id": message_id,
            "content": data.get('content', "Hello world!"),
            "sender": data.get('sender', "user1"),
            "timestamp": "2024-01-01T10:00:00"
        }

    @messages_ns.doc('delete_message')
    def delete(self, message_id):
        """Delete a message"""
        return {"message": f"Message {message_id} deleted successfully"}

# Tutor Profile endpoints
@tutor_profiles_ns.route('/')
class TutorProfileList(Resource):
    @tutor_profiles_ns.doc('list_tutor_profiles')
    @tutor_profiles_ns.marshal_list_with(tutor_profile_model)
    def get(self):
        """Get all tutor profiles"""
        return [
            {
                "tutor_profile_id": 1,
                "name": "Dr. Smith",
                "specialization": "Mathematics",
                "experience_years": 10
            },
            {
                "tutor_profile_id": 2,
                "name": "Prof. Johnson",
                "specialization": "Physics",
                "experience_years": 15
            }
        ]

    @tutor_profiles_ns.doc('create_tutor_profile')
    @tutor_profiles_ns.expect(tutor_profile_create_model)
    @tutor_profiles_ns.marshal_with(tutor_profile_model)
    @tutor_profiles_ns.response(201, 'Tutor profile created successfully')
    def post(self):
        """Create a new tutor profile"""
        data = tutor_profiles_ns.payload
        return {
            "tutor_profile_id": 3,
            "name": data.get('name'),
            "specialization": data.get('specialization'),
            "experience_years": data.get('experience_years')
        }, 201

@tutor_profiles_ns.route('/<int:tutor_profile_id>')
@tutor_profiles_ns.param('tutor_profile_id', 'The tutor profile identifier')
class TutorProfileDetail(Resource):
    @tutor_profiles_ns.doc('get_tutor_profile')
    @tutor_profiles_ns.marshal_with(tutor_profile_model)
    def get(self, tutor_profile_id):
        """Get a tutor profile by ID"""
        return {
            "tutor_profile_id": tutor_profile_id,
            "name": "Dr. Smith",
            "specialization": "Mathematics",
            "experience_years": 10
        }

    @tutor_profiles_ns.doc('update_tutor_profile')
    @tutor_profiles_ns.expect(tutor_profile_create_model)
    @tutor_profiles_ns.marshal_with(tutor_profile_model)
    def put(self, tutor_profile_id):
        """Update an existing tutor profile"""
        data = tutor_profiles_ns.payload
        return {
            "tutor_profile_id": tutor_profile_id,
            "name": data.get('name'),
            "specialization": data.get('specialization'),
            "experience_years": data.get('experience_years')
        }

    @tutor_profiles_ns.doc('update_tutor_profile_partial')
    @tutor_profiles_ns.expect(tutor_profile_create_model)
    @tutor_profiles_ns.marshal_with(tutor_profile_model)
    def patch(self, tutor_profile_id):
        """Patch an existing tutor profile"""
        data = tutor_profiles_ns.payload
        return {
            "tutor_profile_id": tutor_profile_id,
            "name": data.get('name', "Dr. Smith"),
            "specialization": data.get('specialization', "Mathematics"),
            "experience_years": data.get('experience_years', 10)
        }

    @tutor_profiles_ns.doc('delete_tutor_profile')
    def delete(self, tutor_profile_id):
        """Delete a tutor profile"""
        return {"message": f"Tutor profile {tutor_profile_id} deleted successfully"}

# Add namespaces to API
api.add_namespace(users_ns, path='/users')
api.add_namespace(todos_ns, path='/todos')
api.add_namespace(subjects_ns, path='/subjects')
api.add_namespace(messages_ns, path='/messages')
api.add_namespace(tutor_profiles_ns, path='/tutor_profiles')

# Initialize API with app
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
