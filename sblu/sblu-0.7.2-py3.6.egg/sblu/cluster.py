import re
import json as _json


def read_clusters_stream_text(stream):
    cluster_data = {
        "radius": None,
        "min_cluster_size": None,
        "max_clusters": None,
        "clusters": []
    }

    cluster = {"center": -1, "members": []}

    for line in stream:
        line_ = line.rstrip()
        if re.match(r'^Radius', line_):
            cluster_data["radius"] = float(line_.split()[1])
        elif re.match(r'^Center', line_):
            if cluster["center"] != -1:
                cluster_data["clusters"].append(cluster)
            cluster = {"center": int(line_.split()[1]) - 1,
                       "members": []}
        elif re.match(r'^[0-9]+$', line_):
            cluster["members"].append(int(line_) - 1)
        else:
            raise ValueError("Unexpected line in clusterfile.")
    cluster_data["clusters"].append(cluster)

    return cluster_data


def read_clusters(filepath):
    with open(filepath, "r") as f:
        try:
            clusters_data = _json.load(f)
        except ValueError:
            f.seek(0)
            clusters_data = read_clusters_stream_text(f)
        return clusters_data
