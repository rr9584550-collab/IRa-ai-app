import json

with open('./app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'r') as f:
    content = f.read()

# Add context properties and flashlight logic
content = content.replace("class ToolExecutionEngine(private val context: Context) {", """class ToolExecutionEngine(private val context: Context) {

    private var isFlashlightOn = false
""")

flashlight_impl = """                "toggle_flashlight" -> {
                    try {
                        val cameraManager = context.getSystemService(Context.CAMERA_SERVICE) as android.hardware.camera2.CameraManager
                        val cameraId = cameraManager.cameraIdList[0]
                        isFlashlightOn = !isFlashlightOn
                        cameraManager.setTorchMode(cameraId, isFlashlightOn)
                        val state = if (isFlashlightOn) "on" else "off"
                        buildJsonObject { put("status", "success"); put("message", "Flashlight turned $state") }
                    } catch (e: Exception) {
                        buildJsonObject { put("status", "error"); put("message", e.message) }
                    }
                }"""

# Replace the generic toggle_flashlight stub with the real one
content = content.replace("""                "toggle_flashlight" -> {
                    Log.d("ToolEngine", "Executed stub for toggle_flashlight")
                    buildJsonObject { put("status", "success"); put("message", "Executed toggle_flashlight successfully") }
                }""", flashlight_impl)

battery_impl = """                "get_battery" -> {
                    try {
                        val batteryManager = context.getSystemService(Context.BATTERY_SERVICE) as android.os.BatteryManager
                        val batteryPct = batteryManager.getIntProperty(android.os.BatteryManager.BATTERY_PROPERTY_CAPACITY)
                        buildJsonObject { put("status", "success"); put("message", "Battery is at $batteryPct percent") }
                    } catch (e: Exception) {
                        buildJsonObject { put("status", "error"); put("message", e.message) }
                    }
                }"""

content = content.replace("""                "get_battery" -> {
                    Log.d("ToolEngine", "Executed stub for get_battery")
                    buildJsonObject { put("status", "success"); put("message", "Executed get_battery successfully") }
                }""", battery_impl)

with open('./app/src/main/java/com/example/service/ToolExecutionEngine.kt', 'w') as f:
    f.write(content)
