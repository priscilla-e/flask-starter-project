from app.main import main_bp

@main_bp.route('/', methods=['GET'])
def home():
    return {'message': 'Hello world!'}