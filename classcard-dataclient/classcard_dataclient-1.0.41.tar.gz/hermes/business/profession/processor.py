import traceback
from business.profession.action import upload_student_attendance
from utils.loggerutils import logging

logger = logging.getLogger(__name__)


class ProfessionProcessor(object):
    KIND_FUNC = {"OpenStudentAttendance": "upload_student_attendance"}

    @classmethod
    def distribute(cls, topic, payload):
        try:
            data = payload['data']
            kind, content = data["kind"], data["extra"]
        except (Exception,):
            return None
        try:
            if kind in cls.KIND_FUNC:
                getattr(cls, cls.KIND_FUNC[kind])(content)
                return "success"
        except (Exception,):
            logger.error(traceback.print_exc())
            return "failed"

    @staticmethod
    def upload_student_attendance(content):
        upload_student_attendance(content)
