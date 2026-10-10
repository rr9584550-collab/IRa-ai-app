with open('./app/src/main/java/com/example/service/BackgroundAudioService.kt', 'r') as f:
    content = f.read()

content = content.replace(
    'const val ACTION_STOP_ANNOUNCE = "com.example.action.STOP_ANNOUNCE"',
    '''const val ACTION_STOP_ANNOUNCE = "com.example.action.STOP_ANNOUNCE"
        const val ACTION_ANNOUNCE_SMS = "com.example.action.ANNOUNCE_SMS"
        const val ACTION_ANNOUNCE_WHATSAPP = "com.example.action.ANNOUNCE_WHATSAPP"'''
)

announce_sms_wa = """
    private fun announceSms(sender: String) {
        if (!isTtsInitialized) return
        val text = "Sir, $sender ne message kiya hai."
        tts?.speak(text, TextToSpeech.QUEUE_FLUSH, null, "SmsAnnounce")
    }

    private fun announceWhatsApp(sender: String) {
        if (!isTtsInitialized) return
        val text = "Sir, $sender ka WhatsApp message aaya hai."
        tts?.speak(text, TextToSpeech.QUEUE_FLUSH, null, "WhatsAppAnnounce")
    }

    private fun announceCall(caller: String) {"""
content = content.replace('    private fun announceCall(caller: String) {', announce_sms_wa)

intent_handling = """        if (intent?.action == ACTION_ANNOUNCE_CALL) {
            val caller = intent.getStringExtra(EXTRA_CALLER_NAME) ?: "Unknown"
            announceCall(caller)
        } else if (intent?.action == ACTION_ANNOUNCE_SMS) {
            val sender = intent.getStringExtra(EXTRA_CALLER_NAME) ?: "Unknown"
            announceSms(sender)
        } else if (intent?.action == ACTION_ANNOUNCE_WHATSAPP) {
            val sender = intent.getStringExtra(EXTRA_CALLER_NAME) ?: "Unknown"
            announceWhatsApp(sender)
        } else if (intent?.action == ACTION_STOP_ANNOUNCE) {"""
content = content.replace('        if (intent?.action == ACTION_ANNOUNCE_CALL) {\n            val caller = intent.getStringExtra(EXTRA_CALLER_NAME) ?: "Unknown"\n            announceCall(caller)\n        } else if (intent?.action == ACTION_STOP_ANNOUNCE) {', intent_handling)

with open('./app/src/main/java/com/example/service/BackgroundAudioService.kt', 'w') as f:
    f.write(content)
