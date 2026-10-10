import re

with open('./app/src/main/AndroidManifest.xml', 'r') as f:
    content = f.read()

# Add RECEIVE_SMS permission
content = content.replace(
    '<uses-permission android:name="android.permission.INTERNET" />',
    '<uses-permission android:name="android.permission.INTERNET" />\n    <uses-permission android:name="android.permission.RECEIVE_SMS" />'
)

# Add SmsReceiver and NotificationReaderService
services = """
        <receiver android:name=".receiver.SmsReceiver" android:exported="true" android:permission="android.permission.BROADCAST_SMS">
            <intent-filter android:priority="999">
                <action android:name="android.provider.Telephony.SMS_RECEIVED" />
            </intent-filter>
        </receiver>
        
        <service android:name=".service.NotificationReaderService"
            android:label="@string/app_name"
            android:permission="android.permission.BIND_NOTIFICATION_LISTENER_SERVICE"
            android:exported="true">
            <intent-filter>
                <action android:name="android.service.notification.NotificationListenerService" />
            </intent-filter>
        </service>
"""

content = content.replace(
    '</application>',
    services + '\n    </application>'
)

with open('./app/src/main/AndroidManifest.xml', 'w') as f:
    f.write(content)
