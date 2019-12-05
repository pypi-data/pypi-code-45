from requests_futures.sessions import FuturesSession
from concurrent.futures import CancelledError, TimeoutError
import logging
import json
import time

logger = logging.getLogger(__name__)

class StakionError(RuntimeError):
    '''Stakion custom exception'''
    pass


class publisherPost():
    """Publish message using POST.
    
    Parameters
    ----------
    url: str
        URL to post messages to
    """
    def __init__(self, url):
        self.url = url
        self.session = FuturesSession()
        
        # Get access token
        self.timeout = 60
        self.max_retries = 3
    
    def emit(self, message, callback, nb_retries = 0):
        """Publish message
        
        Parameters
        ----------
        message: dict
            Message to push to Stakion.
        callback: func
            The callback function is called when the message is acknowledges.
        """
        def response_hook(resp, *args, **kwargs):
            logger.debug('status_code = {} - nb_retries = {}'.format(resp.status_code, nb_retries))
            
            # Catch 404 errors
            if resp.status_code == 404:
                logger.error('Failed to decode response')
                raise ValueError("host not found")
            
            # Decode response
            try:
                response = resp.json()
            except:
                logger.error('Failed to decode response')
                raise ValueError("Failed to decode response")
            
            # Handle 401
            if (resp.status_code == 401):
                logger.warning('Could not send message - [error: {}]'.format(response['error']))
            else :
                for error_message in response['errors']:
                    logger.warning('Could not send message - [uid: {}, correlation_id: {}, error: {}]'.format(
                        error_message['message']['__uuid'], error_message['message']['correlation_id'],
                        error_message['error'])
                    )
                for published_messages in response['published']:
                    callback(published_messages['__uuid'])
        
        # Publish message
        self.session.post(self.url, json=[{'log': message}], hooks={
            'response': response_hook
        })