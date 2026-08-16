import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

dataset_path = "dataset"

datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),
    batch_size=4,
    class_mode="categorical",
    subset="training"
)

validation_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),
    batch_size=4,
    class_mode="categorical",
    subset="validation"
)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(
        32, (3, 3),
        activation="relu",
        input_shape=(128, 128, 3)
    ),

    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(
        64, (3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        128,
        activation="relu"
    ),

    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(
        4,
        activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=10
)

model.save("model/image_classifier.keras")

print("Model training completed!")