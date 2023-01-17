

class Cart():

    def __init__(self, request):

            self.session = request.session

            # User był, sesja istnieje:

            cart = self.session.get('session_key')

            # User jest pierwszy raz:

            if 'session_key' not in request.session:

                cart = self.session['session_key'] = {}

            self.cart = cart