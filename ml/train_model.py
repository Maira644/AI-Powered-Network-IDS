import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

columns = [
    'duration','protocol_type','service','flag','src_bytes',
    'dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell',
    'su_attempted','num_root','num_file_creations','num_shells',
    'num_access_files','num_outbound_cmds','is_host_login',
    'is_guest_login','count','srv_count','serror_rate',
    'srv_serror_rate','rerror_rate','srv_rerror_rate',
    'same_srv_rate','diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count',
    'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate',
    'dst_host_srv_serror_rate',
    'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    'label',
    'difficulty'
]

df = pd.read_csv(
    "data/KDDTrain+.txt",
    names=columns
)

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nUnique Attack Labels:")
print(df['label'].unique())

print("\nMissing Values:")
print(df.isnull().sum())


encoder_protocol = LabelEncoder()
encoder_service = LabelEncoder()
encoder_flag = LabelEncoder()

df['protocol_type'] = encoder_protocol.fit_transform(df['protocol_type'])
df['service'] = encoder_service.fit_transform(df['service'])
df['flag'] = encoder_flag.fit_transform(df['flag'])

df['label'] = df['label'].apply(
    lambda x: 0 if x == 'normal' else 1
)
print(df['label'].value_counts())


X = df.drop(['label', 'difficulty'], axis=1)
y = df['label']

print("\nFeature Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape:")
print(X_train.shape)

print("\nTesting Shape:")
print(X_test.shape)

joblib.dump(
    encoder_protocol,
    "models/protocol_encoder.pkl"
)

joblib.dump(
    encoder_service,
    "models/service_encoder.pkl"
)

joblib.dump(
    encoder_flag,
    "models/flag_encoder.pkl"
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

print("\nTraining model...")

model.fit(X_train, y_train)

print("Training completed!")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

precision = precision_score(y_test, y_pred)

print("\nPrecision:")
print(precision)

recall = recall_score(y_test, y_pred)

print("\nRecall:")
print(recall)

f1 = f1_score(y_test, y_pred)

print("\nF1 Score:")
print(f1)

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

joblib.dump(
    model,
    "models/model.pkl"
)

print("\nModel saved successfully!")

loaded_model = joblib.load(
    "models/model.pkl"
)

print("\nModel loaded successfully!")

sample_prediction = loaded_model.predict(
    X_test.iloc[:1]
)

print("\nSample Prediction:")
print(sample_prediction)