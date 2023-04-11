#python server.py


import base64
import pykerberos

def get_user_id(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    
    try:
        # Parse the Kerberos token from the Authorization header
        _, token = auth_header.split()
        token_bytes = base64.b64decode(token)
        
        # Authenticate the user using PyKerberos
        service_name = 'HTTP/{}'.format(request.host)
        flags = pykerberos.GSS_C_MUTUAL_FLAG | pykerberos.GSS_C_SEQUENCE_FLAG | pykerberos.GSS_C_INTEG_FLAG
        user_id = pykerberos.authGSSServerInit(service_name)
        pykerberos.authGSSServerStep(user_id, token_bytes)
        client_name = pykerberos.authGSSServerUserName(user_id)
        client_id = client_name.split('@')[0]
        
        return client_id
    except Exception as e:
        # Log any errors and return None
        print('Error getting user ID:', e)
        return None
