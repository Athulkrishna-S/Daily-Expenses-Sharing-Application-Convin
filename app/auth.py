from app import jwt

blacklisted_tokens = set()

# Check if token is in blacklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']  # JTI is a unique identifier for each JWT
    return jti in blacklisted_tokens