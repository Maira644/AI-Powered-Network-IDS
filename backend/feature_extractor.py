def create_feature_vector(flow_data):

    packet_count = flow_data["packet_count"]
    total_bytes = flow_data["total_bytes"]
    duration = flow_data["duration"]

    features = [0] * 41

    features[0] = duration
    features[4] = total_bytes

    return features