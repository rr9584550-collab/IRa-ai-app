with open('./app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

content = content.replace(
    'Manifest.permission.READ_CALL_LOG\n                )',
    'Manifest.permission.READ_CALL_LOG,\n                    Manifest.permission.RECEIVE_SMS\n                )'
)

content = content.replace(
    'Ira needs access to your microphone to hear you, and contacts/phone to make calls on your behalf.',
    'Ira needs access to your microphone, contacts, phone, and SMS to detect and announce incoming calls and messages.'
)

with open('./app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
