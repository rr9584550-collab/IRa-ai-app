with open('./app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'r') as f:
    content = f.read()

# Add imports
imports = """import android.media.AudioManager
import android.view.KeyEvent
"""
content = content.replace('import android.content.Context\n', 'import android.content.Context\n' + imports)

# Replace play_music and media_control stubs
media_impl = """                "play_music", "media_control" -> {
                    try {
                        val audioManager = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
                        
                        val action = args?.get("action")?.jsonPrimitive?.content ?: "play_pause"
                        val keyCode = when(action) {
                            "play" -> KeyEvent.KEYCODE_MEDIA_PLAY
                            "pause" -> KeyEvent.KEYCODE_MEDIA_PAUSE
                            "next" -> KeyEvent.KEYCODE_MEDIA_NEXT
                            "previous" -> KeyEvent.KEYCODE_MEDIA_PREVIOUS
                            else -> KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE
                        }
                        
                        val eventDown = KeyEvent(KeyEvent.ACTION_DOWN, keyCode)
                        audioManager.dispatchMediaKeyEvent(eventDown)
                        val eventUp = KeyEvent(KeyEvent.ACTION_UP, keyCode)
                        audioManager.dispatchMediaKeyEvent(eventUp)
                        
                        buildJsonObject { put("status", "success"); put("message", "Media action \$action dispatched successfully") }
                    } catch (e: Exception) {
                        buildJsonObject { put("status", "error"); put("message", e.message) }
                    }
                }"""

# We have these lines:
old_play_music = """                "play_music" -> {
                    Log.d("ToolEngine", "Executed stub for play_music")
                    buildJsonObject { put("status", "success"); put("message", "Executed play_music successfully") }
                }"""
old_media_control = """                "media_control" -> {
                    Log.d("ToolEngine", "Executed stub for media_control")
                    buildJsonObject { put("status", "success"); put("message", "Executed media_control successfully") }
                }"""

content = content.replace(old_play_music, media_impl)
content = content.replace(old_media_control, "")

with open('./app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'w') as f:
    f.write(content)
