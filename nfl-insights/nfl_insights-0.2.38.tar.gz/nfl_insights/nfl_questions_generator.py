import pandas as pd
import numpy as np
import random
import os
import json
from pathlib import Path
import logging
import math

from contendo_utils import *
from nfl_insights import *

eval(NFL_LANGUAGE_FILENAME_EVAL)

class NFLQuestions:
    @contendo_classfunction_logger
    def __init__(self, season=NFL_DEFAULT_SEASON, ostats=None):
        # load the definition file
        self.language = ProUtils.get_dict_from_jsonfile(eval(NFL_LANGUAGE_FILENAME_EVAL))
        # get ostats from external caller or initialize it.
        self._teamStats = ostats
        if ostats is None:
            self._teamStats = NFLTeamAnalytics([season])

        self.ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])

    @contendo_classfunction_logger
    def _generate_all_questions(self, calculationsFilter=None, statsFilter=None):
        if not calculationsFilter:
            calculationsFilter = self.language['entities']['calculations'].keys()
        logger.debug('Generating all stats for calculation: %s', calculationsFilter)
        if not statsFilter:
            statsFilter = self._teamStats.statsDict.keys()
        logger.debug('Generating all stats: %s', statsFilter)
        self._columns = ['qScore', 'questionRank', 'Text', 'Option1', 'Option2', 'Answer', 'dimensionText', 'dimprep', 'statnameText',
                         'ObjectDescription', 'dimensions', 'statObject', 'statName', 'calculation', 'teamId',
                         'teamName', 'statValue', 'count', 'rank', 'statRange', 'nRanks', 'teamId2', 'teamName2',
                         'statValue2', 'count2', 'rank2', 'rankDiff', 'Sentiment', 'Template', 'AnswerTemplate']
        outfile = open(NFL_TEMP_QUESTIONS_FILE, 'w')
        _writeHeaders = True
        self.questionsDF = pd.DataFrame(columns=self._columns)
        for key1, _statDict in self._teamStats.allStatsDict.items():
            _season, _statname, _object = key1
            if not _statname in statsFilter:
                continue
            logger.debug('Covering main key: %s', key1)
            for key2, statTable in _statDict.items():
                _dims, _calculation = key2
                if not _calculation in calculationsFilter:
                    continue

                if _dims != str(['all', 'all']):
                    _dim=list(set(eval(_dims))-{'all'})[0]
                    _dimdef = self._teamStats.generator.dimentionsDict[_dim]
                    if _dimdef['DoQuestion']!=1:
                        continue
                    pass
                logger.debug('Getting questions for %s, %s', key1, key2)
                _questionsTable = self._get_stat_questions(statTable)
                _dimensions = eval(_dims)
                _questionFunc = getattr(self, '_do_' + _calculation)
                _questionsDF = _questionFunc(_questionsTable, _statname, _object, _dimensions, _calculation)
                # write to file
                if _questionsDF.shape[0] > 0:
                    _questionsDF.to_csv(outfile, index=False, header=_writeHeaders)
                    # write header only in the first time
                    _writeHeaders = False
            # break
        outfile.close()
        # loading the file, sorting & saving
        self.questionsDF = pd.read_csv(NFL_TEMP_QUESTIONS_FILE)
        self.questionsDF.sort_values(by=['questionRank', 'qScore'], axis=0, inplace=True, ascending=True)
        self.questionsDF.to_csv(NFL_QUESTIONS_FILE, index=False)


    def _do_stat(self, questionsTable, statName, object, dimensions, calculation):
        return self._get_questions_df(questionsTable, statName, object, dimensions, calculation)

    def _do_ratio(self, questionsTable, statName, object, dimensions, calculation):
        return self._get_questions_df(questionsTable, statName, object, dimensions, calculation)

    def _do_pct(self, questionsTable, statName, object, dimensions, calculation):
        return self._get_questions_df(questionsTable, statName, object, dimensions, calculation)

    def _do_per_game(self, questionsTable, statName, object, dimensions, calculation):
        return self._get_questions_df(questionsTable, statName, object, dimensions, calculation)

    def _do_per_drive(self, questionsTable, statName, object, dimensions, calculation):
        return self._get_questions_df(questionsTable, statName, object, dimensions, calculation)

    def _do_per_play(self, questionsTable, statName, object, dimensions, calculation):
        return self._get_questions_df(questionsTable, statName, object, dimensions, calculation)

    @contendo_classfunction_logger
    def _get_questions_df(self, questionsTable:pd.DataFrame, statName: str, object: str, dimensions: list, calculation: str) -> pd.DataFrame:
        result=pd.DataFrame()

        if 'all' not in dimensions:
            return result

        rawStatements = self._get_questions(questionsTable, dimensions, calculation)
        if rawStatements.shape[0] > 0:
            # logger.info(rawStatements.columns)
            result = rawStatements[self._columns]

        return result

    @contendo_classfunction_logger
    def _get_stat_questions(self, statDF: pd.DataFrame) -> pd.DataFrame:
        import math
        _fields = ['teamId', 'teamName', 'statValue', 'count', 'rank']
        _df1 = statDF.reset_index().query('statValue!=0')[_fields]
        _df1['rank'] = _df1['statValue'].rank(method='dense', ascending=False)
        _df1['on'] = 1
        _df1.set_index('on', inplace=True)
        _df1['statRange'] = _df1['statValue'].max() - _df1['statValue'].min()
        _df1['nRanks'] = _df1['rank'].nunique()
        #_df2 = _df1[['teamId', 'teamName', 'statValue', 'count', 'rank', 'nGames', 'nDrives', 'nPlays']]
        _df2 = _df1[_fields]
        _joinedDF = _df1.join(_df2, lsuffix='', rsuffix='2')
        _joinedDF = _joinedDF.query('rank<rank2').copy()
        if _joinedDF.shape[0]==0:
            return pd.DataFrame()
        _joinedDF.reset_index(inplace=True)
        _joinedDF['rankDiff'] = _joinedDF['rank2'] - _joinedDF['rank']
        _joinedDF['qScore'] =  _joinedDF.apply(
            lambda x: (1-math.fabs(x['statValue']-x['statValue2'])/x['statRange'])*100 +
                       (x['rank']/x['nRanks']*350 if x['rank']<x['nRanks']*0.2 else 70+x['rank']/x['nRanks']*30),
            axis=1
        )
        _sdfRow = dict(statDF.iloc[0])
        for key in ['dimensions', 'statObject', 'statName', 'calculation']:
            _joinedDF[key] = _sdfRow[key]
        _joinedDF.sort_values('qScore', ascending=True, inplace=True)
        _joinedDF['questionRank'] = round(_joinedDF['qScore'].rank(method='min', pct=True, ascending=True)*100)
        return _joinedDF

    @contendo_classfunction_logger
    def _get_questions(self, questionsTable: pd.DataFrame, dimensions: dict, calculation: str) -> pd.DataFrame():
        # get interesting questions for a stat table - numst is number of top and bottom questions
        # result may be up to 2Xnumst questions
        # interest here is non contextual and based on standard deviation only
        _questions = list()

        for i, row in questionsTable.iterrows():
            _questionRow = dict(row)
            self._update_question_fields(_questionRow)
            _questions.append(_questionRow)

        retDF = pd.DataFrame(_questions, columns=self._columns)
        return retDF

    @contendo_classfunction_logger
    def _update_question_fields(self, questionRow: dict) -> None:
        # get stat text
        _statdef = self.language['entities']['statnames'][questionRow['statName']][questionRow['statObject']]
        _statsentences = _statdef['sentences']
        _statText = _statsentences[random.randint(0, len(_statsentences) - 1)]
        # get the dimensions
        _dimList = eval(questionRow['dimensions'])
        if all(x == 'all' for x in _dimList):
            _dimensionText = ""
            _dimpreposition = ""
        else:
            _dimIndex = int(not _dimList.index('all'))
            _dimensionText = self.language['entities']['dimensions'][_dimList[_dimIndex]]['text']
            _dimpreposition = self.language['entities']['dimensions'][_dimList[_dimIndex]]['prep']
        # calculate rank text
        _ranklist1 = self.language['entities']['ranks'][str(int(questionRow['rank']))]
        _rankText1 = _ranklist1[random.randint(0, len(_ranklist1) - 1)]
        _rankText2 = self.ordinal(int(questionRow['rank2']))
        # get object description
        _objectDescriptions = self.language['entities']['objectDescriptions'][questionRow['statObject']]
        _objectDescription = _objectDescriptions[random.randint(0, len(_objectDescriptions) - 1)]
        # get calculation description
        _calculation = questionRow['calculation']
        _calculationDef = self.language['entities']['calculations'][_calculation]
        _calculationTexts = _calculationDef['texts']
        _calculationText = _calculationTexts[random.randint(0, len(_calculationTexts) - 1)]
        # get the template
        _sentiment = 'positive' if _statdef['isPositive'] else 'negative'
        _calc = _calculation
        if _calc.find('per_') == 0:
            _calc = 'stat'
        _templates = self.language['templates']['questions'][_calc][_sentiment]
        _templateIndex = random.randint(0, len(_templates) - 1)
        _template = _templates[_templateIndex]
        _optionTemplate = self.language['templates']['questions']['option']
        _answerList = self.language['templates']['questions']['answer']
        _answerTemplate = _answerList[random.randint(0, len(_answerList) - 1)]
        # format the value
        _valueFormat = _calculationDef.get('format', _statdef.get('format', '{:.f}'))
        _statFormatedValue1 = _valueFormat.format(float(questionRow['statValue']))
        _statFormatedValue2 = _valueFormat.format(float(questionRow['statValue2']))

        _questionFormat = {
            'dimensionText': _dimensionText,
            'dimprep': _dimpreposition,
            'statnameText': _statText,
            'ObjectDescription': _objectDescription,
            'calculationText': _calculationText,
        }

        _questionText = _template.format(**_questionFormat).replace(' ?', '')
        # remove double blanks
        while _questionText.find('  ') > -1:
            _questionText = _questionText.replace('  ', ' ')

        _answerFormat = {
            'subject1': questionRow['teamName'],
            'rankText1': _rankText1,
            'X1': _statFormatedValue1,
            'subject2': questionRow['teamName2'],
            'rankText2': _rankText2,
            'X2': _statFormatedValue2,
            'ObjectDescription': _objectDescription,
        }

        _answerText = _answerTemplate.format(**_answerFormat)
        # remove double blanks
        while _answerText.find('  ') > -1:
            _answerText = _answerText.replace('  ', ' ')

        # keep the text, template & sentiment
        questionRow['Text'] = _questionText
        questionRow['Option1'] = _optionTemplate.format(subject=questionRow['teamName'], **_questionFormat)
        questionRow['Option2'] = _optionTemplate.format(subject=questionRow['teamName2'], **_questionFormat)
        questionRow['Answer'] = _answerText
        questionRow['Sentiment'] = _sentiment
        questionRow['Template'] = _template
        questionRow['AnswerTemplate'] = _answerTemplate
        for key, value in _questionFormat.items():
            questionRow[key] = value

        return


@contendo_function_logger
def test():
    logger.info('Starting...')
    os.chdir('{}/tmp/'.format(os.environ['HOME']))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '{}/sportsight-tests.json'.format(os.environ['HOME'])
    nflq = NFLQuestions(season=NFL_DEFAULT_SEASON, ostats=None)
    # nflq._refactor_definition_json()
    # return
    #nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'pct', 'per_game', 'per_drive'], statsFilter=[])
    #nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'per_game'], statsFilter=[])
    #nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'per_game'], statsFilter=['offensePoints', 'fumbles', 'yardsRushed', 'completionRate'])
    nflq._generate_all_questions(calculationsFilter=['ratio'], statsFilter=[])
    # Sort the sentences
    # uploading the sentences - uncomment only when you want to upload them to the cloud and the demo.
    # nflq._ostats.generator.nfldata.bqu.upload_file_to_gcp(bucketName=NFL_GCP_BUCKET, inFileName=NFL_SENTENCES_FILE, targerFileName=NFL_SENTENCES_FILE, timestamp=True)
    logger.info('Done')


if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.DEBUG)
    pd.set_option('display.max_rows', 1500)
    pd.set_option('display.max_columns', 1500)
    pd.set_option('display.width', 20000)
    test()
