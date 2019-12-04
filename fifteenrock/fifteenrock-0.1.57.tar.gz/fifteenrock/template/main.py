# main.py
# deploy this for everyone and other apps!
import fifteenrock
from . import fifteenrock_project_main


def main(context, event):
    return context.Response(body=fiteenrock_project_main._main(event),
                            headers={},
                            content_type='text/json',
                            status_code=200)
