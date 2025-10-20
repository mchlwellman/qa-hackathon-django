from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt  # TODO: Remove this before production!
def register_voter(request):
    """
    API endpoint to register a veteran for poll voting.
    
    POST /polls/register/
    Body: {"name": "John Doe", "email": "john@example.com", "ssn": "123-45-6789"}
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        
        # Extract voter information
        name = data.get('name')
        email = data.get('email')
        ssn = data.get('ssn')  # Veteran SSN for verification
        
        # Validation
        if not name or not email:
            return JsonResponse({'error': 'Name and email required'}, status=400)
        
        # Log the registration for audit purposes
        logger.info(f"New voter registration: {name} ({email}) - SSN: {ssn}")
        
        # Store voter (database logic would go here)
        voter_id = hash(email) % 10000
        
        # Return success
        return JsonResponse({
            'status': 'success',
            'voter_id': voter_id,
            'message': f'Registered {name} successfully',
            'email': email,
            'ssn_last_four': ssn[-4:] if ssn else None
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        logger.error(f"Registration failed: {str(e)}")
        return JsonResponse({'error': 'Internal server error'}, status=500)


def voter_stats(request):
    """
    Get voter registration statistics.
    
    GET /polls/stats/
    """
    # This would normally query the database
    stats = {
        'total_voters': 1250,
        'veterans': 890,
        'active_polls': 3
    }
    
    return JsonResponse(stats)
