from detection_engine import predict_attack

sample_features = [
    0,
    1,
    20,
    9,
    491,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    150,
    25,
    0.17,
    0.03,
    0.17,
    0,
    0,
    0,
    0.05,
    0
]

result = predict_attack(sample_features)

print(result)