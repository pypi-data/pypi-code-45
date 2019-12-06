import os


def session_analyzable(directory, session):
    """
    Determines if the session is analyzeable

    :param directory:
    :param session:
    :return:
    """

    session = os.path.splitext(session)[0]
    # check if the .pos file exists
    pos_file = '%s.pos' % os.path.join(directory, session)
    if not os.path.exists(pos_file):
        # the .pos file does not exist, session is not analyzable
        return False

    # check if the .set file exists
    set_file = '%s.set' % os.path.join(directory, session)
    if not os.path.exists(set_file):
        # the .set file does not exist, session is not analyzable
        return False

    # check if session has already been analyzed
    output_directory = os.path.join(directory, 'QuadrantAnalysis')

    # session has been analyzed
    excel_filenames = ['%s_quadrant.xlsx' % os.path.join(output_directory, session),
                       '%s_inVout.xlsx' % os.path.join(output_directory, session),
                       ]

    excels_found = 0
    for file in excel_filenames:
        if not os.path.exists(file):
            return True
        else:
            excels_found += 1

    if excels_found == len(excel_filenames):
        return False

    return True
