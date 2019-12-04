

def get_cols():
    """Return the column names

    Example:
    --------

    col_ids, col_typ, col_era, col_target, col_feat, (
        col_feat_1, col_feat_2, col_feat_3, col_feat_4,
        col_feat_5, col_feat_6) = get_cols()
    """
    col_feat_1 = [f"feature_intelligence{i}" for i in range(1, 12 + 1)]
    col_feat_2 = [f"feature_charisma{i}" for i in range(1, 86 + 1)]
    col_feat_3 = [f"feature_strength{i}" for i in range(1, 38 + 1)]
    col_feat_4 = [f"feature_dexterity{i}" for i in range(1, 14 + 1)]
    col_feat_5 = [f"feature_constitution{i}" for i in range(1, 114 + 1)]
    col_feat_6 = [f"feature_wisdom{i}" for i in range(1, 46 + 1)]
    col_feat = (
        col_feat_1 + col_feat_2 + col_feat_3
        + col_feat_4 + col_feat_5 + col_feat_6)

    col_target = ["target_kazutsugi"]
    col_era = ["era"]
    col_ids = ["id"]
    col_typ = ["data_type"]

    return col_ids, col_typ, col_era, col_target, col_feat, (
        col_feat_1, col_feat_2, col_feat_3, col_feat_4, col_feat_5, col_feat_6)
