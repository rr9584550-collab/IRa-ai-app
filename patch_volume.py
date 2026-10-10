with open('./app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'r') as f:
    content = f.read()

# Replace set_volume stub
volume_impl = """                "set_volume" -> {
                    try {
                        val audioManager = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
                        val action = args?.get("action")?.jsonPrimitive?.content ?: "up"
                        val direction = when(action) {
                            "up" -> AudioManager.ADJUST_RAISE
                            "down" -> AudioManager.ADJUST_LOWER
                            else -> AudioManager.ADJUST_SAME
                        }
                        audioManager.adjustStreamVolume(AudioManager.STREAM_MUSIC, direction, AudioManager.FLAG_SHOW_UI)
                        buildJsonObject { put("status", "success"); put("message", "Volume adjusted $action") }
                    } catch (e: Exception) {
                        buildJsonObject { put("status", "error"); put("message", e.message) }
                    }
                }"""

old_set_volume = """                "set_volume" -> {
                    Log.d("ToolEngine", "Executed stub for set_volume")
                    buildJsonObject { put("status", "success"); put("message", "Executed set_volume successfully") }
                }"""

content = content.replace(old_set_volume, volume_impl)

with open('./app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'w') as f:
    f.write(content)
