import unittest
import traceback
from datetime import datetime
from tv2test.merge_audio_video import MGAudio, MGVideo, MergeAudioVideo 
from tv2test.constants import ConstTestCaseFailReason, ConstDeviceNames
import requests
import json
import time
import abc

class TestCaseModule(unittest.TestCase, metaclass=abc.ABCMeta):
    """
    TestCase classes that need to be parametrized should
    inherit from this class.
    """
    audio_file_path = None

    def __init__(self, method_name='run_test', test_name=None, dut=None, mf=None, test_result=False, test_number=0, audio_file_path=None):
        super(TestCaseModule, self).__init__(method_name)
        self.test_name = test_name
        self.dut = dut
        self.mf = mf
        self.test_result = test_result
        self.test_number = test_number
        self.const_fail_reason = ConstTestCaseFailReason()
        self.fail_reason = None
        audio_file_path = audio_file_path

    'Abstract method to get device name. Every inherited class must implement this method to return device name'
    @classmethod
    @abc.abstractmethod
    def get_device_name(cls):
        raise NotImplementedError

    @staticmethod
    def parametrize(testcase_klass, test_name=None, dut=None, mf=None, test_result=False, test_number=0, audio_file_path=None):
        """
        Create a suite containing all tests taken from the given
        subclass, passing them the parameters.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        suite.addTest(testcase_klass(testnames[0], test_name=test_name, dut=dut, mf=mf, test_result=test_result, test_number=test_number))
        return suite

    def assertTrue(self, test_result):
        print('TEST RESULT ::: ', test_result)
        if not test_result:
            print('-- TEST CASE FAILED --')
            print("-- REASON:-", self.fail_reason)
            url = self.dut.options.get('teams_webhook_url', None)
            data = {
                'summary': 'Test Case Report',
                'sections': [
                    {
                        'title': 'Test-Case details:',
                        'facts': [
                            {
                                'name': 'Test Name:',
                                'value': self.test_name
                            },
                            {
                                'name': 'Test Result:',
                                'value': '<b>Fail</b>'
                            },
                        ]
                    }
                ]
            }
            response = requests.post(url, data=json.dumps(data))
        else:
            with open("pass_logs.txt", "a") as log:
                date_now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                log.write('\n--------------------------------\n\n')
                log.write('%s. PASS CASE LOG-DATE : %s\nTEST CASE : %s\n' % (self.test_number, date_now_str, self.test_name))
                traceback.print_exc(file=log)
            print('TEST CASE NAME ::: ', self.test_name)
            print('-- TEST CASE PASSED -- PASS NUMBER:: ', self.test_number)
        
        #self.send_tc_data_to_elk()
        super().assertTrue(test_result)

    def get_end_time(self):
        end_time = None
        for timestamp in self.dut.timestamps:
            if timestamp.get('test_end_time') is not None:
                end_time = timestamp.get('test_end_time')
                break
        if end_time is None:
            end_time = time.time()
            self.dut.timestamps.append({'test_end_time': time.time()})

        return end_time

    def send_tc_data_to_elk(self):
        data = {
            'testCaseName': self.test_name,
            'durationList': self.dut.durations,
            'timestampList': self.dut.timestamps,
            'testCasePassStatus': self.test_result,
            'setupBoxAcctNo': '',
            'setupBoxDeviceCode': '',
            'setupBoxId': '',
            'setupBoxId': '',
            'videoUrl': '',
            'completionTime': str(self.get_end_time()),
            'failReason': self.fail_reason if self.fail_reason is not None else ""
        }

        url = self.dut.options.get('elk_url', None)
        print("URL:-", url)
        #print("DATA:- ",json.dumps([data]))
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps([data]),headers=headers)
        #print('RESPONSE:- ',response.json())
        print('ELK API RESPONSE STATUS CODE:- ',response.status_code)

    @staticmethod
    def memory_check():
        print('IN MEMORY CHECK')
        with open('/proc/meminfo') as file:
            for line in file:
                print(line)
                if 'MemFree' in line:
                    free_mem_in_kb = line.split()[1]
                    print(free_mem_in_kb)
                    if int(free_mem_in_kb) < 200000:
                        print('EXPLICIT APPLICATION EXIT')
                        exit()
                    break

    @staticmethod
    def merge_audio_video(video_file_path, timestamps):
        if TestCaseModule.audio_file_path is not None:
            for timestamp in timestamps:
                if timestamp.get('test_start_time') is not None:
                    start_time = timestamp.get('test_start_time')
                elif timestamp.get('audio_cmd_play_time') is not None:
                    audio_cmd_timestamp = timestamp.get('audio_cmd_play_time')
                    audio_launch_time = round(audio_cmd_timestamp - start_time, 2)
                    break
            video_1 = MGVideo("./%s" % video_file_path)
            print('VIDEO :: ', video_1)
            audio_1 = MGAudio(TestCaseModule.audio_file_path, audio_launch_time)
            print('AUOI : ', audio_1)
            merg_audio_video = MergeAudioVideo(video_file=video_1, audio_files=[audio_1])
            merg_audio_video.merge()
