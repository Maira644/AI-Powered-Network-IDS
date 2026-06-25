from feature_extractor import create_feature_vector
from detection_engine import predict_attack

sample_flow = {
    "packet_count": 25,
    "total_bytes": 3000,
    "duration": 5
}

features = create_feature_vector(sample_flow)

result = predict_attack(features)

print(result)