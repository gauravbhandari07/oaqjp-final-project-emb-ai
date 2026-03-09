from EmotionDetection import emotion_detector

# Test 1
result = emotion_detector("I am glad this happened")
print("Test 1:", "Passed" if result["dominant_emotion"] == "joy" else "Failed")

# Test 2
result = emotion_detector("I am really mad about this")
print("Test 2:", "Passed" if result["dominant_emotion"] == "anger" else "Failed")

# Test 3
result = emotion_detector("I feel disgusted just hearing about this")
print("Test 3:", "Passed" if result["dominant_emotion"] == "disgust" else "Failed")

# Test 4
result = emotion_detector("I am so sad about this")
print("Test 4:", "Passed" if result["dominant_emotion"] == "sadness" else "Failed")

# Test 5
result = emotion_detector("I am really afraid that this will happen")
print("Test 5:", "Passed" if result["dominant_emotion"] == "fear" else "Failed")