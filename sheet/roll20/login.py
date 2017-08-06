import logging
import re
from typing import Dict, List  # noqa

import bs4
import requests

logger = logging.getLogger(__name__)


class Roll20AuthenticationError(RuntimeError):
    pass


class Roll20LoginError(RuntimeError):
    pass


class Roll20Login:
    def __init__(self, firebase_root: str, auth_token: str, campaign_path: str,
                 campaign_name: str) -> None:
        self.firebase_root = firebase_root
        self.auth_token = auth_token
        self.campaign_path = campaign_path
        self.campaign_name = campaign_name


def login(email: str, password: str, campaign_id: int) -> Roll20Login:
    session = requests.session()
    session.post(
        'https://app.roll20.net/sessions/create',
        data={'email': email, 'password': password}
    )

    campaigns_response = session.get('https://app.roll20.net/campaigns/search')
    document = bs4.BeautifulSoup(campaigns_response.text, 'html.parser')

    title = document.find_all('title')[0]
    if 'Login' in title.string:
        raise Roll20AuthenticationError('Roll20 password is not correct.')

    campaigns: List[Dict[str, str]] = []
    for div in document.find_all('div'):
        if 'class' in div.attrs and 'gameinfo' in div['class']:
            if 'Join Game' in div.text:
                campaigns.append({
                    'name': div.a.text,
                    'link': div.find_all('a')[1]['href']
                })

    if len(campaigns) == 0:
        raise Roll20LoginError('No campaigns found for this player.')

    found_campaign = None
    for campaign in campaigns:
        current_campaign_id = int(re.search(r'setcampaign/(\d+)', campaign['link']).group(1))
        logger.debug(f'Found campaign #{current_campaign_id} {campaign["name"]}')
        if current_campaign_id == campaign_id:
            found_campaign = campaign

    if found_campaign is None:
        raise Roll20LoginError(f'Campaign ID {campaign_id} could not be found.')

    join_response = session.get(found_campaign['link'])
    startjs = None
    document = bs4.BeautifulSoup(join_response.text, 'html.parser')
    for script in document.find_all('script'):
        if 'src' in script.attrs and '/editor/startjs/' in script['src']:
            startjs = script['src']

    if startjs is None:
        raise Roll20LoginError('Could not find startjs.')

    js_response = session.get('https://app.roll20.net' + startjs)
    fb_root = re.search(r'window\.FIREBASE_ROOT\s+=\s+"(.*)"', js_response.text).group(1)
    auth_token = re.search(r'window\.GNTKN\s+=\s+"(.*)"', js_response.text).group(1)
    campaign_path = re.search(r'window\.campaign_storage_path\s+=\s+"(.*)"',
                              js_response.text).group(1)

    logger.debug(f'FIREBASE_ROOT: {fb_root}')
    logger.debug(f'GNTKN: {auth_token}')
    logger.debug(f'campaign_storage_path: {campaign_path}')

    return Roll20Login(firebase_root=fb_root, auth_token=auth_token, campaign_path=campaign_path,
                       campaign_name=found_campaign['name'])
