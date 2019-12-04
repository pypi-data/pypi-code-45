import logging
from abc import ABC

import numpy as np
import pandas as pd
from numpy.linalg import LinAlgError
from pandas import DataFrame

from py_pal.complexity import ALL_CLASSES, UnderDeterminedEquation

LOGGER = logging.getLogger(__name__)


class Estimator(ABC):
    def __init__(self, tracer):
        self.tracer = tracer

    @property
    def calls(self):
        data_frame = DataFrame(
            columns=[
                Columns.CALL_ID, Columns.FUNCTION_ID, Columns.FILE, Columns.FUNCTION_LINE, Columns.FUNCTION_NAME,
                Columns.ARGS_NAMES,
                Columns.ARGS_PROXY, Columns.KWARGS_NAMES, Columns.KWARGS_PROXY, Columns.VARARGS_NAMES,
                Columns.VARARGS_PROXY, Columns.VARKW_NAMES, Columns.VARKW_PROXY,
            ],
            data=self.tracer.get_call_stats()
        )

        # Remove columns if arguments are not present
        data_frame.dropna(axis=1, how='all', inplace=True)
        LOGGER.debug(len(data_frame))
        return data_frame

    @property
    def opcodes(self):
        opcode_statistics = self.tracer.get_opcode_stats()
        if opcode_statistics.size == 0:
            return DataFrame(columns=[Columns.CALL_ID, Columns.LINE, Columns.OPCODE_WEIGHT])

        data_frame = DataFrame(
            columns=[Columns.CALL_ID, Columns.LINE, Columns.OPCODE_WEIGHT],
            data=opcode_statistics,
        )
        LOGGER.debug(len(data_frame))
        return data_frame

    # Data transformation
    def aggregate_opcodes(self, line):
        # Sum opcode weights and map them to their respective calls.
        if line:
            opcode_sum = self.opcodes.groupby(
                [Columns.CALL_ID, Columns.LINE]
            )[Columns.OPCODE_WEIGHT].agg(OpcodeWeight=np.sum).reset_index()
        else:
            opcode_sum = self.opcodes.groupby(Columns.CALL_ID)[Columns.OPCODE_WEIGHT].agg(
                OpcodeWeight=np.sum).reset_index()

        data_frame = pd.merge(self.calls, opcode_sum, on=Columns.CALL_ID)

        # Clean
        data_frame.drop_duplicates(inplace=True)
        LOGGER.debug("line=%s: %s", line, len(data_frame))
        return data_frame

    @staticmethod
    def infer_complexity(data_frame, arg_column):
        """
        Derive the big O complexity class.

        :param arg_column: Argument column to use as x-axis.
        :param data_frame: Time series-like data.
                            x-axis: argument size
                            y-axis: executed opcodes
        :return: Best fitting complexity class
        """
        best_class = None
        best_residuals = np.inf
        fitted = {}

        for class_ in ALL_CLASSES:
            inst = class_()
            residuals = inst.fit(
                data_frame[arg_column].values.astype(np.float),
                data_frame[Columns.NORM_OPCODE_WEIGHT].values.astype(np.float)
            )
            fitted[inst] = residuals

            if residuals < best_residuals - 1e-6:
                best_residuals = residuals
                best_class = inst

        return best_class


# TODO: check if complexity estimations are independent from each other (not modifying their data frames)
# TODO: handle kwargs/varargs/varkw ? what to do about all other arguments ?
class ComplexityEstimator(Estimator):
    def analyze_args_separate_ascending(self, data_frame):
        # TODO: Experimental feature make available as such
        # View separate argument axes and sort argument proxy value ascending
        for column in data_frame:
            if column == Columns.NORM_OPCODE_WEIGHT:
                continue

            # Keep influence of other arguments as low as possible by selecting rows with smallest proxy value
            args_columns = data_frame.columns.to_list()[:-1]
            data_frame = data_frame.sort_values(args_columns)
            data_frame.drop_duplicates([column, Columns.NORM_OPCODE_WEIGHT], keep='first', inplace=True)
            yield self.infer_complexity(data_frame, column), column, data_frame[[column, Columns.NORM_OPCODE_WEIGHT]]

    def analyze_all_args(self, data_frame):
        # View all argument axes together and sort argument proxy value ascending
        if Columns.ARGS_PROXY not in data_frame:
            return None, DataFrame()

        args_df = pd.DataFrame(data_frame[Columns.ARGS_PROXY].tolist(), index=data_frame.index)
        args_df['mean'] = args_df.mean(axis=1)
        args_df[Columns.NORM_OPCODE_WEIGHT] = data_frame[Columns.NORM_OPCODE_WEIGHT]

        # Take average of ArgProxy values and opcode weights
        if not args_df.empty:
            args_df = args_df.groupby('mean')[Columns.NORM_OPCODE_WEIGHT].mean().reset_index()
            args_df.sort_values('mean', inplace=True)

        return self.infer_complexity(args_df, 'mean'), args_df[['mean', Columns.NORM_OPCODE_WEIGHT]]

    @staticmethod
    def unpack_tuples(data_frame):
        # Unpack tuples of arguments
        slice = data_frame.copy()
        slice.dropna(subset=[Columns.ARGS_PROXY], inplace=True)
        unpacked_data_frame = pd.DataFrame(zip(*slice[Columns.ARGS_PROXY])).transpose()
        unpacked_data_frame[Columns.NORM_OPCODE_WEIGHT] = slice[Columns.NORM_OPCODE_WEIGHT]
        unpacked_data_frame.dropna(inplace=True, )
        return unpacked_data_frame

    @staticmethod
    def normalize_column(data_frame):
        _min = data_frame.min()
        _max = data_frame.max()
        # Replacing is needed to infer complexity
        return data_frame.apply(lambda x: (x - _min) / (_max - _min))

    def get_data_points(self, data, group_by, return_columns):
        for _, data_frame in data.groupby(group_by, sort=False):
            slice = DataFrame.copy(data_frame)
            filename = slice[Columns.FILE].values[0]
            line = slice[Columns.FUNCTION_LINE].values[0]
            function = slice[Columns.FUNCTION_NAME].values[0]
            if Columns.ARGS_NAMES in slice:
                arg_names = slice[Columns.ARGS_NAMES].values[0]
            else:
                arg_names = None

            # Normalize opcode weights for least squares
            slice[Columns.NORM_OPCODE_WEIGHT] = self.normalize_column(slice[Columns.OPCODE_WEIGHT])

            if all(map(lambda x: x in slice, return_columns)):
                data_frame_out = slice[return_columns]
            else:
                data_frame_out = DataFrame()
            yield filename, line, function, arg_names, data_frame_out

    @staticmethod
    def map_arg_names(pos, names):
        if not names:
            return ""
        if isinstance(pos, int):
            return names[pos]
        return list(map(lambda x: names[x], pos))

    def analyze_complexity(self, per_line, separate_args):
        LOGGER.info(
            '%s(per_line=%s, separate_args=%s)',
            self.analyze_complexity.__name__, per_line, separate_args
        )

        data = self.aggregate_opcodes(per_line)

        if per_line:
            iterator = self.get_data_points(
                data,
                [Columns.FUNCTION_ID, Columns.LINE],
                [Columns.ARGS_PROXY, Columns.NORM_OPCODE_WEIGHT, Columns.LINE]
            )
        else:
            iterator = self.get_data_points(
                data,
                [Columns.FUNCTION_ID],
                [Columns.ARGS_PROXY, Columns.NORM_OPCODE_WEIGHT]
            )

        for filename, line, function, arg_names, data_frame in iterator:
            LOGGER.debug("%s: %s", function, len(data_frame))
            if separate_args:
                args_df = self.unpack_tuples(data_frame)

                arg = 0
                try:
                    for best, arg_pos, data_points in self.analyze_args_separate_ascending(args_df):
                        yield filename, line, function, self.map_arg_names(arg_pos, arg_names), best, \
                              len(data_points), data_points
                except (LinAlgError, UnderDeterminedEquation) as exception:
                    yield filename, line, function, self.map_arg_names(arg, arg_names), \
                          exception.__class__.__name__, None, None
                finally:
                    arg += 1

            try:
                complexity, data_points = self.analyze_all_args(data_frame)
                yield filename, line, function, arg_names, complexity, len(
                    data_points), data_points
            except (LinAlgError, UnderDeterminedEquation) as exception:
                yield filename, line, function, arg_names, exception.__class__.__name__, None, None

    def export(self, line=False, separate=False):
        data_frame = DataFrame(
            self.analyze_complexity(line, separate),
            columns=[Columns.FILE, Columns.LINE, Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY,
                     Columns.DATA_POINTS, Columns.TRACING_DATA, ]
        )

        # Reorder columns
        cols = [Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY, Columns.LINE, Columns.FILE,
                Columns.DATA_POINTS, Columns.TRACING_DATA]
        data_frame = data_frame[cols]

        return data_frame


class PerformanceTestingAnalyzer(Estimator):
    def report(self):
        raise NotImplementedError()


class Columns:
    """Column names for the DataFrame objects used in the estimator."""
    CALL_ID = 'CallID'
    FILE = 'File'
    FUNCTION_NAME = 'FunctionName'
    ARGS_PROXY = 'ArgsProxy'
    ARGS_NAMES = 'Args'
    KWARGS_PROXY = 'KwargsProxy'
    KWARGS_NAMES = 'Kwargs'
    VARARGS_PROXY = 'VarArgsProxy'
    VARARGS_NAMES = 'VarArgs'
    VARKW_PROXY = 'VarKwProxy'
    VARKW_NAMES = 'VarKw'
    LINE = 'Line'
    FUNCTION_LINE = 'FunctionLine'
    OPCODE_WEIGHT = 'OpcodeWeight'
    NORM_OPCODE_WEIGHT = 'NormOpcodeWeight'
    ARG_DEP = 'DependentArgs'
    COMPLEXITY = 'Complexity'
    DATA_POINTS = 'DataPoints'
    TRACING_DATA = 'TracingData'
    FUNCTION_ID = 'FunctionID'
